class dtree_node(object)
	"""
	Basic decision tree object
	"""
	def __init__(self, data = None):
		if data != None:
			self.load_data(data)

	def create_node(self, data = None):
		# load data here

	def set_entropy(self, data = None, Column = None, Value = None):
		# for a given set calculate the entrop of a set

		return entropy

	def find_cutoff_value(self, datacol = None):
		# for a given datacol find the aveage value and return this as the cut off value of splitting

		return value
	
	def find_best_split(self, data = None):
		# send in the entire dataset at this node level, returns the best sets to return on.


		return leftset, rightset

	def predict(self, sample):
		# predict the state of the sample
		return prediction

	def display(self):
		# display the tree somehow? low priority task
