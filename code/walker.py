# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     walker
   Description :
   Author :       haxu
   date：          2019/4/3
-------------------------------------------------
   Change Activity:
                   2019/4/3:
-------------------------------------------------
"""
__author__ = 'haxu'

import itertools
import random
import networkx as nx


class RandomWalker:
    def __init__(self, G, p=1, q=1):
        assert isinstance(G, nx.Graph)
        self.G = G
        self.p = p
        self.q = q

    def simulate_walks(self, num_walks, walk_length, workers):
        G = self.G
        nodes = list(G.nodes())

        import multiprocessing as mlp
        results = []
        num_cpu = workers
        pool = mlp.Pool(num_cpu)
        batch_num = num_walks // num_cpu

        for i in range(num_cpu):
            result = pool.apply_async(self._simulate_walks, (nodes, batch_num, walk_length,))
            results.append(result)

        pool.close()
        pool.join()

        walks = []
        for result in results:
            feat = result.get()
            walks.append(feat)

        walks = list(itertools.chain(*walks))

        # walks = self._simulate_walks(nodes, num_walks, walk_length)
        print(len(walks))

        return walks

    def deepwalk_walk(self, walk_length, start_node):
        walk = [start_node]
        while len(walk) < walk_length:
            cur = walk[-1]
            cur_nbrs = list(self.G.neighbors(cur))
            if len(cur_nbrs) > 0:
                walk.append(random.choice(cur_nbrs))
            else:
                break
        return walk

    def _simulate_walks(self, nodes, num_walks, walk_length):
        walks = []
        for _ in range(num_walks):
            random.shuffle(nodes)
            for v in nodes:
                if self.p == 1 and self.q == 1:
                    walks.append(self.deepwalk_walk(walk_length=walk_length, start_node=v))

        return walks
