import pandas as pd 
from rforest import rforest
from pprint import pprint as pp

if __name__ == '__main__':
    data_df = pd.read_csv('toydataset2.csv')

    print("full toy data set")
    print(len(data_df))

    myforest = rforest(data = data_df, labelcol = 0)

    sampleforest = myforest.build_forest(data = data_df, ktrees = 3, msamples = len(data_df), nfeatures = 2)

    print("passed sampleforest")

    test_df = pd.read_csv("testingtoyset2.csv")
    unknown_df = test_df.iloc[:,1:]
    prediction = myforest.predict_df(unknown_df)

    test_pred_df = test_df
    test_pred_df['pred'] = prediction['pred']

    test_pred_df['correct'] = test_pred_df['pred'] == test_pred_df['label']
    print('preditions and labels of toydataset2')
    print(test_pred_df)


    correct_precentage = float(len(test_pred_df[test_pred_df['correct'] == True]))/len(test_pred_df)
    print("correct percentage of Dtree with traning data derived of the same way")
    print(correct_precentage)