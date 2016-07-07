class dtree_node(object)
	from math import log
	"""
	Basic decision tree object
	"""
	def __init__(self, data = None, cancercol = None):
		# can be initalized without data or cancercol
		self.cancer_column = cancercol
		if data != None:
			self.create_node(data)

	def create_node(self, data = None):
		# load data here

	def set_entropy(self, data = None):

		### note this needs to be debugged, assuming we are using pandas not sure how this will all work out.
		log2 = lambda x: log(x)/log(2)
		resulttypes = data.cancer_column.value_counts()
		ent = 0
		ent=0.0
   		for r in results.keys():
      		p=float(results[r])/len(rows)
      		ent=ent-p*log2(p)
   		return ent


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
