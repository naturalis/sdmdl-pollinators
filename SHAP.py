import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import shap
import os

root = "C:/Users/lotta/Desktop/sdmdl-master/SDMDL/sdmdl/data/results"

for occurrence in os.listdir("C:/Users/lotta/Desktop/sdmdl-master/SDMDL/sdmdl/data/occurrences"):
    filename = "/"+occurrence[:-4]+"/"+occurrence[:-4]+"_feature_impact"
    print(filename)

    shap_values = np.load(root + filename + ".npy")
    test_set = pd.read_csv(root + filename + ".csv")
    test_set = test_set.iloc[:,list(range(1,np.shape(test_set)[1]))]
    shap.summary_plot(shap_values[1], test_set, show=False)
    plt.savefig(root + filename, bbox_inches="tight")
    plt.close()