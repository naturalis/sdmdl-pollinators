import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import shap
import os


def shap_plot(occurrence_directory, root):

    """ Creates SHAP feature importance figures from SDMDL package outputs for
    each species.

    :param occurrence_directory: A string containing a pathway to the SDMDL
                                 occurrence data folder.
    :param root: A string containing a pathway to the SDMDL results folder
                 containing the SHAP evaluation figure to be plotted.
    :return: -
    """

    for occurrence in os.listdir(occurrence_directory):
        filename = "/"+occurrence[:-4]+"/"+occurrence[:-4]+"_feature_impact"
        print(filename)

        shap_values = np.load(root + filename + ".npy")
        test_set = pd.read_csv(root + filename + ".csv")
        test_set = test_set.iloc[:,list(range(1,np.shape(test_set)[1]))]
        shap.summary_plot(shap_values[1], test_set, show=False)
        plt.savefig(root + filename, bbox_inches="tight")
        plt.close()


def main():

    """ Asks user for a pathway to the SDMDL results directory and SDMDL
    occurrence data directory. Initiates the SHAP plotting.

    :return: -
    """

    root = input("Enter the pathway to the SDMDL results directory:\n")
    occurrence_directory = input("Enter the pathway to the occurrence data "
                                 "directory:\n")
    shap_plot(occurrence_directory, root)


main()
