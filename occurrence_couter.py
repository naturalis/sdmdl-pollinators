import os

os.chdir("C:/Users/lotta/Desktop/sdmdl-master/SDMDL/sdmdl/data/occurrences")
occurrences = os.listdir("C:/Users/lotta/Desktop/sdmdl-master/SDMDL/sdmdl/data/occurrences")
counter = 0
for x in occurrences:
    if x != "README.md":
        print(x)
        file = open(x, "r")
        list = file.read().split("\n")
        print(len(list)-2)
        counter = counter + len(list) - 2
        file.close()
print("final occurrence count:",counter)