# Result interpretation
This folder contains the Python script used to interpret the SDMDL outputs, 
mainly by looking at the model fit of different parameters by looking at 
the AUC values for the test runs per species.

* [AUC_comparison.py](https://github.com/naturalis/sdmdl-pollinators/blob/main/Result%20Interpretation/AUC_comparison.py) - Filters the AUC values for all given runs for each species from the SDMDL DNN evaluation file, and writes these to a new .csv file