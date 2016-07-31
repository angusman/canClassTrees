import pandas as pd 
import numpy as np
import random
import time as time
from rforest import rforest
from pprint import pprint as pp

if __name__ == '__main__':
    random.seed(87)             # seed for dtree samples
    np.random.seed(seed = 15)   # seed for rforest samples
    data_df = pd.read_csv('thousandtoy.csv') # !! This is being read incorrectly! Use no header!

    print("full toy data set")
    print(len(data_df))

    myforest = rforest(data = data_df, labelcol = 0)

    sampleforest = myforest.build_forest(data = data_df, ktrees = 20, msamples = len(data_df), nfeatures = "bagging")
    
    start2 = time.process_time()
    test_df = pd.read_csv("thousandtoytest.csv")
    unknown_df = test_df.iloc[:,1:]
    prediction = myforest.predict_df(unknown_df)
    end2 = time.process_time() - start2

    test_pred_df = test_df
    test_pred_df['pred'] = prediction['pred']

    test_pred_df['correct'] = test_df.iloc[:,0] == test_pred_df["pred"]
    print('preditions on thousandtoytest')
    print(test_pred_df)
  


    correct_precentage = float(len(test_pred_df[test_pred_df['correct'] == True]))/len(test_pred_df)
    print("correct percentage of Rforest")
    print(correct_precentage)
        
    print()
    print("prediction CPU time")
    print(end2)