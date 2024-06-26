from mod.colorprint import colorprint
import subprocess
import requests
import sys
import os

PRECISION = 4

if len(sys.argv) == 1:
    todo_file = open('TODO', "r").readlines()
    todo_file = [(x[:-1] if x[-1] == "\n" else x) for x in todo_file]
    colorprint("Problems to do :", color = "blue")
    for x in todo_file:
        colorprint(x, color = "blue")
    result = requests.get("https://alfa-leetcode-api.onrender.com/userProfile/Sarenard").json()
    colorprint(f"Total : {result['totalSolved']}/{result['totalQuestions']} (\
{round(result['totalSolved']/result['totalQuestions'], PRECISION)}%)", color = "cyan")
    colorprint(f"Easy : {result['easySolved']}/{result['totalEasy']} (\
{round(result['easySolved']/result['totalEasy'], PRECISION)}%)", color = "green")
    colorprint(f"Medium : {result['mediumSolved']}/{result['totalMedium']} (\
{round(result['mediumSolved']/result['totalMedium'], PRECISION)}%)", color = "yellow")
    colorprint(f"Hard : {result['hardSolved']}/{result['totalHard']} (\
{round(result['hardSolved']/result['totalHard'], PRECISION)}%)", color = "red")
    long = os.listdir(".")
    long = [int(x) for x in long if x not in ["main.py", "mod", "TODO"]]
    long.sort()
    long = [str(x) for x in long]
    for nb in long:
        os.system(f"python main.py {nb}")
else:
    testnb = int(sys.argv[1])
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