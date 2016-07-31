# Math 502B classification project
# Nicholas Sullivan

from sklearn import tree
from numpy import genfromtxt
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import BaggingClassifier

import numpy as np

if __name__ == '__main__':
	# load the data set
	# reads data row-wise

	# CHOOSE DATASET ID (reduced, leuk)
	dataset = 3

	if dataset == 1:	
	   # REDUCED
	   data = genfromtxt('data/DNA/ReducedDataSet_dataonly.csv', delimiter=',')
	   # extract label and features of training set
	   X = np.transpose(data[1:,:-10])
	   Y = np.transpose(data[0,:-10])

	   Xtest = np.transpose(data[1:,-10:]) # leave 10 out
	   Ytest = np.transpose(data[0,-10:])

	elif dataset == 2:
	   # LEUK
	   data = genfromtxt('data/DNA/labeled_leuk_corrected.csv', delimiter=',', skip_header = 1)
	   # extract label and features of training set
	   X = data[list(range(0,25)) + list(range(48,61)), 1:-1]
	   Y = data[list(range(0,25)) + list(range(48,61)), -1]

	   Xtest = data[list(range(25,48)) + list(range(61,73)), 1:-1]
	   Ytest = data[list(range(25,48)) + list(range(61,73)), -1]
    
	elif dataset == 3:
	   # BLADDER
	   data = genfromtxt('data/DNA/labeled_baddler.csv', delimiter=',', skip_header = 1)
	   # extract label and features of training set
	   X = data[list(range(0,6)) + list(range(7,122)), 1:-1]
	   Y = data[list(range(0,6)) + list(range(7,122)), -1]

	   Xtest = data[list(range(122,126)), 1:-1]
	   Ytest = data[list(range(122,126)), -1]
 	   
	

	
	# Fit and predict with decisiontree classifier
	clfDtree = tree.DecisionTreeClassifier()
	clfDtree = clfDtree.fit(X,Y)

	YpredDtree = clfDtree.predict(Xtest)

	Dtreescore = accuracy_score(Ytest, YpredDtree)
	print("accuracy_score of decision tree")
	print(Dtreescore)

	# Fit and prediction with R forrest
	clfRforest = RandomForestClassifier(n_estimators=100)
	clfRforest = clfRforest.fit(X,Y)

	YpredRforest = clfRforest.predict(Xtest)
	Rforestscore = accuracy_score(Ytest, YpredRforest)
	print("accuracy_score of R forest, with 100 trees")
	print(Rforestscore)
 
 
	# Fit and predict with Bagging
	clfBagging = BaggingClassifier(n_estimators = 100) # default is tree
	clfBagging = clfBagging.fit(X,Y)
     
	YpredBagging = clfBagging.predict(Xtest)
     
	Baggingscore = accuracy_score(Ytest, YpredBagging)
	print("accuracy_score of Bagging, with 100 trees")
	print(Baggingscore)

	# Fit and predict with AdaBoost

	clfAdaBoost = AdaBoostClassifier(n_estimators=100)
	clfAdaBoost = clfAdaBoost.fit(X, Y)
	YpredAdaBoost = clfAdaBoost.predict(Xtest)

	AdaBoostscore = accuracy_score(Ytest, YpredAdaBoost)
	print("accuracy_score of Adaboost, with 100 trees")
	print(AdaBoostscore)


