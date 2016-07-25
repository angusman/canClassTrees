from objects.rforest import rforest
import pandas as pd
import numpy as np
from pprint import pprint as pp
import random

def split_df(df, partitions):

	df['partiton'] = np.random.randint(partitions, size = len(df))
	split_data = []
	for k in range(partitions):
		split_data.append(df[df['partiton'] == k])


	return split_data

def list_to_dict(liste):
	mydict = {}
	for idx, val in enumerate(liste):
		mydict['fold' + str(idx)] = val
	return mydict





def buildtestmodels(files, treenumbers, names, folds):
	# files: list of datafiles to be processed ['leuk_labeled', ... etc] assuming that data files are in the right folder
	# treenumbers, vector containing number of trees to run in RF forrest [5, 10, ...]
	# names, cancer name type associated with file

	rowlist = []
	for idxf, fil in enumerate(files):
		# run each file
		
		for treenum in treenumbers:
			rowdict = {}
			print(fil)
			data = pd.read_csv("data/DNA/" + fil)

			split_data = split_df(data, folds)

			for df in split_data:
				df.drop('partiton', axis=1, inplace=True)

			labelcol = data.columns.get_loc("Cancer")
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
				sampleforest = myforest.build_forest(data = train_data, ktrees = treenum, msamples = len(data), nfeatures = nfeatures)
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
				print("finishing fold number", idx + 1, 'of', len(split_data), 'accuracy = ', correct_precentage)

			# print out accuracy results	
			print('accuracy vector',accuracy)
			print('average accuracy',np.mean(accuracy))
			
			# send data to a rowdict and throw it into a rowlist
			rowdict = list_to_dict(accuracy)
			rowdict['cancertype'] = names[idxf]
			rowdict['aveaccuracy'] = np.mean(accuracy)
			rowdict['ntrees'] = treenum
			rowlist.append(rowdict)

	# convert the rowlist into a dataframe and save it to a .csv
	performance_df = pd.DataFrame(rowlist)
	performance_df.to_csv('data/results/' +str(folds) + 'folds' +str(random.randint(1000,2000))+ 'perfomance.csv')







if __name__ == '__main__':

	files = ['labeled_leuk.csv','labeled_bladder.csv', 'labeled_liver.csv', 'labeled_prostate.csv', 'labeled_colon.csv']
	treenumbers = [10,20,40,100, 200]
	names = ['leuk','bladder', 'liver', 'prostate', 'colon']

	# # print(list_to_dict(treenumbers))

	buildtestmodels(files, treenumbers, names,5)



