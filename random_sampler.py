import os
import random


def count_occurrences(occurrences):

    """ Loops through all occurrence data files to find the lowest number of
    occurrences across all files. Prints the number of occurrences for each
    species, the total, and lowest number.

    :param occurrences: A list containing the pathways to all occurrence data
                        files.
    :return: lowest : An integer containing the lowest number of occurrences
                      found
    """

    counter = 0
    first = True
    for x in occurrences:
        if x.endswith(".csv"):
            print(x)
            file = open(x, "r")
            list = file.read().split("\n")
            number_of_occ = len(list)-2
            print(number_of_occ)
            counter = counter + number_of_occ
            file.close()
            if first:
                lowest = number_of_occ
                first = False
            if number_of_occ < lowest:
                lowest = number_of_occ
    print("Final occurrence count:", counter)
    print("The lowest number of occurrences is:", lowest)
    return lowest


def random_sample(occurrences, lowest, occurrences_directory):

    """ Randomly samples from all occurrence data files till all files
    contain the same number of occurrences, which is the lowest number of
    occurrences found among all occurrence data files. The random sample number
    can be changed to a desired number in the nested for loop.
    Writes sampled occurrence data points to a new .csv file in a folder called
    random_sampled.

    :param occurrences: A list containing the pathways to all occurrence data
                        files.
    :param lowest: An integer containing the lowest number of occurrences
                   found.
    :param occurrences_directory: A string containing the pathway to the
                                  occurrence data directory.
    :return: -
    """

    for x in occurrences:
        if x.endswith(".csv"):
            file = open(x, "r")
            list = file.read().split("\n")
            file.close()
            try:
                os.mkdir("random_sampled")
            except:
                pass
            location = occurrences_directory + "/random_sampled/" + x
            new = open(location, "w")
            new.write("decimalLatitude,decimalLongitude\n")
            for x in range(lowest):
                chosen_occurrence = list.pop(random.randint(1, (len(list)-1))) \
                                    + "\n"
                new.write(chosen_occurrence)

            new.close()


def main():

    """ Asks user for pathway to the directory containing occurrence data to
    be sampled. Initiates data point counting and random sampling.

    :return: -
    """

    occurrences_directory = input("Enter the pathway to the directory "
                                  "containing the occurrence data to be "
                                  "randomly sampled:\n")
    print("Random sampling will occur according to the lowest number of"
          "occurrences.")
    os.chdir(occurrences_directory)
    occurrences = os.listdir(occurrences_directory)
    lowest = count_occurrences(occurrences)
    random_sample(occurrences, lowest, occurrences_directory)


main()
