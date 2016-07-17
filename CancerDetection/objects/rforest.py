from dtree_rforest import dtree_rforest
class rforest:
    
    
    # Random forest object utilizing dtree
    
    def __init__(self, data = None, labelcol = None):
        # can be initialized without data or labels
        self.label = labelcol
        forest = {}
        return None
    
    
    def build_forest(self, data = None, ktrees = 10, msamples = None, nfeatures = None):
        ### default msamples to length of data (WARNING!! not actually None default!!)
        if msamples == None:        
            msamples = len(data)        
        
        # train classifiers
        
        # initialize list of classifiers
        self.forest = []
        
        # build k tree classifiers
        for i in range(int(ktrees)):
            data_tc = self.sample_data(data = data, msamples = msamples)
            mytree = dtree_rforest(data = data_tc, labelcol = 0, nfeatures = nfeatures)
            self.forest.append(mytree)
            
            
        return self.forest
    
    
    def sample_data(self, data = None, msamples = None):
        # uniformly sample data with replacement
        import numpy as np
    
        # bootstrap replicates take same number of samples as original
        row_indx = np.random.randint(0, high = len(data), size = msamples)
        
        # sample data according to indices and selected features
        data_sampled = data.iloc[row_indx,:]
        
        return data_sampled
        
        
    def predict_df(self, sample = None):
        # given a sample dataframe without labels, predict its label as the mode of trees
        import pandas as pd

        
        # make sure build_forest has been run
        if self.forest == {}:
            return "no forest found"
            
        # prepare a vector to put predictions into    
        subpredictions = pd.DataFrame()        
        
        # use tree classifiers to predict
        for i in range(len(self.forest)):
            self.forest[i].tree_dict = self.forest[i].build_tree(data = self.forest[i].full_df, min_entropy = .1, tree_dict = {})
            prediction = self.forest[i].predict_df(sample).iloc[:,-1]
            subpredictions = pd.concat([subpredictions,prediction], axis = 1)
              
        sample['pred'] = self.compute_mode(labels = subpredictions)
        prediction_df = sample
        return prediction_df
      
      
    def compute_mode(self, labels = None):
        ### find the mode of binary labeling (WARNING!! hardcoded for "A" and "B")
        import numpy as np
    
        label1count = np.sum(labels == "A", axis = 1)
        label2count = label1count - len(self.forest)
        
        # +1 if "A", -1 if "B", 0 if tie
        signs = np.sign(label1count+label2count)
        
        prediction_mode = []
        for i in range(len(signs)):
            if signs[i] == 1:
                prediction_mode.append("A")
            elif signs[i] == -1:
                prediction_mode.append("B")
            else:
                guess = np.random.randint(0,2)
                if guess == 0:
                    prediction_mode.append("A")
                else:
                    prediction_mode.append("B")
                    
        return prediction_mode
        
        