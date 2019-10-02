import argparse
import os
import subprocess

parser = argparse.ArgumentParser(description="Script is to free the given port")
parser.add_argument('port',type=int,help="Enter the port numbrt")
linewithlisten = None
portp = parser.parse_args().port
result = subprocess.run(['lsof','-n',"-i4444TCP:%s" % portp],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
processtoKill = None
for lines in result.stdout.splitlines():
    print(str(lines))
    if "LISTEN" in str(lines):
        linewithlisten = str(lines)
        processtoKill = int(linewithlisten.split()[1])
        break
if linewithlisten:
    print("found line")
    os.kill(processtoKill,9)
    print("Process Killed")
else:
    print(f"No such process with port {portp}")
    exit(1)
