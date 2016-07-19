import pandas as pd 
import numpy as np
from rforest import rforest
from pprint import pprint as pp

if __name__ == '__main__':
    np.random.seed(seed = 15)
    data_df = pd.read_csv('thousandtoy.csv')

    print("full toy data set")
    print(len(data_df))

    myforest = rforest(data = data_df, labelcol = 0)

    sampleforest = myforest.build_forest(data = data_df, ktrees = 1, msamples = len(data_df), nfeatures = 25)


    test_df = pd.read_csv("thousandtoytest.csv")
    unknown_df = test_df.iloc[:,1:]
    prediction = myforest.predict_df(unknown_df)

    test_pred_df = test_df
    test_pred_df['pred'] = prediction['pred']

    test_pred_df['correct'] = test_df.iloc[:,0] == test_pred_df["pred"]
    print('preditions on thousandtoytest')
    print(test_pred_df)


    correct_precentage = float(len(test_pred_df[test_pred_df['correct'] == True]))/len(test_pred_df)
    print("correct percentage of Rforest with traning data derived of the same way")
    print(correct_precentage)