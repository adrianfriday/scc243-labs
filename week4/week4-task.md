# Week 4 worksheet
The goal of today is to learn how to take energy measurements associated with running specific software.  We'll be indirectly using the Intel RAPL energy reporting from the CPU in your lab machine.  Note, this is specific to Intel processors, so will not work directly on anything else (e.g. a Mac with Apple Silicon, Google Chromebook etc.)

**In short: I strongly recommend you do this on the lab machine, and not on your laptop.**

## Taking good measurements

Really, we're taking a snapshot of the energy use of the CPU from the time we start measuring to the time the task is complete.

1. This could catch any computation going on, not just your code, so we should aim for **Isolation**, i.e. trying not to get data that's confounded by other software and hardware running at the same time
2. Ideally, recognise that the measurement framework may add additional **overhead** (hopefully in this case it should be relatively constant for all tests)
3. Understanding how much is **missed** by what we are able to measure (for example, RAPL measures the CPU, but not the memory, I/O subsystems or anything else that makes up the total system energy)
4. **Repeatable** and **representative** test selection.  We should run tests more than once and take an average (arithmetic mean) and standard deviation.  We should report each run and the average.  I'd suggest running each test 5 times.

Normally, test selection would involve picking representative use cases or data sets to ensure that data or interaction dependent behaviour is captured.  In our case for this lab, we're going to use a CPU stress testing framework to make the test development process simpler.

## Task

Time available: 1 hour:

Make sure you have an up to date copy of your coursework repo available (`git clone` or `git pull` as needed to ensure you are up to date with the server), as before.  In the '`week4`' folder create a new markdown document called `username-week4-labnotes.md`, named with your user as in past weeks.

1. Read about `stress-ng` [a system stress testing framework](https://github.com/ColinIanKing/stress-ng)
2. Select 3 tests that exercise the CPU (as that's what we're going to measure)
3. Download [this python script](profiler.py) which we'll use for energy reporting from [Intel's RAPL API](https://greencompute.uk/Measurement/RAPL).  This is a python script and **needs to be executable** - you may need to change it's file permissions (e.g. `chmod u+x profiler.py` in the terminal shell)
4. In your markdown report, add an introductory paragraph on what you plan to measure and your 'method statement' of how you've conducted your tests
5. For each test case, add a subsection with the goal of the test, the command line you've used and a table with the results.
6. The table should have the results of each test run, how much time it took and how many joules of energy
7. Finish the table with the average time taken and standard deviation.  You could use a spreadsheet like excel, or a stats package like R (see [getting started reference](https://education.rstudio.com/learn/beginner/))
8. For each test case add a summary converting from Joules to Watts (e.g. [using a converter](https://www.rapidtables.com/calc/electric/Joule_to_Watt_Calculator.html), or by hand)
9. Add a subsection called `## Reflections` which summarises what you've found, and any personal observations on the number of Watt's associated with the computations.  How much variability was there between the tests; how does the energy compare with say a 12W LED, or watching TV for an hour?

Don't forget to `git add` your new file, `commit` and `push` to the server at least at the end of the task.

## Learning outcomes
* You should have an appreciation of how energy varies with computation
* Should know how to take measurements in a systematic way
* Should know how each run varies at a system level, and the challenges of apportioning to specific running software
* A 'ready reckoning' of the bounds for energy saving due to reducing load on the CPU