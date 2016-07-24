from objects.rforest import rforest
import pandas as pd
import numpy as np
from pprint import pprint as pp

def split_data(df, partitions):

	df['partiton'] = np.random.randint(partitions, size = len(df))
	split_data = []
	for k in range(partitions):
		split_data.append(df[df['partiton'] == k])


	return split_data





if __name__ == '__main__':
	leuk = pd.read_csv("data/DNA/labeled_leuk.csv")

	split_data = split_data(leuk, 5)
	
	for df in split_data:
		df.drop('partiton', axis=1, inplace=True)

	labelcol = leuk.columns.get_loc("Cancer")
	accuracy = []
	numcols = len(df.columns)
	nfeatures = int(np.floor(np.sqrt(numcols)))

	for idx, df in enumerate(split_data):
		print("starting fold number", idx+1, 'of', len(split_data))
		# set up data to test on
		test_data = df.copy()
		# set up training data
		print("builing test/train sets")
		train_list = (split_data[:idx] + split_data[idx+1 :]).copy()
		train_data = pd.concat(train_list)

		# bulid forrest
		print("buliding random forest")
		myforest = rforest(data = train_data, labelcol = labelcol)
		sampleforest = myforest.build_forest(data = train_data, ktrees = 20, msamples = len(leuk), nfeatures = nfeatures)
		# predict on test data
		# print(sampleforest)
		print("getting test data ready for predicting")
		unknown_df = test_data.iloc[:,1:]
		prediction = myforest.predict_df(unknown_df)

		# calculate correct percentrage
		test_pred_df = test_data
		test_pred_df['pred'] = prediction['pred']

		test_pred_df['correct'] = test_data.iloc[:,labelcol] == test_pred_df["pred"]
		correct_precentage = float(len(test_pred_df[test_pred_df['correct'] == True]))/len(test_pred_df)
		accuracy.append(correct_precentage)
		print("finishing fold number", idx, 'of', len(split_data), 'accuracy = ', correct_precentage)

	# print out accuracy results
	print('accuracy vector',accuracy)
	print('average accuracy',np.mean(accuracy))



