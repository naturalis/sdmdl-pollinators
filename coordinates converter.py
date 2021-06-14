from pyproj import Proj, transform
import os


def convert(files, inProj, outProj):

    """Converts all coordinates of given occurrence files from epsg:28992 to
    epsg:4326, and writes all converted occurrences into new files.

    :param files: A list of occurrence data files to be converted
    :param inProj: Coordinate system to be converted from
    :param outProj: Coordinate system to be converted to
    :return: -
    """

    for occurrence in files:
        if "new" not in occurrence:
            with open(occurrence) as occ:
                print("currently converting: ", occurrence)
                new_file = "/wgs84_occurrences/"+occurrence
                new_csv = open(new_file, 'w')
                new_line = ["decimalLatitude", "decimalLongitude\n"]
                new_csv.write(','.join(new_line))
                for lines in occ:
                    line = occ.readline()
                    if "X" not in line and 'x' not in line:
                        coords = line.split(',')
                        try:
                            x1,y1 = int(coords[0]), int(coords[1])
                            x2,y2 = transform(inProj,outProj,x1,y1)
                            new_line = [str(x2), str(y2)+"\n"]
                            new_csv.write(','.join(new_line))
                        except:
                            pass


def main():

    """Asks user to enter pathway to data, declares coordinate systems, and
    creates new directory for converted data. Initiates conversion.

    :return: -
    """

    root = input("Please enter the pathway to the occurrence data directory:\n")
    os.chdir(root)
    inProj = Proj('epsg:28992')
    outProj = Proj('epsg:4326')
    files = os.listdir(root)
    try:
        os.mkdir(root+"/wgs84_occurrences")
    except:
        pass
    convert(files, inProj, outProj)

main()
