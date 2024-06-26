from mod.colorprint import colorprint
import subprocess
import sys
import os

if len(sys.argv) == 1:
    long = os.listdir(".")
    long = [int(x) for x in long if x not in ["main.py", "mod"]]
    long.sort()
    long = [str(x) for x in long]
    for nb in long:
        os.system(f"python main.py {nb}")
else:
    testnb = int(sys.argv[1])
    # TODO : subprocess run
    command = f"python ./{testnb}/test.py"
    p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    if p.stdout is None:
        colorprint("Error : couldnt open a subprocess", color = "red")
        exit(1)
    if p.stdout.read() != b'':
        colorprint(f"{testnb} : ERREUR", color = "red")
        os.system(command)
    else:
        colorprint(f"{testnb} : OK", color = "green")