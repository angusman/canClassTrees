class dtree:

	
	# Basic decision tree object

	def __init__(self, data = None, labelcol = None):
		# can be initalized without data or cancercol
		self.label = labelcol
		full_df = data
		return None

	def entropy(self, data = None):
		# calculate entropy of a set
		# we need log
		from math import log

		# defining log base 2
		log2 = lambda x: log(x)/log(2)

		# get the labels and counts from the given data set
		results = data.label.value_counts()
		
		# inital entropy is 0
		ent=0.0

		# loop over the label types and calculate entropy
		for r in results.keys():
			p= float(results[r])/len(data)
			ent=ent-p*log2(p)
  		
		return ent

	def set_splitter(self, data = None, column = None, value = None):
		# take a set and devided it based on the value in a given column, note this is not set up for categorical data.

		leftset = data[data.iloc[:,column] > value]
		rightset = data[data.iloc[:,column] <= value]

		return leftset, rightset

	def find_cutoff_value(self, data = None, column = None):
		# for a given datacol find the aveage value and return this as the cut off value of splitting
		# this could be expanded by in the future to find a better splitting point than just the mean of the data.
		value = data.iloc[:,column].mean()

		return value

	def information_gain(self, data = None, column = None):
		# calculate information gain for a split on a given column splitting value found from find_cutoff_value
		value = self.find_cutoff_value(data = data, column = column)

		# split the data into left and right sets
		leftset, rightset = self.set_splitter(data = data, column = column, value = value)

		# calculate the information gain of split
		infogain = self.entropy(data) - ( float(len(leftset)) / len(data) * self.entropy(leftset) + float(len(rightset)) / len(data) * self.entropy(rightset))

		return infogain, value

	
	def find_best_split(self, data = None):
		# given a full dataset find the best column to split on

		# find column range to check
		num_cols = len(data.columns)
		col_range = list(range(0,num_cols))
		col_range.remove(self.label)

		# second loop over columns to try find one with highest information gain.
		# setting starting infogain and targetcolumn
		maxinfogain = 0
		targetcolumn = -1
		targetvalue = 0

		for col in col_range:
			infogain, value = self.information_gain(data = data, column = col)

			# if we get a top information gain then we save that and continue
			if infogain >= maxinfogain:
				maxinfogain = infogain
				targetcolumn = col
				targetvalue = value


		# third, split along the column and return the left and right sets

		leftset, rightset = self.set_splitter(data = data,  column = targetcolumn, value = targetvalue)

		

		return leftset, rightset

	def create_node(self, data = None):
		# load data here
		return data

	def predict(self, sample):
		# predict the state of the sample
		return prediction

	def display(self):
		# display the tree somehow? low priority task
		return None
