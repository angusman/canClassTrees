
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sklearn as skl
import sklearn.cross_validation as sklcv
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import BaggingClassifier

from pprint import pprint as pp
from time import time

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

def load_colon():
    data = np.genfromtxt('data/DNA/labeled_colon.csv',
                        delimiter = ',', skip_header = 1)
    X = data[:, 1:-1]
    Y = data[:, -1]
    dset = {}
    dset['observations'] = X
    dset['labels'] = Y
    return dset

def load_liver():
    data = np.genfromtxt('data/DNA/labeled_liver.csv',
                        delimiter = ',', skip_header = 1)
    X = data[:, 1:-1]
    Y = data[:, -1]
    dset = {}
    dset['observations'] = X
    dset['labels'] = Y
    return dset



def fix_y(nfolds, y):
    return y


def do_classification(clfname, clf, x, y, cvnum, esizes):
    res = []
    print clfname
    if clfname == 'dtree':
        C = clf()
        start = time()
        err = sklcv.cross_val_score(C, x, y, cv=cvnum)
        stop = time()
        result = {}
        result['method'] = clfname
        result['trees'] = 1
        result['error'] = err
        result['mean'] = err
        result['min'] = err
        result['max'] = err
        result['std'] = 0
        result['computationtime'] = stop - start
        
        res.append(result)
    else:
        itr = iter(esizes)
        for n_trees in itr:
            C = clf(n_estimators = n_trees)
            start = time()
            err = sklcv.cross_val_score(C, x, y, cv=cvnum)
            stop = time()
            result = {}
            result['method'] = clfname
            result['trees'] = n_trees
            result['error'] = err
            result['mean'] = np.mean(err)
            result['min'] = np.min(err)
            result['max'] = np.max(err)
            result['std'] = np.std(err)
            result['computationtime'] = stop - start
            res.append(result)
        
    return res


def analyze_data(ensemble_sizes, dataset):
    """Produce a dict structure of error and runtime values."""
    
    dsets = {'reduced': load_reduced,
            'leuk': load_leuk,
            'bladder': load_bladder,
            'colon': load_colon,
            'liver': load_liver}
    dstf = dsets[dataset]
    dset = dstf()
    X = dset['observations']
    Y = dset['labels']
    num_obs = X.shape[0]
    num_feats = X.shape[1]

    
    results = {'dtree': {},
              'bagging': {},
              'randomforest': {},
              'adaboost': {},}
    
    classifiers = {'dtree': skl.tree.DecisionTreeClassifier,
                   'bagging': BaggingClassifier,
                   'randomforest': RandomForestClassifier,
                   'adaboost': AdaBoostClassifier}
    cvs = {'KFold1': 2,
          'KFold2': 3,
          'KFold3': 5}
    
    algs = ['adaboost', 'bagging', 'dtree', 'randomforest']
    for algorithm in iter(algs):
        clf = classifiers[algorithm]
        cvruns = {}
        
        for cv, cvnum in cvs.iteritems():
            cvruns[cv] = do_classification(algorithm, clf, X, Y, cvnum, ensemble_sizes)
        
        results[algorithm] = cvruns
    
    return results


"""    
    for algorithm, value in results.iteritems():
        errordt = {}
        for key, clf in classifiers.iteritems():
            classfd = {}
            for cvkey, cvnum in cvs.iteritems():
                classfd[cvkey] = do_classification(key, clf, X, Y, 4)
            errordt[key] = classfd
        results[algorithm] = errordt
"""

def to_file(fname):
    dl = ['bladder', 'colon', 'leuk', 'liver']
    dct = {}
    num_trees = [2, 5, 10, 20]
    for dset in iter(dl):
        dct[dset] = analyze_data(num_trees, dset)
    
    fl = open(fname, 'w+')
    pp(dct, stream=fl)
    fl.close()

def to_spreadsheet(resdict):
    """Make Pandas DataFrames, resdict is output from analyze_data()."""
    dfs = []

to_file('skldt.json')

# num_trees = [2, 5, 10, 20] # add 60, 100 on faster machines
# dtt = analyze_data(num_trees, 'bladder')
# pp(dtt)
