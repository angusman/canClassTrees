
from pprint import pprint as pp

import numpy as np
import random
import pandas as pd


class dtree:

	
	# Basic decision tree object

	def __init__(self, data = None, labelcol = None, weights = None, randfeatures = False, rfeaturen = None):
		# can be initalized without data or cancercol
		if rfeaturen == None and randfeatures == True:
			print("specfiy number of randome features to select on each node")
		self.rfeatn = rfeaturen
		self.rfeatures = randfeatures
		self.label = labelcol
		self.featureweights = weights
		self.full_df = data
		self.tree_dict = {}
		return None

	def entropy(self, data = None):
		# calculate entropy of a set

		# get the labels and counts from the given data set
		results = data.iloc[:,self.label].value_counts()
		# inital entropy is 0
		ent=0.0

		# loop over the label types and calculate entropy


		for r in results.keys():
			p = float(results[r])/len(data)
			ent = ent - p*np.log2(p)
  		
		return ent

	def set_splitter(self, data = None, column = None, value = None):
		# take a set and devided it based on the value in a given column, note this is not set up for categorical data.

		leftset = data[data.iloc[:,column] > value]
		rightset = data[data.iloc[:,column] <= value]

		return leftset, rightset


	def information_gain(self, data = None, column = None, value = None):
		# calculate information gain for a split on a given column splitting value found from find_cutoff_value

		# split the data into left and right sets
		leftset, rightset = self.set_splitter(data = data, column = column, value = value)

		# calculate the information gain of split
		infogain = self.entropy(data) - ( float(len(leftset)) / len(data) * self.entropy(leftset) + float(len(rightset)) / len(data) * self.entropy(rightset))

		return infogain

	
	def find_best_split(self, data = None):
		# given a full dataset find the best column to split on


		# find column range to check
		num_cols = len(data.columns)
		col_range = list(range(0,num_cols))
		col_range.remove(self.label)

		if self.rfeatures:

			col_range = random.sample(range(1,num_cols), self.rfeatn)
		else:
			col_range = list(range(0,num_cols))
			col_range.remove(self.label)


		# second loop over columns to try find one with highest information gain.
		# setting starting infogain and targetcolumn
		maxinfogain = 0
		targetcolumn = -1
		targetvalue = 0
		colaverages = list(data.mean(axis = 0))

		for idx, col in enumerate(col_range):
			infogain = self.information_gain(data = data, column = col, value = colaverages[col])

			# if we get a top information gain then we save that and continue
			if infogain >= maxinfogain:
				maxinfogain = infogain
				targetcolumn = col
				targetvalue = colaverages[col]



		# third, split along the column and return the left and right sets
		leftset, rightset = self.set_splitter(data = data,  column = targetcolumn, value = targetvalue)

		return leftset, rightset, targetcolumn, targetvalue, maxinfogain

	def node_tree(self, data = None, min_entropy = None, tree_dict = None):
		# recusively split the tree until all nodes h ave entropy less than min_entropy
		node_counts = dict(data.iloc[:,self.label].value_counts())
		tree_dict["stats"] = { "training_points" : len(data),
							 "point_composition" : node_counts,
							 "node_entropy" : self.entropy(data = data) }

		if self.entropy(data = data) > min_entropy:
			leftset, rightset, targetcolumn, targetvalue, infogain = self.find_best_split(data)


			if infogain <= .000001:
				print("I aborted because of shitty infogain")
				return tree_dict

			tree_dict["column"] = targetcolumn
			tree_dict["value"] = targetvalue
			tree_dict["leftnode"] = self.node_tree(data = leftset, min_entropy = min_entropy, tree_dict = {})
			tree_dict["rightnode"] = self.node_tree(data = rightset, min_entropy = min_entropy, tree_dict = {})


		return tree_dict

	def build_tree(self, data = None, min_entropy = None, tree_dict = None):
		self.tree_dict = self.node_tree(data = data, min_entropy = min_entropy, tree_dict = {})

		return self.tree_dict



	def predict_df(self, sample = None):
		# given a sample dataframe without label predict its label given the tree_dict structure

		# make sure there is a tree in place
		if self.tree_dict == {}:
			return "no tree dictionary found"

		# prepare a vector to put predictions into
		row_pred = []
		# loop over the rows and use the predict_row function on that row
		for k in range(len(sample)):
			prediction = self.predict_row(samplerow = sample.iloc[k,:], tree_dict = self.tree_dict)
			row_pred.append(prediction)


		sample['pred'] = row_pred
		prediction_df = sample
		return prediction_df

	def predict_row(self, samplerow = None, tree_dict = None):
		# helper recusvice function for predict_df
		# note this assumes that the label occupies the first column


		value = list(tree_dict.values())
		keys = list(tree_dict.keys())
		v = list(tree_dict['stats']['point_composition'].values())
		k = list(tree_dict['stats']['point_composition'].keys())
		prediction = None
		# while we still have nodes to continue along for keep digging down
		if "leftnode" in keys:

			if samplerow.iloc[tree_dict["column"]-1] > tree_dict["value"]:
				prediction = self.predict_row(samplerow = samplerow, tree_dict = tree_dict["leftnode"])

			elif samplerow.iloc[tree_dict["column"]-1] <= tree_dict["value"]:
				prediction = self.predict_row(samplerow = samplerow, tree_dict = tree_dict["rightnode"])

		if "leftnode" not in keys:
			prediction = k[v.index(max(v))]
			return prediction

		return prediction


		
