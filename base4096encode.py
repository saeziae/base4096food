from cgitb import reset
import random
import sys
from unittest import result
TABLE = ""
with open("list.txt", "r") as a:
    TABLE = a.readlines()
    TABLE = [x.rstrip("\n") for x in TABLE]
RESULT = []
with open(sys.argv[1], "rb") as a:
    f = a.read().hex()
    x = False
    if len(f) % 3:
        f += "00"
        x = True
    for i in range(0, len(f), 3):
        RESULT.append(TABLE[int(f[i:i+3], 16)])
    if x:
        RESULT.append("好吃")
with open(sys.argv[1]+".yummy", "w") as a:
    for i in range(len(RESULT)):
        a.write(RESULT[i])
        a.write("  "*(7-len(RESULT[i])))
        if not (i+1) % 8:
            a.write("\n")