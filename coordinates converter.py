from pyproj import Proj, transform
import os

os.chdir('C:\\Users\\lotta\\Desktop\\Master_EB\\Deep_Learning\\Plant occurrences')
inProj = Proj('epsg:28992')
outProj = Proj('epsg:4326')
location = 'C:\\Users\\lotta\\Desktop\\Master_EB\\Deep_Learning\\Plant occurrences'

files = os.listdir(location)


for occurrence in files:
    if "new" not in occurrence:
        with open(occurrence) as occ:
            print("currently converting: ", occurrence)
            new_file = "C:/Users/lotta/Desktop/sdmdl-master/SDMDL/sdmdl/data/occurrences/"+occurrence
            new_csv = open(new_file, 'w')
            new_line = ["decimalLatitude", "decimalLongitude\n"]
            new_csv.write(','.join(new_line))
            for lines in occ:
                line = occ.readline()
                #print(line)
                if "X" not in line and 'x' not in line:
                    coords = line.split(',')
                    #print("Old coordinates:", coords)
                    try:
                        x1,y1 = int(coords[0]), int(coords[1])
                        x2,y2 = transform(inProj,outProj,x1,y1)
                        new_line = [str(x2), str(y2)+"\n"]
                        #print ('New coordinates:', x2, y2)
                        new_csv.write(','.join(new_line))
                    except:
                        pass
