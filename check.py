a = []
essay = []
with open("working.csv", "r") as f:
    a = f.readlines()
    a = [x.rstrip("\n") for x in a]
with open("essay.txt", "r") as f:
    essay = f.readlines()
    essay = [x.split("\t")[0] for x in essay]
a = [x+(",1\n" if x.split(",")[0] in essay else ",0\n") for x in a]
with open("working.csv", "w") as f:
    f.writelines(a)
