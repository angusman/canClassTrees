import pandas as pd 
from dtree import dtree
from pprint import pprint as pp

if __name__ == '__main__':
	data_df = pd.read_csv('toydataset.csv')

	print("full toy data set")
	print(data_df)

	mytree = dtree(data = data_df, labelcol = 0)
	entropy = mytree.entropy(data_df)
	print("entropy of fullset")
	print(entropy)

	meanvalue = mytree.find_cutoff_value(data = data_df, column = 2)
	print("finding value to split on for feature2 column")
	print(meanvalue)

	leftset, rightset = mytree.set_splitter(data = data_df, column = 2, value = meanvalue)
	print("spltting dataset on feature2 column for value = meanvalue")
	print("leftset")
	print(leftset)
	print("rightset")
	print(rightset)



	infogain, value = mytree.information_gain(data = data_df, column = 2)
	print("calculating information gain and splitting value  feature2")
	print("information gain:")
	print(infogain)
	print("splitting value")
	print(value)

	leftsets, rightsets, targetcolumn, targetvalue = mytree.find_best_split(data = data_df)

	print("best split for full data")
	print("leftset")
	print(leftsets)
	print("rightset")
	print(rightsets)

	sampletree = mytree.bulid_tree(data = data_df, min_entropy = .5 ,tree_dict = {})

	pp(sampletree)