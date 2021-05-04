import os
"""
os.chdir("C:/Users/lotta/Desktop/Master_EB/Deep_Learning/Bee occurrences test")
oligolectic_bees_file = open("C:/Users/lotta/Desktop/sdmdl-master/Bees/oligolectic_bees.txt", "r")
oligolectic_bees = oligolectic_bees_file.readlines()
oligo_bees = []
for x in range(len(oligolectic_bees)):
    oligo_bees.append(oligolectic_bees[x].rstrip("\n"))
with open("C:/Users/lotta/Desktop/sdmdl-master/Bees/allbees_2004_noNA_noduplicates.csv", "r") as all_bees:
    for lines in all_bees:
        line = all_bees.readline().split(",")
        try:
            species = line[3].strip("\"")
            if species in oligo_bees:
                if os.path.exists(species.replace(" ", "_")+".csv") == True:
                    file = open(species.replace(" ", "_")+".csv", "a")
                    line_write = line[5]+","+line[6]+"\n"
                    file.write(line_write)
                    file.close()
                elif os.path.exists(species.replace(" ", "_")+".csv") == False:
                    file = open(species.replace(" ", "_")+".csv", "w")
                    line_write = "AX,AY\n"+line[5]+","+line[6]+"\n"
                    file.write(line_write)
                    file.close()
        except:
            pass
"""

os.chdir("C:/Users/lotta/Desktop/Master_EB/Deep_Learning/Plant occurrences")
hostplant_file = open("C:/Users/lotta/Desktop/sdmdl-master/Bees/hostpl_less.csv", "r")
hostplants = hostplant_file.readlines()
hostplant = []
for x in range(len(hostplants)):
    hostplant.append(hostplants[x].rstrip("\n").split(";")[5])

with open("C:/Users/lotta/Desktop/sdmdl-master/Bees/NDFFcompletedata_lessvar.csv", "r") as all_plants:
    for lines in all_plants:
        line = all_plants.readline().split(",")
        try:
            species = line[1].strip("\"")
            if species in hostplant:
                if os.path.exists(species.replace(" ", "_")+".csv") == True:
                    file = open(species.replace(" ", "_")+".csv", "a")
                    line_write = line[2]+","+line[3]+"\n"
                    file.write(line_write)
                    file.close()
                elif os.path.exists(species.replace(" ", "_")+".csv") == False:
                    file = open(species.replace(" ", "_")+".csv", "w")
                    line_write = "AX,AY\n"+line[2]+","+line[3]+"\n"
                    file.write(line_write)
                    file.close()
        except:
            pass
