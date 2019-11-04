A script by https://github.com/iordakis/

A solution to prevent running more than one instance of a program.
The script can be implemented at the start of your existing python code, or used as an external trigger with your adaptations.

It will terminate the python code execution if the target program is opened a second time in the system.
It will also terminate the python code execution if the target program file name was modified. (this prevents avoiding the process counting which will result in bypassing the filter)
