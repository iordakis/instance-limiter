A script by https://github.com/iordakis/

DESCRIPTION:

A solution to prevent running more than one instance of a program inside a Windows OS.

If more than one instance of the same process is detected, the script will force-close the target process.

The script will also terminate the execution of the target process if the program filename was modified. (This prevents bypassing the process count filter)

USE CASES:

Providing or licensing an app which is having some form of output limitations in a given amount of time.
Thus, the instance limiter prevents the user to generate a large output volume in a relatively shorter time-span by running multiple instances of your app.

IMPLEMENTATION:

For executables: Before compiling your Python code to an executable, add the instance limiter code anywhere in your main code file.
The code can also be used for non-Python-based apps, as an external control trigger with your own adaptations hooks.
