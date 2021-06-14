import os


def filter(custom_file, species_list, AX, AY, AS):

    """Filters given plants or bees from an NDFF or bee database respectively.
    Coordinates for each species are filtered and written to species specific
    text-files. Only works with database text-files from NDFF or EIS!

    :param custom_file: A string containing a pathway to the Database file
                        to be filtered
    :param species_list: A list of species names to be filtered from the
                         database
    :param AX: An integer containing the location of the AX coordinates in the
               database file
    :param AY: An integer containing the location of the AY coordinates in the
               database file
    :param AS: An integer containing the location of the species name in the
               database file
    :return: -
    """

    with open(custom_file, "r") as all_data:
        for lines in all_data:
            line = all_data.readline().split(",")
            try:
                species = line[AS].strip("\"")
                if species in species_list:
                    if os.path.exists(species.replace(" ", "_")+".csv") == True:
                        file = open(species.replace(" ", "_")+".csv", "a")
                        line_write = line[AX]+","+line[AY]+"\n"
                        file.write(line_write)
                        file.close()
                    elif os.path.exists(species.replace(" ", "_")+".csv") == False:
                        file = open(species.replace(" ", "_")+".csv", "w")
                        line_write = "AX,AY\n"+line[AX]+","+line[AY]+"\n"
                        file.write(line_write)
                        file.close()
            except:
                pass


def main():

    """Requests database file, file destination, and file including species
    names that are to be filtered from the database. Creates lists including
    the desired species names. Adjusts column numbers for species name and
    coordinates to either NDFF or EIS format. Initiates filtering.
    Only works with database text-files from NDFF or EIS!

    :return: -
    """

    custom_file = input("Enter the pathway to the NDFF/EIS database file:\n")
    destination_directory = input("Choose the desired destination for the new "
                                  "files:\n")
    os.chdir(destination_directory)
    soi_input = input("Enter the pathway to the file including the species"
                      " desired to be filtered from the database:\n")
    species_of_interest = open(soi_input, "r")
    species_of_interest_file = species_of_interest.readlines()
    species_list = []

    if "NDFF" in custom_file:
        for x in range(len(species_of_interest_file)):
            species_list.append(species_of_interest_file[x].rstrip("\n").split(";")[5])
        AS = 1
        AX = 2
        AY = 3
    elif "allbees" in custom_file:
        for x in range(len(species_of_interest_file)):
            species_list.append(species_of_interest_file[x].rstrip("\n"))
        AS = 3
        AX = 5
        AY = 6
    filter(custom_file, species_list, AX, AY, AS)


main()
