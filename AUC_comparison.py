import os
import pandas as pd

os.chdir("C:/Users/lotta/Desktop/Master_EB/Deep_Learning/CASE STUDY 1/results")
occurrences = os.listdir("C:/Users/lotta/Desktop/Master_EB/Deep_Learning/CASE STUDY 1/results")
first = True
data = {}
to_write = []
species_list = []
for run in occurrences:
    run_epoch = run.split("_")[3]
    run_batch = run.split("_")[2]
    if run_batch == "b75":
        to_write = []
        eval = open("C:/Users/lotta/Desktop/Master_EB/Deep_Learning/CASE STUDY 1/results/"+run+"/_DNN_performance/DNN_eval.txt", "r")
        auc = eval.readlines()
        if first == True:
            first = False
            for species in auc[1:]:
                species_list.append(species.split('\t')[0])
            data = {"Species":species_list}
            df = pd.DataFrame(data)
        for species in auc[1:]:
            to_write.append(species.split('\t')[4])
        df[run_epoch[1:]] = to_write
print(df)
df.to_csv("C:/Users/lotta/Desktop/Master_EB/Deep_Learning/CASE STUDY 1/auc_eval.csv", index=False)

newdata = pd.read_csv("C:/Users/lotta/Desktop/Master_EB/Deep_Learning/CASE STUDY 1/auc_eval.csv")

df_t = newdata.transpose()
print(df_t)
df_t.to_csv("C:/Users/lotta/Desktop/Master_EB/Deep_Learning/CASE STUDY 1/auc_eval.csv", header=False)