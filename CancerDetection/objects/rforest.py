from objects.dtree import dtree
import numpy as np
from pprint import pprint as pp
# from pprint import pprint as pp

class rforest:
    
    
    # Random forest object utilizing dtree
    
    def __init__(self, data = None, labelcol = None):
        # can be initialized without data or labels
        self.label = labelcol
        forest = {}
        return None
    
    
    def build_forest(self, data = None, ktrees = 10, msamples = None, nfeatures = None, randfeatures = None):
        ### default msamples to length of data (WARNING!! not actually None default!!)
        if msamples == None:        
            self.msamples = len(data)
        else:
            self.msamples = msamples
        # if number of features exceeds number of total features
        if nfeatures == "bagging" or nfeatures > data.shape[1]-1:  
            nfeatures = data.shape[1]-1

        # train classifiers
        
        # initialize list of classifiers
        self.forest = []
        self.posvalues = data.iloc[:,self.label]
        
        # build k tree classifiers
        for i in range(int(ktrees)):
            print('building tree',i +1, 'of ',int(ktrees))
            data_tc = self.sample_data(data = data, msamples = msamples)
            mytree = dtree(data = data_tc, labelcol = self.label, randfeatures = True, rfeaturen = nfeatures)
            treedict = mytree.build_tree(data = data_tc, min_entropy = .1)
            self.forest.append(mytree)


            
            
        return self.forest
    
    
    def sample_data(self, data = None, msamples = None):
        # uniformly sample data with replacement
    
        # bootstrap replicates take same number of samples as original
        row_indx = np.random.randint(0, high = len(data), size = msamples)
        
        # sample data according to indices and selected features
        data_sampled = data.iloc[row_indx,:]
        
        return data_sampled
        
        
    def predict_df(self, sample = None):
        # given a sample dataframe without labels, predict its label as the mode of trees
        import pandas as pd

        
        # make sure build_forest has been run
        if self.forest == []:
            return "no forest found"
            
        # prepare a vector to put predictions into    
        subpredictions = pd.DataFrame()
        # use tree classifiers to predict

        # setting up vector told dictionary of predictions, each entry contains a dictionary of votes from each tree
        predictvect = []
        # populate the prediction vector with dictionaries containing zero votes for all possiblities
        
        for i in range(len(sample)):
            pdict = {}
            for val in self.posvalues:
                pdict[val] = 0
            predictvect.append(pdict)

        # now prediction 
        for i in range(len(self.forest)):
            # get the prediction
            prediction = self.forest[i].predict_df(sample)['pred']

            # increment the proper value of prediction in the predictvect
            for idx,val in enumerate(prediction):

                predictvect[idx][val] = predictvect[idx][val]+1

            # subpredictions = pd.concat([subpredictions,prediction], axis = 1)
              
        sample["pred"] = self.compute_mode(predvect = predictvect)

        prediction_df = sample
        return prediction_df
      
      
    def compute_mode(self, predvect = None):
        # altered to accept prediction vector as made in predict_df
        predictions = []

        for idx, val in enumerate(predvect):
            # find the max value for the keys of the prediction dictionary
            k = list(val.keys())
            v = list(val.values())
            idxpredict = k[v.index(max(v))]

            # append that to the list of predictions
            predictions.append(idxpredict)

        return predictions

        
        