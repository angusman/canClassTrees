# Math 502B classification project
# Nicholas Sullivan
import pandas as pd
import numpy as np
from sklearn import tree
from numpy import genfromtxt
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import BaggingClassifier
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.cross_validation import StratifiedKFold
from sklearn.cross_validation import KFold
from timeit import default_timer as timer
import datetime
from pprint import pprint as pp
from sklearn import tree

def load_data(fil):
	# given a filepath split the data into observations and labels
	# returns thouse observations and labels
	data = pd.read_csv("data/DNA/" + fil)

	labels = np.array(data['Cancer'])

	# remove Cancer and that weird unnamed: 0 columns
	data.drop('Cancer', axis=1, inplace=True)
	data.drop('Unnamed: 0', axis=1, inplace=True)
	observations = np.array(data)


	return observations, labels

def datalen(fil):
	# given a file math return the length of data set
	data = pd.read_csv("data/DNA/" + fil)
	return data.shape[0]






def dowork(filelist, names, clflist, clfnames,nfolds,treenum, kstrat = False, Kindexerlist = None):

	rowlist = []

	for idxf, fil in enumerate(filelist):

		# load data from file
		X, Y = load_data(fil)

		# calculate its length for using kfolds
		datalength = len(X)

		
		# using Stratified Kfolds?
		if Kindexerlist == None:
			if kstrat:
				kf = StratifiedKFold(Y, n_folds = nfolds)
			else:
				kf = KFold(datalength, n_folds=nfolds)	
		else:
			print("Using Preset Kfolds index")
			kf = Kindexerlist[idxf]


		# Stratified KFolds
		# 

		for idx, clf in enumerate(clflist):
			rowdict = {}
			acclist = []

			# counter for keeping track of fold numbers
			k = 0
			# timer for tracking computation time
			start = timer()
			for train_index, test_index in kf:
				# if you want to be kept in the loop
				# print("starting fold number ",k+1, "of", nfolds)

				# split data using kfolds indexes
				X_train, X_test = X[train_index], X[test_index]
				Y_train, Y_test = Y[train_index], Y[test_index]

				# fit predict and score the train/test data
				clf.fit(X_train,Y_train)
				Y_pred = clf.predict(X_test)
				accuracy = accuracy_score(Y_test,Y_pred)

				# print off accuracy

				# keep track of fold accuracy
				acclist.append(accuracy)

				# iterate k
				k = k+1

			end = timer()
			
			# after all folds of a dataset/classifier are done record stats for analysis
			rowdict['cancertype'] = names[idxf]
			rowdict['aveaccuracy'] = np.mean(acclist)
			rowdict['ntrees'] = treenum
			rowdict['std'] = np.std(acclist)
			rowdict['timestamp'] = datetime.datetime.now()
			rowdict['computationtime'] = (end-start)
			rowdict['maxsinglefold'] = max(acclist)
			rowdict['minsinglefold'] = min(acclist)
			rowdict['method'] = clfnames[idx]
			rowdict['kfolds'] = nfolds
			rowdict['kstrat'] = kstrat
			rowdict['median'] = np.median(acclist)
			rowdict['lenfolds'] = len(acclist)

			# add this rowdict to the list of rows

			rowlist.append(rowdict)


	data_df = pd.DataFrame(rowlist)
	
	# data_df.drop_duplicates(inplace = true)

	return data_df







if __name__ == '__main__':


	"""
	Case Study 1: RandomForest and AdaBoost Varing Tree numbers Standard Parameters
	Changing parameter: trees = [1,2,5,10,20,60,100]
	Other parameters: Kstrat = False
	Data: All Data sets
	Kfolds = 10
	"""
	print("Study1")
	trees = [1,2,5,10,20,60,100]
	data_df = pd.DataFrame()
	filelist = ['labeled_leuk.csv','labeled_bladder.csv', 'labeled_liver.csv', 'labeled_prostate.csv', 'labeled_colon.csv']
	names = ['leuk','bladder', 'liver', 'prostate', 'colon']
	clfnames = ["RandomForestClassifier", "AdaBoostClassifier", "DecisionTreeClassifier"]
	Kindexlist = []
	for fil in filelist:
		X, Y = load_data(fil)
		Kindex = StratifiedKFold(Y, n_folds = 10)
		Kindexlist.append(Kindex)
	
	for treenum in trees:
		clflist = [RandomForestClassifier(n_estimators=treenum), AdaBoostClassifier(n_estimators = treenum), tree.DecisionTreeClassifier()]


		holder_df = dowork(filelist, names, clflist, clfnames, nfolds = 10, treenum = treenum, kstrat = False, Kindexerlist = Kindexlist)
		data_df = data_df.append(holder_df, ignore_index=True)
		
	data_df.to_csv('data/results/casestudy1.csv')

	"""
	Case Study 2: RandomForest and AdaBoost Stratified K Folds
	Changing parameter: Kstrat = [True, False]
	Other parameters: treenum = 100
	Data: All data sets
	Kfolds = 10
	"""
	print("Study2")

	clflist = [RandomForestClassifier(n_estimators=100), AdaBoostClassifier(n_estimators = 100)]
	filelist = ['labeled_leuk.csv','labeled_bladder.csv', 'labeled_liver.csv', 'labeled_prostate.csv', 'labeled_colon.csv']
	names = ['leuk','bladder', 'liver', 'prostate', 'colon']
	clfnames = ["RandomForestClassifier", "AdaBoostClassifier"]

	data_df = dowork(filelist, names, clflist, clfnames, nfolds = 10, treenum = 100, kstrat = False)
	datastrat_df = dowork(filelist, names, clflist, clfnames, nfolds = 10, treenum = 100, kstrat = True)

	data_df = data_df.append(datastrat_df, ignore_index = True)

	data_df.to_csv('data/results/casestudy2.csv')


	"""
	Case Study 3: RandomForest Random feature size
	Changing Parameter: max_features = [log2(n), 0.5*[ log2(n) + sqrt(n), sqrt(n), sqrt(2n)]
	Other parameters: treenum = 100, kstrat = false
	Data: All data sets
	Kfolds = 10
	"""
	print("Study3")
	filelist = ['labeled_leuk.csv','labeled_bladder.csv', 'labeled_liver.csv', 'labeled_prostate.csv', 'labeled_colon.csv']
	names = ['leuk','bladder', 'liver', 'prostate', 'colon']
	datalens = []
	for fil in filelist:
		datalens.append(datalen(fil))

	# note that log2(n) and sqrt(n) are already options for the classifer to use so 
	# first send those up. the others will have to be manually done
	
	clflist = [RandomForestClassifier(n_estimators=100, max_features = 'log2'), RandomForestClassifier(n_estimators = 100, max_features = 'sqrt')]
	clfnames = ["RandomForestClassifierLog2", "RandomForestClassifierSqrt"]

	data_df = dowork(filelist, names, clflist, clfnames, nfolds = 10, treenum = 100, kstrat = False)

	# now we have to find the data for max_features = [0.5*[ log2(n) + sqrt(n), sqrt(2n)]
	# each dataset has a different n so we have to loop around a bit.

	filelistmeta = [['labeled_leuk.csv'],['labeled_bladder.csv'], ['labeled_liver.csv'], ['labeled_prostate.csv'], ['labeled_colon.csv']]
	namesmeta = [['leuk'],['bladder'], ['liver'], ['prostate'], ['colon']]

	for idxfm, fillist in enumerate(filelistmeta):

		# find values
		halflogsqrt = int(np.floor(.5*(np.log2(datalens[idxfm]) + np.sqrt(datalens[idxfm]))))
		sqrt2n = int(np.floor(np.sqrt(2*datalens[idxfm])))

		# for each file set make the appropreiate classifer
		clflist = [RandomForestClassifier(n_estimators=100, max_features = halflogsqrt), RandomForestClassifier(n_estimators = 100, max_features = sqrt2n)]
		clfnames = ["RandomForestClassifierHalfLogSqrt", "RandomForestClassifierSqrt2n"]
		
		# predict on a single dataset
		holder_df = dowork(fillist, namesmeta[idxfm], clflist, clfnames, nfolds = 10, treenum = 100, kstrat = False)

		# append together hold_dfs
		data_df = data_df.append(holder_df, ignore_index=True)

	print(data_df)
	# write data to file
	data_df.to_csv('data/results/casestudy3.csv')

	"""
	Case Study 4: ExtraRandom trees v. RandomForest
	Changing parameters: using ExtraRandom trees
	Other parameters: treenum = 100, kstrat = false
	Data: all datasets
	Kfolds: 10
	"""
	print("Study4")
	# datasets names and clfs and names
	filelist = ['labeled_leuk.csv','labeled_bladder.csv', 'labeled_liver.csv', 'labeled_prostate.csv', 'labeled_colon.csv']
	names = ['leuk','bladder', 'liver', 'prostate', 'colon']
	clflist = [RandomForestClassifier(n_estimators=100), ExtraTreesClassifier(n_estimators = 100)]
	clfnames = ["RandomForestClassifier", "ExtraTreesClassifier"]

	data_df = dowork(filelist, names, clflist, clfnames, nfolds = 10, treenum = 100, kstrat = False)

	print(data_df)

	data_df.to_csv('data/results/casestudy4.csv')

	"""
	Case Study 5: RandomForest with BootStrapping True or False
	Changing parameters: BootStrapping True or False
	Other parameters: treenum = 100, kstrat = false
	Data: all datasets
	Kfolds: 10
	"""
	print("Study5")
	clflist = [RandomForestClassifier(n_estimators=100, bootstrap = True), RandomForestClassifier(n_estimators=100, bootstrap = False)]
	filelist = ['labeled_leuk.csv','labeled_bladder.csv', 'labeled_liver.csv', 'labeled_prostate.csv', 'labeled_colon.csv']
	names = ['leuk','bladder', 'liver', 'prostate', 'colon']
	clfnames = ["RandomForestClassifierBootStrap", "RandomForestClassifierNoBootStrap"]

	data_df = dowork(filelist, names, clflist, clfnames, nfolds = 10, treenum = 100, kstrat = False)

	data_df.to_csv('data/results/casestudy5.csv')
	
	"""
	Case Study 6: RandomForest, AdaBoost, Bagging, ExtraTreesClassifier
	Changing parameter: classifer
	Other parameters: Kstrat = True
	Data: All Data sets
	Kfolds = 10
	"""

	print("Study6")
	clflist = [RandomForestClassifier(n_estimators=100), AdaBoostClassifier(n_estimators = 100), BaggingClassifier(n_estimators = 100),ExtraTreesClassifier(n_estimators = 100)]
	filelist = ['labeled_leuk.csv','labeled_bladder.csv', 'labeled_liver.csv', 'labeled_prostate.csv', 'labeled_colon.csv']
	names = ['leuk','bladder', 'liver', 'prostate', 'colon']
	clfnames = ["RandomForestClassifier", "AdaBoostClassifier", "BaggingClassifier", "ExtraTreesClassifier"]

	data_df = dowork(filelist, names, clflist, clfnames, nfolds = 10, treenum = 100, kstrat = True)

	data_df.to_csv('data/results/casestudy6.csv')










