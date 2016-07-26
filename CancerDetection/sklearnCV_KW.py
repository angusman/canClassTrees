
import numpy as np
import matplotlib.pyplot as plt
import sklearn as skl
import sklearn.cross_validation as sklcv
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import BaggingClassifier


"""Each function returns a dictionary of observations and labels"""

def load_reduced():
    """Load Reduced dataset. Return a dict"""
    data = np.genfromtxt('data/DNA/ReducedDataSet_dataonly.csv')
    X = np.transpose(data[1:, :-10])
    Y = np.transpose(data[0, :-10])
    dset = {}
    dset['observations'] = X
    dset['labels'] = Y
    
    return dset

def load_leuk():
    data = np.genfromtxt('data/DNA/labeled_leuk_corrected.csv',
                        delimiter = ',', skip_header = 1)
    X = data[:, 1:-1]
    Y = data[:, -1]
    dset = {}
    dset['observations'] = X
    dset['labels'] = Y
    
    return dset

def load_bladder():
    data = np.genfromtxt('data/DNA/labeled_bladder.csv',
                        delimiter = ',', skip_header = 1)
    X = data[:, 1:-1]
    Y = data[:, -1]
    dset = {}
    dset['observations'] = X
    dset['labels'] = Y
    return dset

def analyze_data(dataset):
    """Produce a dict structure of error and runtime values."""
    dsets = {'reduced': load_reduced,
            'leuk': load_leuk,
            'bladder': load_bladder}
    dstf = dsets[dataset]
    dset = dstf()
    X = dset['observations']
    Y = dset['labels']
    num_obs = X.shape[0]
    
    results = {'dtree': {},
              'bagging': {},
              'randomforest': {},
              'adaboost': {}}
    
    classifiers = {'dtree': skl.tree.DecisionTreeClassifier(),
                   'bagging': BaggingClassifier(),
                   'randomforest': RandomForestClassifier()}
    cvs = {'KFold3': 3,
          'KFold5': 5,
          'KFold7': 7,
          'KFold10': 10,
          'KFold13': 13}
    
    for algorithm, value in results.iteritems():
        errordt = {}
        for key, clf in classifiers.iteritems():
            print clf
            classfd = {}
            for cvkey, cvnum in cvs.iteritems():
                C = skl.tree.DecisionTreeClassifier()
                classfd[cvkey] = sklcv.cross_val_score(C, X, Y, cv=cvnum)
            errordt[key] = classfd
        results[algorithm] = errordt
    
    return results

analyze_data('bladder')

