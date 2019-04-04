# Graph Embedding

1. DeepWalk
2. node2vec
3. pytorch-big-graph example



# fb15k example


usage:

```
cd data
unzip fb15k.tgz
```

该数据的保存存储形式为
```<e1, r, e2>```

## 将数据转成 PBG's input format形式
```torchbiggraph_import_from_tsv  --lhs-col=0 --rel-col=1 --rhs-col=2 code/fb15k_config.py data/FB15k/freebase_mtr100_mte100-*.txt```

## 训练
```torchbiggraph_train code/fb15k_config.py -p edge_paths=data/FB15k/freebase_mtr100_mte100-train_partitioned```

## 将节点进行embedding,得到节点的向量化表示。
```torchbiggraph_export_to_tsv --dict data/FB15k/dictionary.json --checkpoint model/fb15k --out joined_embeddings.tsv```
