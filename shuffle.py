from random import shuffle
a=[]
with open("working.csv","r") as f:
    a=f.readlines()
shuffle(a)
with open("working.csv","w") as f:
    f.writelines(a)