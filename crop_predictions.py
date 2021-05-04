"""
class      : Extent
xmin       : 3.245713
xmax       : 7.256333
ymin       : 50.72637
ymax       : 53.53395
"""

netherlands_locations = open("C:/Users/lotta/Desktop/sdmdl-master/SDMDL/sdmdl/data/gis/world_locations_to_predict2.csv", "w")
xmin = 3.245713
xmax = 7.256333
ymin = 50.72637
ymax = 53.53395
tag = 0
"""
with open("C:/Users/lotta/Desktop/sdmdl-master/SDMDL/sdmdl/data/gis/world_locations_to_predict.csv") as wlp:
    netherlands_locations.write(',decimal_longitude,decimal_latitude\n')
    for lines in wlp:
        print(lines)
        line = wlp.readline().rstrip('\n').split(',')
        if "decimal_longitude" not in line:
            if float(line[1]) < xmax and float(line[1]) > xmin and float(line[2]) < ymax and float(line[2]) > ymin:
                    line = str(tag) + "," + str(line[1]) + "," + str(line[2]) + "\n"
                    netherlands_locations.write(line)
                    tag += 1
        else:
            print(line)
            netherlands_locations.write(line)

netherlands_locations.close()
"""
world_locations = open("C:/Users/lotta/Desktop/sdmdl-master/CLTP/current/NL_locations_to_predict_500.csv", "r")

for lines in world_locations.readlines():
    line = lines.rstrip('\n').split(',')
    try:
        if "decimal_longitude" not in line:
            if float(line[1]) < xmax and float(line[1]) > xmin and float(line[2]) < ymax and float(line[2]) > ymin:
                line = str(tag) + "," + str(line[1]) + "," + str(line[2]) + "\n"
                netherlands_locations.write(line)
                tag += 1
        else:
            print(line)
            netherlands_locations.write(lines)
    except ValueError:
        netherlands_locations.write(',decimal_longitude,decimal_latitude\n')