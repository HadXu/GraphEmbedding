# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     fb15k_config.py
   Description :
   Author :       haxu
   date：          2019/4/4
-------------------------------------------------
   Change Activity:
                   2019/4/4:
-------------------------------------------------
"""
__author__ = 'haxu'

entity_base = "data/FB15k"


def get_torchbiggraph_config():
    config = dict(
        entity_path=entity_base,

        num_epochs=3,

        entities={
            'all': {'num_partitions': 1},
        },

        relations=[{
            'name': 'all_edges',
            'lhs': 'all',
            'rhs': 'all',
            'operator': 'complex_diagonal',
        }],
        dynamic_relations=True,

        edge_paths=[],

        checkpoint_path='model/fb15k',

        dimension=400,
        global_emb=False,
        comparator='dot',
        loss_fn='softmax',
        lr=0.1,
        num_uniform_negs=1000,

        eval_fraction=0,  # to reproduce results, we need to use all training data
    )

    return config
