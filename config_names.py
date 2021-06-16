import os


def names(location, occurrence_files):

    """Loops through the occurrence files and prints the species names and
    pathways to the occurrence data in a format used in the SDMDL config.yml.
    Species names and pathways are also written in a file called occurrence.txt.

    :param location: A string containing the pathway to the occurrence data
                     directory.
    :param occurrence_files: A list containing pathways to the files of
                             the given directory.
    :return: -
    """

    occurrences = open(location+ "/occurrences.txt", "w")
    for x in occurrence_files:
        if x != "README.md":
            x = x.replace(" ", "_")
            text = "  "+ x[:-4] + ": " + location + "/" + x + "\n"
            occurrences.write(text)
            print("  "+ x[:-4] + ": " + location + "/" + x)
    occurrences.close()


def main():

    """ Asks user for pathway to the directory containing the occurrence data
    files. Initiates name formatting.

    :return: -
    """

    location = input("Enter the pathway to the directory for your occurrence "
                     "data:\n")
    occurrence_files = os.listdir(location)
    names(location, occurrence_files)


main()
