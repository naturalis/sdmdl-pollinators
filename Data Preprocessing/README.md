# Data pre-processing
This folder contains Python scripts used for the pre-processing of data 
during the case studies, where the effect of the addition of biotic interactions
were studied.


* [convert.py](https://github.com/naturalis/sdmdl-pollinators/blob/main/Data%20Preprocessing/convert.py) - Converts GIS ASCII raster layers to GTIFF, and then to TIFF
* [coordinates_converter.py](https://github.com/naturalis/sdmdl-pollinators/blob/main/Data%20Preprocessing/coordinates%20converter.py) - Converts occurrence data coordinates from EPSG:28992 to EPSG: 4326
* [crop_predictions.py](https://github.com/naturalis/sdmdl-pollinators/blob/main/Data%20Preprocessing/crop_predictions.py) - Crops the world_locations_to_predict.csv file to the extent of the Netherlands
* [occurrence_counter.py](https://github.com/naturalis/sdmdl-pollinators/blob/main/Data%20Preprocessing/occurrence_counter.py) - Counts the number of occurrences in each dataset
* [oligolectic_bees.py](https://github.com/naturalis/sdmdl-pollinators/blob/main/Data%20Preprocessing/oligolectic_bees.py) - Filters oligolectic bees and their host plants from NDFF and EIS database files
* [random_sampler.py](https://github.com/naturalis/sdmdl-pollinators/blob/main/Data%20Preprocessing/random_sampler.py) - Randomly samples the datasets to contain the same number of data points