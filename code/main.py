# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     main
   Description :
   Author :       haxu
   date：          2019/4/3
-------------------------------------------------
   Change Activity:
                   2019/4/3:
-------------------------------------------------
"""
__author__ = 'haxu'

import networkx as nx
from deepwalk import DeepWalk
from classify import read_node_label, Classifier
from sklearn.linear_model import LogisticRegression

if __name__ == '__main__':
    G = nx.read_edgelist('../data/Wiki_edgelist.txt',
                         create_using=nx.DiGraph(), nodetype=None, data=[('weight', int)])

    model = DeepWalk(G, walk_length=30, num_walks=80, workers=4)

    model.train(window_size=5, iter=3)
    embeddings = model.get_embeddings()

    X, Y = read_node_label('../data/wiki_labels.txt')

    tr_frac = 0.8
    clf = Classifier(embeddings=embeddings, clf=LogisticRegression())
    clf.split_train_evaluate(X, Y, tr_frac)

