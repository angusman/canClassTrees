import numpy as np
import pandas as pd

from dtree import dtree


    

def grow_tree(ws, learn_set, sample_size):
    """Grow a decision tree using given weights ws and DataFrame learn_set"""
    sample_set = learn_set.sample(n = sample_size, weights = ws,
                                  replace = True, axis = 0)
    return DTree(data = sample_set)

def learn_error(D, h_t, y):
    n = len(D)
    err = 0
    
    for i in xrange(n):
        if h_t[i] != y[i]:
            err = err + D[i]
    
    
    # numerically stable way to compute e^(-al_t) and e^(al_t)
    enalt = np.sqrt(error_t/(1 - error_t))
    ealt = np.sqrt((1 - error_t)/error_t)
    
    for i in xrange(n):
        if h_t[i] == y[i]:
            Dnew[i] = D[i]*enalt
        else:
            Dnew[i] = D[i]*ealt
    
    # normalize
    Z = sum(Dnew)
    Dnew = (1/Z)*Dnew
    return Dnew

def my_booster(learn_set, test_x, test_y, sampling_size, num_boosts):
    """AdaBoost, learn_set is the learning set
     test_x is a df, test_y is a series. Return a list of learner objects"""
    k = num_boosts
    
    # number of observations
    num_obs = num_observations(learn_set)
    learners = []
    
    # Sum of alpha weighted hypotheses
    hsum = 0
    
    # initial weights
    D = (1.0/num_obs)*np.ones(num_obs)
    
    while k > 0:
        tree_t = grow_tree(D, learn_set)
        h_t = tree_t.classify(test_x)
        error_t = learn_error(D, h_t, y)
        alpha_t = 0.5*np.log((1.0 - error_t)/error_t)
        learners.append({'alpha': alpha_t, 'tree': learner_t, 'D': D})
        D = update_weights(D, h_t, y, error_t)
        k = k - 1
    return learners

def boost_classify(learners, vct):
    """Run a set of boosted learners"""
    hypothesis_sum = 0
    for learner in learners:
        alpha_t = learner['alpha']
        tree_t = learner['tree']
        h_t = tree_t.classify(vct)
        hypothesis_sum = hypothesis_sum + alpha_t*h_t
    
    return np.sign(hypothesis_sum)


