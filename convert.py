import os

location = "C:\\Users\\lotta\\Desktop\\Master_EB\\Deep_Learning\\env_variables-20210309T162741Z-001\\env_variables"
os.chdir(location)
for src_asc in os.listdir(location):
    if ".asc" in src_asc:
        dest_gtif = src_asc[:-4] + '.gtiff'
        command = "gdal_translate -of GTiff -ot Float32 " + location +'\\' +  src_asc + ' ' + location +'\\' + dest_gtif
        os.system(command)

for src_gtiff in os.listdir(location):
    if ".gtiff" in src_gtiff:
        dest_tif = src_gtiff[:-6] + '.tiff'
        command = "gdal_translate -co profile=baseline " + src_gtiff + ' ' + dest_tif
        os.system(command)