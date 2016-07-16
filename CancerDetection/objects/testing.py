import pandas as pd 
from dtree import dtree
from pprint import pprint as pp

if __name__ == '__main__':
	data_df = pd.read_csv('thousandtoy.csv')

	print("full toy data set")
	print(len(data_df))

	mytree = dtree(data = data_df, labelcol = 0)

	sampletree = mytree.bulid_tree(data = data_df, min_entropy = .1 ,tree_dict = {})

	pp(sampletree)

	test_df = pd.read_csv("thousandtoytest.csv")
	unknown_df = test_df.iloc[:,1:]
	prediction = mytree.predict_df(unknown_df)

	test_pred_df = test_df
	test_pred_df['pred'] = prediction['pred']


	test_pred_df['correct'] = test_pred_df.iloc[:,0] == test_pred_df.iloc[:,0]
	print('preditions on thousandtoytest')
	print(test_pred_df)


	correct_precentage = float(len(test_pred_df[test_pred_df['correct'] == True]))/len(test_pred_df)
	print("correct percentage of Dtree with traning data derived of the same way")
	print(correct_precentage)



