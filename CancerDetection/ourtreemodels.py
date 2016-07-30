# TODO:
# 1) review FOR loop changes (trying to only change data when moving to new data set
# instead of between changes in tree numbers)
#
# 2) output cross-validation sets with results (i.e., indexes, classes?)
#
# 3) remove "Unnamed: 0" indexing column from data # done
#
# 4) numcols in line 60 will probably be effected by 3)... recommend len(df.columns)-1 after fix # done
#
# 5) probably should just go ahead and add stuff we'll need for the bulk experiment format
# (etc.)

from objects.rforest import rforest
import pandas as pd
import numpy as np
from pprint import pprint as pp
import random
import datetime
from timeit import default_timer as timer

def split_df(df, partitions):

	#df['partiton'] = np.random.randint(partitions, size = len(df))
	R = random.sample(range(0, len(df)), len(df))
	df['partiton'] = np.array(list(i % partitions for i in R))

	# print(df['partiton'])
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
		print(fil)
		data = pd.read_csv("data/DNA/" + fil)

		split_data = split_df(data, folds)

		for df in split_data:
			df.drop('partiton', axis=1, inplace=True)

		
		numcols = len(df.columns) - 1
		nfeatures = int(np.floor(np.sqrt(numcols)))
   
		for treenum in treenumbers:
			rowdict = {}
			accuracy = []

			# start timing
			start = timer()
			for idx, df in enumerate(split_data):
				print("starting fold number", idx+1, 'of', len(split_data))
				# set up data to test on
				test_data = df.copy()
				# set up training data
				print("builing test/train sets")
				train_list = (split_data[:idx] + split_data[idx+1 :]).copy()
				train_data = pd.concat(train_list)

				# not sure what is going on here we really shouldnt be including this column but doing so kills the accuracy. some bug with the column list when predicting
				# train_data = train_data.iloc[:,1:]
				labelcol = train_data.columns.get_loc("Cancer")

				# bulid forrest
				print("buliding random forest")
				myforest = rforest(data = train_data, labelcol = labelcol)
				sampleforest = myforest.build_forest(data = train_data, ktrees = treenum, msamples = len(train_data), nfeatures = nfeatures)
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

			# finish timing
			end = timer()
			# print out accuracy results	
			print('accuracy vector',accuracy)
			print('average accuracy',np.mean(accuracy))
			
			# send data to a rowdict and throw it into a rowlist
			rowdict = list_to_dict(accuracy)
			rowdict['cancertype'] = names[idxf]
			rowdict['aveaccuracy'] = np.mean(accuracy)
			rowdict['ntrees'] = treenum
			rowdict['std'] = np.std(accuracy)
			rowdict['timestamp'] = datetime.datetime.now()
			rowdict['computationtime'] = (end-start)
			rowlist.append(rowdict)
			rowdict['maxsinglefold'] = max(accuracy)
			rowdict['minsinglefold'] = min(accuracy)

	# convert the rowlist into a dataframe and save it to a .csv
	performance_df = pd.DataFrame(rowlist)
	print(performance_df)
	performance_df.to_csv('data/results/' +str(folds) + 'folds' +str(datetime.datetime.now())+ 'perfomance.csv')
	return split_data







if __name__ == '__main__':

	files = ['labeled_leuk.csv','labeled_bladder.csv', 'labeled_liver.csv', 'labeled_prostate.csv', 'labeled_colon.csv']


	for idxf, fil in enumerate(files):
		# run each file
		print(fil)
		data = pd.read_csv("data/DNA/" + fil)
		print(pd.value_counts(data["Cancer"].values))
	# treenumbers = [1,2,5,10,20,60,100]
	# names = ['leuk','bladder', 'liver', 'prostate', 'colon']

	# for testing
	# files = ['labeled_prostate.csv', 'labeled_colon.csv']
	# names = ['prostate', 'colon']
	# treenumbers = [1,2,5]

	# # print(list_to_dict(treenumbers))

	# buildtestmodels(files, treenumbers, names,5)


