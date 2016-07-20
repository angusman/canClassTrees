import numpy as np
import pandas as pd

from dtree import dtree


class MyAdaBooster:
    LearnClass = dtree
    
    def __init__(self, data = None, labelcol = None, num_boosts):
        self.label = labelcol
        self.full_df = data
        self.num_obs = data
        self._learners = self.boost(num_boosts)
           
    def predict_row(self, observation):
        """Classify an observation."""
        hypothesis_sum = 0
        
        for learner in self._learners:
            alpha_t = learner['alpha']
            tree_t = learner['tree']
            h_t = tree_t.predict(observation)
            hypothesis_sum = hypothesis_sum + alpha_t*h_t
        
        return hypothesis_sum
    
    
    def _n_obs(df):
        return df.shape[0]
    
    def _grow_learner(ws, learn_set, sample_size):
        """Grow a learner from a sample of learn_set with given weights ws."""
        sample_set = learn_set.sample(n = sample_size, weights = ws, replace = True)
        return dtree(data = sample_set)
    
    def _learn_error(D, h_t, y):
        n = len(D)
        err = 0
        
        for i in xrange(len(D)):
            if h_t[i] != y[i]:
                err = err + D[i]
        return err
    
    def _update_weights(D, h_t, y, error_t):
        n = len(D)
        Dnew = np.zeros(n)
        
        # numerically stable way to compute e^(-al_t) and e^(al_t)
        enega = np.sqrt(error_t/(1 - error_t))
        eposa = np.sqrt((1 - error_t)/error_t)
        
        for i in xrange(n):
            if h_t[i] == y[i]:
                Dnew[i] = D[i]*enega
            else:
                Dnew[i] = D[i]*eposa
        
        Z = sum(Dnew)
        Dnew = (1.0/Z)*Dnew
        
        return Dnew
        
        def boost(self, num_boosts):
            k = num_boosts
            y = self.labelcol
            
            learners = []
            
            # initial weights
            D = (1.0/self.num_obs)*np.ones(self.num_obs)
            
            while k > 0:
                tree_t = self._grow_learner(D, self.full_df)
                h_t = tree_t.predict_row(sample = self.full_df)
                error_t = self._learn_error(D, h_t, y)
                alpha_t = 0.5*np.log((1.0 - error_t)/error_t)
                learners.append({'alpha': alpha_t, 'tree': tree_t, 'D': D})
                D = self._update_weights(D, h_t, y, error_t)
                k = k - 1
            
            return learners

