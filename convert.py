import os


def gtiff(location):

    """ Converts ASCII raster files into GTIFF files in given directory

    :param location: A string containing the pathway to the directory containing
                     the files to be converted
    :return: -
    """

    for src_asc in os.listdir(location):
        if ".asc" in src_asc:
            dest_gtif = src_asc[:-4] + '.gtiff'
            command = "gdal_translate -of GTiff -ot Float32 " + location +'\\' \
                      +  src_asc + ' ' + location +'\\' + dest_gtif
            os.system(command)


def tiff(location):

    """ Converts GTIFF files into TIFF files in given directory

    :param location: A string containing the pathway to the directory containing
                     the files to be converted
    :return: -
    """

    for src_gtiff in os.listdir(location):
        if ".gtiff" in src_gtiff:
            dest_tif = src_gtiff[:-6] + '.tiff'
            command = "gdal_translate -co profile=baseline " + src_gtiff + ' ' \
                      + dest_tif
            os.system(command)


def main():

    """ Asks user for directory containing the files to be converted.
    Initiates the conversion from ASC to GTIFF, and from GTIFF to TIFF.

    :return:
    """

    location = input("Enter the pathway to the directory containing the files"
                     "to be converted:\n")
    os.chdir(location)
    gtiff(location)
    tiff(location)


main()
