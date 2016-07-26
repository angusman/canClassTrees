
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
    data = np.genfromtxt('data/DNA/ReducedDataSet_dataonly.csv').transpose()
    X = data[:, 1:-1]
    Y = data[:, 0]
    dset = {}
    dset['observations'] = X
    dset['labels'] = Y
    
    return dset

def load_leuk():
    data = np.genfromtxt('data/DNA/labeled_leuk.csv',
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

def analyze_data(ensemble_n_estimators, dataset):
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
    
    classifiers = {'dtree': skl.tree.DecisionTreeClassifier,
                   'bagging': BaggingClassifier,
                   'randomforest': RandomForestClassifier,
                   'adaboost': AdaBoostClassifier}
    cvs = {'KFold3': 3,
          'KFold5': 5,
          'KFold7': 7}
    
    for algorithm, value in results.iteritems():
        errordt = {}
        for key, clf in classifiers.iteritems():
            classfd = {}
            for cvkey, cvnum in cvs.iteritems():
                if key == 'dtree':
                    C = clf()
                else:
                    C = clf(n_estimators = ensemble_n_estimators)
                classfd[cvkey] = sklcv.cross_val_score(C, X, Y, cv=cvnum)
            errordt[key] = classfd
        results[algorithm] = errordt
    
    return results

dtt = analyze_data('reduced')

print dtt
