# a script by https://github.com/iordakis

import sys
import psutil


proclist = []
proccesscount = 1
for proc in psutil.process_iter(): # appending current running processes to list
    if proc.name() == 'target-program.exe':
        proclist.append(proc)

for proccesscount, item in enumerate(proclist): # counting total instances of the target executable
    print('Process found: ', proccesscount)

if proccesscount >= 2:
    print("Only one instance allowed to run!")
    time.sleep(3)
    sys.exit() # this stops the python script. replace with your desired command

proclist = str(proclist) # converting list to string after counting list elements above

if 'target-program.exe' not in proclist: # denies changing executable name that can avoid instance counting above
    print("Changing executable name not allowed!")
    time.sleep(3)
    sys.exit() # this stops the python script. replace with your desired command
