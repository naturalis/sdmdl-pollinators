import os
import pandas as pd


def auc_table(results_folder, test_run, run_type, param_size, test_type, to_test):

    """ Opens the SDMDL DNN performance evaluation files to extract AUC values
    for a specific tested batch or epoch size for each species used. All AUC
    values corresponding to the parameter tests are placed into a Pandas
    dataframe and written into a new csv file.

    :param results_folder: A string containing the pathway to the folder
                           containing all SDMDL result folders.
    :param test_run: A list of all the results in the folder
    :param run_type: An integer containing the list element to filter the
                     correct parameter size from test run names.
    :param param_size: A string containing the specific parameter value to
                       compare the AUCs for.
    :return: -
    """

    first = True
    data = {}
    to_write = []
    species_list = []
    for run in test_run:
        parameter = run.split("_")[run_type]
        to_test_run = run.split("_")[test_type]
        if parameter == param_size:
            to_write = []
            eval = open(results_folder + "/" + run + "/_DNN_performance/DNN_eval.txt", "r")
            auc = eval.readlines()
            if first == True:
                first = False
                for species in auc[1:]:
                    species_list.append(species.split('\t')[0])
                data = {"Species":species_list}
                df = pd.DataFrame(data)
            for species in auc[1:]:
                to_write.append(species.split('\t')[4])
            df[to_test_run[1:]] = to_write
    print(df)
    df.to_csv("AUC_eval_" + to_test + ".csv", index=False)



def transpose_table(to_test):

    """ Transposes the previously created .csv file to have species as columns
    and the parameter values as rows.

    :param to_test: A string containing the type of parameter to be tested.
    :return: -
    """

    newdata = pd.read_csv("AUC_eval_" + to_test + ".csv")

    df_t = newdata.transpose()
    print(df_t)

    df_t.to_csv("transposed_AUC_eval_" + to_test + ".csv", header=False)


def main():

    """ Asks user to enter pathway to the directory containing the SDMDL result
    folders. The parameter (epoch or batch size) to be compared must be given
    by used, accompanied with the steady batch size (if epochs are compared) or
    epoch size (if batch sizes are compared). Initiates comparison .csv file
    creation and transposing.
    WARNING: in order for this script to work separate SDMDL folders are to be
    named as followed: results_b<enter batch size>_e<enter epoch size>
    Besides, all the complete SDMDL results folder must be placed in given
    directory.

    :return: -
    """

    try:
        results_folder = input("Enter the pathway ot the directory containing the"
                            " SDMDL results folders:\n")
        os.chdir(results_folder)
        test_run = os.listdir(results_folder)
        to_test = input("Do you want to test batch or epoch size?\n")
        param_size = input("What parameter and size do you want to filter the "
                           "AUC s for? \nIf you want to test epoch sizes, "
                           "you enter the batch size and vice versa. \n"
                           "(eg testing epochs with a batch size of "
                           "32 'b32', or testing batch sizes with an epoch"
                           "size of 150 'e150')\n")
    except:
        pass

    if "epoch" == to_test.lower() and "b" in param_size:
        run_type = 1
        test_type = 2
        auc_table(results_folder, test_run, run_type, param_size, test_type, to_test)
        transpose_table(to_test)
    elif "batch" in to_test.lower() and "e" in param_size:
        run_type = 2
        test_type = 1
        auc_table(results_folder, test_run, run_type, param_size, test_type, to_test)
        transpose_table(to_test)
    else:
        print("No results of this type were found in this location...")


main()
