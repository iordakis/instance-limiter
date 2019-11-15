# a script by https://github.com/iordakis

import sys
import psutil

targetProgram1 = 'yourtargetprogram.exe' # your target program
targetProgram2 = 'YOURTA~1.EXE' # in some systems the process name is truncated to maximum 8 chars, and also capitalized.
procList = []
proccessCount = 1

for proc in psutil.process_iter(): # appending current target running processes to list
    if proc.name() == targetProgram1 or proc.name() == targetProgram2:
        procList.append(proc)

for proccessCount, item in enumerate(procList): # counting total instances of the target program
    print('Process found: ', proccessCount, proc)

if proccessCount >= 2: # prevents running more than one instance of the target program
    print("Only one instance allowed to run!")
    time.sleep(3)
    sys.exit() # this stops the python script. replace with your desired command

procList = str(procList) # converting list to string after counting list elements above

if targetProgram1 not in procList and targetProgram2 not in procList: # prevents changing program file name that can avoid instance counting above
    print("Changing program file name not allowed!")
    time.sleep(3)
    sys.exit() # this stops the python script. replace with your desired command
