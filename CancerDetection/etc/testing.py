import pandas as pd 
# from dtree import dtree
from pprint import pprint as pp

if __name__ == '__main__':
	# data_df = pd.read_csv('thousandtoy.csv')

	# print("full toy data set")
	# print(len(data_df))

	# mytree = dtree(data = data_df, labelcol = 0)

	# sampletree = mytree.build_tree(data = data_df, min_entropy = .1 ,tree_dict = {})

	# pp(sampletree)

	# test_df = pd.read_csv("thousandtoytest.csv")
	# unknown_df = test_df.iloc[:,1:]
	# prediction = mytree.predict_df(unknown_df)

	# test_pred_df = test_df
	# test_pred_df['pred'] = prediction['pred']


	# test_pred_df['correct'] = test_df.iloc[:,0] == test_pred_df["pred"]
	# print('preditions on thousandtoytest')
	# print(test_pred_df)


	# correct_precentage = float(len(test_pred_df[test_pred_df['correct'] == True]))/len(test_pred_df)
	# print("correct percentage of Dtree with traning data derived of the same way")
	# print(correct_precentage)


	# print("training and testing with random feature selection")


	# badmodel = dtree(data = data_df, labelcol = 0, randfeatures = True, rfeaturen = 5)
	# badtree = badmodel.build_tree(data = data_df, min_entropy = .1 ,tree_dict = {})
	# bad_pred_df = badmodel.predict_df(unknown_df)
	# bad_pred_df['correct'] = test_df.iloc[:,0] == bad_pred_df["pred"]

	# print("tree of with random feature selection on each node")
	# pp(badtree)

	# print(bad_pred_df)

	# correct_precentage = float(len(bad_pred_df[bad_pred_df['correct'] == True]))/len(bad_pred_df)
	# print("correct percentage of Dtree random feature selection at each node")
	# print(correct_precentage)

	data = pd.read_csv("../data/results/casestudiesNEWdata/casestudy6a.csv")

	rowlist = []
	for row in range(len(data.index)):
		rowserries = data.iloc[row,:]
		for val in range(10):
			rowdict = {}
			rowdict["Accuracy"] = rowserries[str("fold"+str(val))]
			rowdict["cancertype"] = rowserries["cancertype"]
			rowdict["method"] = rowserries["method"]
			print(rowdict)
			print(rowserries[str("fold"+str(val))])
			rowlist.append(rowdict)


	meltdata = pd.DataFrame(rowlist)
	print(meltdata)
	print(meltdata.shape)

	meltdata.to_csv("../data/results/casestudiesNEWdata/casestudy6aMelt.csv")




