# Math 502B classification project
# Nicholas Sullivan

from sklearn import tree
from numpy import genfromtxt
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import AdaBoostClassifier



if __name__ == '__main__':
	# load the toydata set	
	thoustoy_data = genfromtxt('objects/thousandtoy.csv', delimiter=',')
	thoustoytest_data = genfromtxt('objects/thousandtoytest.csv', delimiter=',')
	# extract label and features of training set
	X = thoustoy_data[:,1:]
	Y = thoustoy_data[:,0]

	Xtest = thoustoytest_data[:,1:]
	Ytest = thoustoytest_data[:,0]

	
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


	# Fit and predict with AdaBoost

	clfAdaBoost = AdaBoostClassifier(n_estimators=100)
	clfAdaBoost = clfAdaBoost.fit(X, Y)
	YpredAdaBoost = clfAdaBoost.predict(Xtest)

	AdaBoostscore = accuracy_score(Ytest, YpredAdaBoost)
	print("accuracy_score of Adaboost, with 100 trees")
	print(AdaBoostscore)


