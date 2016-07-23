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

	# REDUCED
	data = genfromtxt('data/DNA/ReducedDataSet_dataonly.csv', delimiter=',')
	# extract label and features of training set
	# CV-10 fold
	Dtreemiss = []
	Rforestmiss = []
	Baggingmiss = []
	AdaBoostmiss = []
	for i in range(0,13):
	    test = list(range(0+i*10,10+i*10))
	    train = list(range(0,139))
	    del train[(0+i*10):(10+i*10)]         
	         
	    X = np.transpose(data[1:,train])
	    Y = np.transpose(data[0,train])

	    Xtest = np.transpose(data[1:,test]) # leave 10 out
	    Ytest = np.transpose(data[0, test])


	    # Fit and predict with decisiontree classifier
	    clfDtree = tree.DecisionTreeClassifier()
	    clfDtree = clfDtree.fit(X,Y)

	    YpredDtree = clfDtree.predict(Xtest)

	    Dtreescore = accuracy_score(Ytest, YpredDtree, normalize = False)
	    Dtreemiss.append(10 - Dtreescore)

	    # Fit and prediction with R forrest
	    clfRforest = RandomForestClassifier(n_estimators=100)
	    clfRforest = clfRforest.fit(X,Y)

	    YpredRforest = clfRforest.predict(Xtest)
	    Rforestscore = accuracy_score(Ytest, YpredRforest, normalize = False)
	    Rforestmiss.append(10 - Rforestscore)
 
 
	    # Fit and predict with Bagging
	    clfBagging = BaggingClassifier(n_estimators = 100) # default is tree
	    clfBagging = clfBagging.fit(X,Y)
     
	    YpredBagging = clfBagging.predict(Xtest)
     
	    Baggingscore = accuracy_score(Ytest, YpredBagging, normalize = False)
	    Baggingmiss.append(10 - Baggingscore)

	    # Fit and predict with AdaBoost

	    clfAdaBoost = AdaBoostClassifier(n_estimators=100)
	    clfAdaBoost = clfAdaBoost.fit(X, Y)
	    YpredAdaBoost = clfAdaBoost.predict(Xtest)

	    AdaBoostscore = accuracy_score(Ytest, YpredAdaBoost, normalize = False)
	    AdaBoostmiss.append(10 - AdaBoostscore)

import matplotlib.pyplot as plt
plt.hist(Dtreemiss)
plt.title("Dtreemiss")
plt.show()

plt.hist(Rforestmiss)
plt.title("Rforestmiss")
plt.show()

plt.hist(Baggingmiss)
plt.title("Baggingmiss")
plt.show()

plt.hist(AdaBoostmiss)
plt.title("AdaBoostmiss")
plt.show()

print("Number and type of missclassified points (0 = no error, 1 = 1 error, etc)")
