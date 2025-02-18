# Week 5 worksheet
The goal of today is to explore the effect of offloading computation from the CPU to the GPU, exploring the maximum potential for reducing the energy implicated with doing so.  The GPU in most lab machines on campus is the onboard Intel graphics which is considerably lower power draw than a dedicated GPU found in most gaming machines and high end AI or graphics machines.  Recall, that processors increasingly have other co-processors, such as Intel's NPU, for accelerating operations for machine learning - which also might perform specialist parallel instructions with good compute/energy performance.  *You should keep this in mind when generalising from your findings!*

**We will use the same measurement setup as last week, so I again strongly recommend you do this on the lab machine, and not on your home machine or laptop.  It does not work on the VM with virtualised hardware.**

## Taking good measurements

Reminder:

1. You should aim to take good, repeatable measurements, **minimising interference from other tasks on the system**.
2. You should run each test multiple times to get several measurements and take a mean and standard deviation.
3. Measuring the GPU is more difficult, so you will need to look more closely at the numbers coming back from the profiling script to isolate the CPU cores and GPU from the rest, see below.
4. I'd suggest running **each test 5 times**, providing **all** of the readings in your report markdown fie.
5. You should do a 'warmup' run before taking your measurements, not least because this task **downloads a large data file at startup**.  Be careful **not to include** the download and data loading time in your benchmark results.  **Take care also to remove or not include the data file in your git repo!**

We're going to use a test which forecasts data points from a [linear regression](https://www.geeksforgeeks.org/ml-linear-regression/) using python for [this task](https://uxlfoundation.github.io/scikit-learn-intelex/latest/samples/linear_regression.html) which utilises the [`scitkit-learn`](https://scikit-learn.org/stable/) package and GPU extension by Intel).

## Understanding Intel RAPL channels

The profiler script will give you a block of output like this:

```
Performance Metrics:
Execution time: 6402.042 ms (6402042057 ns)
CPU time (user): 16.690 seconds
CPU time (system): 0.680 seconds

CPU Power Usage (RAPL):
  intel-rapl:0: 133020839 µJ (133.021 J)
  intel-rapl:0:0: 123113210 µJ (123.113 J)
  intel-rapl:0:1: 7812 µJ (0.008 J)
```

If you're curious, read about `user` and `system` time in this helpful answer to [this stackoverflow question](https://stackoverflow.com/questions/556405/what-do-real-user-and-sys-mean-in-the-output-of-time1).

Note that the `intel-rapl:` corresponds to different MSRs (module specific registers) on your Intel processor.  These are normally:

Channel | Value | Meaning
----|----|----
`intel-rapl:0:`| 133020839 µJ (133.021 J)| Overall 'package' energy (all parts of the CPU package, including CPU and GPU)
`intel-rapl:0:0:` | 123113210 µJ (123.113 J) | Channel 0 is the 'CPU cores' part of the package
`intel-rapl:0:1:` | 7812 µJ (0.008 J) | "Normally" the GPU

Note that 0.008 Joules is tiny, so probably more significant in interpreting your results is the difference between the package and CPU channels and estimating 'what is saved' by the GPU by taking workload from the processor between test variants. The energy saved should really be *not just the difference in load*, but *also the reduced execution time*.  **You'll need to take this into account and explain your working out in your markdown report.**

## Task

Time available: 1 hour:

Make sure you have an up to date copy of your coursework repo available.  In the '`week5`' folder create a new markdown document called `username-week5-labnotes.md`.

1. Run the terminal, and switch into a python virtual environment for our course^[[About python virtual environments](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/#create-and-use-virtual-environments).]

	```bash
	source /usr/local/lib/python-venv/scc-243/bin/activate
	```
	
	This should provide all the python packages we're going to use without the need to download and install them.
	
2. Download the [profiler.py](../week4/profiler.py) script we used last week (or copy it from last week's folder - *it hasn't changed*.)

3. Download the two test files [test-cpu.py](test-cpu.py) and [test-gpu.py](test-gpu.py).  This is the same code, the only difference being that with `test-cpu.py` all the calculation is done on the CPU cores.

4. Run the test case to 'warm up' the system (*load packages and data files for the first time*).

	```bash
	python test-cpu.py
	```
	
5. Run each test case at least 5 times, noting down the test case, energy and time taken for each.  e.g. using:

	```bash
	./profiler.py "python test-cpu.py"
	```
	**Important note: the profiler.py swallows the output from the task, so I'd recommend running the task to verify it's running ok, before running under the energy profiler.  Especially, if the task completion time and energy used is suspiciously small!**

6. Document your experiment *in markdown format*, using markdown tables as last week.  Add an *introductory paragraph* on what you plan to measure and your 'method statement' of how you've conducted your tests.  *Take care to explain how you are calculating the energy saved.*
5. For each test case, add a subsection with the goal of the test, *the command line* you've used and a table with the results.
6. The table should have the results of each test run, how much time it took and how many Joules of energy and total watt/hours.
7. Finish the table with the average time taken and standard deviation.
8. Add a subsection called `## Reflections` which summarises what you've found, and any personal observations on the number of Watt's associated with the computations.  How much energy was saved by offloading from CPU to GPU and speeding up the task?  If you ran this task for an entire day, week, month or year how many kWh would be used for CPU and GPU variants?

Don't forget to `git add` your new file, `commit` and `push` to the server at least at the end of the task.  **Take care not to add the 'data' folder to your git repository - it contains an enormous data file that you don't need to keep!**  You can remove it with `git rm -r data` or on `scc-source` if you need to.

## Learning outcomes
* You should have an appreciation of how energy varies with CPU vs. GPU computation
* Should reinforce your expirimental method, i.e. how to take measurements, calculate a difference in energy saved and report them in a systematic way
* A 'ready reckoning' of the bounds for energy saving due to reducing load on the CPU by shifting workloads to the GPU
* An appreciation of how efficient GPU cores are for offloading parallel mathematical tasks (e.g. vector matrix operations)

<!-- ## Going further

* [https://pawseysc.github.io/sc20-gpu-offloading/](https://pawseysc.github.io/sc20-gpu-offloading/) -->
