#!/usr/bin/env python3

import time
import subprocess
import os
from pathlib import Path
import psutil
from datetime import datetime
import argparse
import sys
import shlex

class RAPLMonitor:
    def __init__(self):
        self.rapl_dir = Path("/sys/class/powercap/intel-rapl")
        self.supports_rapl = self.rapl_dir.exists()
        self.energy_files = []
        
        if self.supports_rapl:
            # Find all energy_uj files (microjoules)
            for path in self.rapl_dir.rglob("energy_uj"):
                if path.is_file():
                    self.energy_files.append(path)
    
    def read_energy(self, path):
        try:
            with open(path, 'r') as f:
                return int(f.read().strip())
        except (IOError, ValueError):
            return 0
    
    def get_energy_readings(self):
        """Get energy readings from all RAPL domains"""
        return {str(path): self.read_energy(path) for path in self.energy_files}

class PowerProfiler:
    def __init__(self):
        self.rapl_monitor = RAPLMonitor()
    
    def profile(self, command):
        """
        Profile a command's execution time and power usage
        Args:
            command (str): Command to execute
        Returns:
            dict: Profiling results
        """
        # Initial readings
        start_time = time.perf_counter_ns()
        start_cpu_times = psutil.cpu_times()
        start_energy = self.rapl_monitor.get_energy_readings()
        
        # Get initial CPU frequency
        start_freq = psutil.cpu_freq(percpu=True) if hasattr(psutil, 'cpu_freq') else None
        
        # Execute command
        process = subprocess.run(command, shell=True, capture_output=True, text=True)
        
        # Final readings
        end_time = time.perf_counter_ns()
        end_cpu_times = psutil.cpu_times()
        end_energy = self.rapl_monitor.get_energy_readings()
        end_freq = psutil.cpu_freq(percpu=True) if hasattr(psutil, 'cpu_freq') else None
        
        # Calculate metrics
        execution_time_ns = end_time - start_time
        execution_time_ms = execution_time_ns / 1_000_000
        
        # RAPL energy calculations
        energy_usage = {}
        for path in self.rapl_monitor.energy_files:
            path_str = str(path)
            energy_diff = end_energy[path_str] - start_energy[path_str]
            domain_name = path.parent.name
            energy_usage[domain_name] = energy_diff
        
        # CPU utilization
        cpu_user = end_cpu_times.user - start_cpu_times.user
        cpu_system = end_cpu_times.system - start_cpu_times.system
        
        return {
            'command': command,
            'timestamp': datetime.now().isoformat(),
            'execution_time_ms': execution_time_ms,
            'execution_time_ns': execution_time_ns,
            'rapl_energy_usage_uj': energy_usage,
            'cpu_time_user': cpu_user,
            'cpu_time_system': cpu_system,
            'stdout': process.stdout,
            'stderr': process.stderr,
            'return_code': process.returncode,
            'rapl_supported': self.rapl_monitor.supports_rapl
        }

def format_results(results):
    """Format profiling results for display"""
    output = []
    output.append(f"Profile results for: {results['command']}")
    output.append(f"Timestamp: {results['timestamp']}")
    output.append(f"\nPerformance Metrics:")
    output.append(f"Execution time: {results['execution_time_ms']:.3f} ms ({results['execution_time_ns']} ns)")
    output.append(f"CPU time (user): {results['cpu_time_user']:.3f} seconds")
    output.append(f"CPU time (system): {results['cpu_time_system']:.3f} seconds")
    
    if results['rapl_supported']:
        output.append("\nCPU Power Usage (RAPL):")
        for domain, energy in results['rapl_energy_usage_uj'].items():
            output.append(f"  {domain}: {energy} µJ ({energy/1_000_000:.3f} J)")
    
    if results['return_code'] != 0:
        output.append(f"\nWarning: Command returned non-zero exit code: {results['return_code']}")
    
    #Print the program Output
    #if results['stdout']:
    #    output.append(f"\nStandard output:\n{results['stdout']}")
    #if results['stderr']:
    #    output.append(f"\nStandard error:\n{results['stderr']}")
        
    return "\n".join(output)

def main():
    parser = argparse.ArgumentParser(
        description='Profile execution time and power usage of a command',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s "python3 script.py"
  %(prog)s "ls -la"
  %(prog)s "sleep 5"
        """
    )
    
    parser.add_argument(
        'command',
        help='Command to profile (use quotes for commands with arguments)',
        type=str,
        nargs=argparse.REMAINDER
    )
    
    parser.add_argument(
        '-o', '--output',
        help='Output file for results (default: stdout)',
        type=argparse.FileType('w'),
        default=sys.stdout
    )
    
    parser.add_argument(
        '--json',
        help='Output results in JSON format',
        action='store_true'
    )

    args = parser.parse_args()

    if not args.command:
        parser.error("No command provided to profile")
        
    # Reconstruct the command string
    command = ' '.join(args.command)
    
    try:
        profiler = PowerProfiler()
        results = profiler.profile(command)
        
        if args.json:
            import json
            # Convert results to JSON-serializable format
            json_results = {k: v for k, v in results.items() if isinstance(v, (dict, list, str, int, float, bool, type(None)))}
            print(json.dumps(json_results, indent=2), file=args.output)
        else:
            formatted_results = format_results(results)
            print(formatted_results, file=args.output)
        
        if args.output is not sys.stdout:
            args.output.close()
            print(f"Results written to {args.output.name}")
            
    except KeyboardInterrupt:
        print("\nProfiling interrupted by user", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error during profiling: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
