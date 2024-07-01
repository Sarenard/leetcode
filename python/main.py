from mod.colorprint import colorprint
import subprocess
import requests
import sys
import os

PRECISION = 4

def show():
    todo_file = open('TODO', "r").readlines()
    todo_file = [(x[:-1] if x[-1] == "\n" else x) for x in todo_file]
    colorprint("Problems to do :", color = "blue")
    for x in todo_file:
        colorprint(x, color = "blue")
    result = requests.get("https://alfa-leetcode-api.onrender.com/userProfile/Sarenard").json()
    colorprint(f"Total : {result['totalSolved']}/{result['totalQuestions']} (\
{round(result['totalSolved']/result['totalQuestions']*100, PRECISION)}%)", color = "cyan")
    colorprint(f"Easy : {result['easySolved']}/{result['totalEasy']} (\
{round(result['easySolved']/result['totalEasy']*100, PRECISION)}%)", color = "green")
    colorprint(f"Medium : {result['mediumSolved']}/{result['totalMedium']} (\
{round(result['mediumSolved']/result['totalMedium']*100, PRECISION)}%)", color = "yellow")
    colorprint(f"Hard : {result['hardSolved']}/{result['totalHard']} (\
{round(result['hardSolved']/result['totalHard']*100, PRECISION)}%)", color = "red")

if len(sys.argv) == 1:
    show()
    long = os.listdir(".")
    long = [int(x) for x in long if x.isnumeric()]
    long.sort()
    long = [str(x) for x in long]
    for nb in long:
        os.system(f"python main.py {nb}")
else:
    entree = sys.argv[1]
    if entree in ["full", "all"]:
        show()
        sys.exit(0)
    testnb = int(entree)
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