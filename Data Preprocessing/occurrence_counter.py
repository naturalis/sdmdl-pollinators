import os


def count(occurrences):

    """Loops through the given occurrence directory and counts the number of
    occurrences per species. Prints the results per species and the total
    number of occurrences.

    :param occurrences: List of occurrence files to be counted
    :return: -
    """

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


def main():

    """Asks user for pathway to the occurrence directory.
    Initiates the counting.

    :return: -
    """
    root = input("Enter the pathway to your occurrence directory:\n")
    os.chdir(root)
    occurrences = os.listdir(root)
    count(occurrences)


main()
