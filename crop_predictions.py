def crop(netherlands_locations, world_locations, xmin, xmax, ymin, ymax):

    """ Reads world_locations_to_predict.csv, and scans for coordinates that are
    withing the range of the Netherlands. These coordinates are written to a
    new file.

    :param netherlands_locations: A csv-file, to where the cropped
                                  coordinates extent is written
    :param world_locations: A csv-file from SDMDL, containing the prediction
                            coordinates of the world
    :param xmin: A float containing the minimum x coordinate of the Netherlands
    :param xmax: A float containing the maximum x coordinate of the Netherlands
    :param ymin: A float containing the minimum y coordinate of the Netherlands
    :param ymax: A float containing the maximum y coordinate of the Netherlands
    :return: -
    """

    tag = 0

    for lines in world_locations.readlines():
        line = lines.rstrip('\n').split(',')
        try:
            if "decimal_longitude" not in line:
                if float(line[1]) < xmax and float(line[1]) > xmin and\
                        float(line[2]) < ymax and float(line[2]) > ymin:
                    line = str(tag) + "," + str(line[1]) + "," + str(line[2])\
                           + "\n"
                    netherlands_locations.write(line)
                    tag += 1
            else:
                print(line)
                netherlands_locations.write(lines)
        except ValueError:
            netherlands_locations.write(',decimal_longitude,decimal_latitude\n')


def main():

    """ Defines border coordinates of the Netherlands. Asks user to enter
    pathway to world_locations_to_predict.csv, and a destination for the newly
    cropped coordinate file. Initiates the cropping.

    :return: -
    """

    xmin = 3.245713
    xmax = 7.256333
    ymin = 50.72637
    ymax = 53.53395
    world_file = input("Enter the pathway to the world_locations_to_"
                            "predict file:\n")
    netherlands_file = input("Enter desired pathway location to write"
                                  "the cropped file:\n")
    world_locations = open(world_file, "r")
    netherlands_locations = open(netherlands_file, "w")

    crop(netherlands_locations, world_locations, xmin, xmax, ymin, ymax)


main()
