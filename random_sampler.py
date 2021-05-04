import os
import random

os.chdir("C:/Users/lotta/Desktop/Master_EB/Deep_Learning/CASE STUDY 3")
occurrences = os.listdir("C:/Users/lotta/Desktop/Master_EB/Deep_Learning/CASE STUDY 3")
counter = 0
first = True
for x in occurrences:
    if x.endswith(".csv") == True:
        print(x)
        file = open(x, "r")
        list = file.read().split("\n")
        number_of_occ = len(list)-2
        print(number_of_occ)
        counter = counter + number_of_occ
        file.close()
        if first == True:
            lowest = number_of_occ
            first = False
        if number_of_occ < lowest:
            lowest = number_of_occ
print("final occurrence count:",counter)
print("The lowest amount of occurrences is:", lowest)

for x in occurrences:
    if x.endswith(".csv") == True:
        print(x)
        file = open(x, "r")
        list = file.read().split("\n")
        file.close()
        location = "C:/Users/lotta/Desktop/Master_EB/Deep_Learning/CASE STUDY 3/random_sampled/"+x
        new = open(location, "w")
        new.write("decimalLatitude,decimalLongitude\n")
        for x in range(290):
            chosen_occurrence = list.pop(random.randint(1,(len(list)-1))) + "\n"
            new.write(chosen_occurrence)

        new.close()