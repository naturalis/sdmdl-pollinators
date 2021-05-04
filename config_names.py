import os

location = "/Users/lotta/Desktop/sdmdl-master/SDMDL/sdmdl/data/occurrences/"
occurrence_files = os.listdir("/Users/lotta/Desktop/sdmdl-master/SDMDL/sdmdl/data/occurrences/")

occurrences = open("/Users/lotta/Desktop/sdmdl-master/occurrence/occurrences.txt", "w")
for x in occurrence_files:
    if x != "README.md":
        x = x.replace(" ", "_")
        text = "  "+ x[:-4] + ": /Users/lotta/Desktop/sdmdl-master/SDMDL/sdmdl/data/occurrences/"+x+"\n"
        occurrences.write(text)
        print("  "+ x[:-4] + ": /Users/lotta/Desktop/sdmdl-master/SDMDL/sdmdl/data/occurrences/"+x)
occurrences.close()
