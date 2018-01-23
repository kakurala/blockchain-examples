#!/usr/bin/env python
from hashlib import sha256
 
H = lambda *x: sha256(''.join([str(X) for X in x])).hexdigest()
 
def merkle_tree(items):
    """Given an array of items, build a merkle tree"""
    tree = [[H(x) for x in items]]
    while len(tree[-1]) != 1:
        it = iter(tree[-1])
        tree.append([H(item, next(it, item)) for item in it])
    return tree
 
 
def merkle_path(item, tree):
    """Given an item and a tree, return its path"""
    lvl = 0
    itemidx = tree[lvl].index(H(item))
    even = itemidx % 2
    baseidx = itemidx - even
    otheridx = itemidx - 1 if even else idx + 1
    path = [tree[lvl][otheridx]]
    lvl += 1
    while len(tree[lvl]) != 1:
        baseidx = baseidx / 2
        path += tree[lvl][baseidx:baseidx+2]
        lvl += 1
    return path
 
 
def merkle_proof(item, path, root):
    path.insert(0 if H(item, path[0]) == path[0] else 1, item)
    it = iter(path)
    calc_root = None
    for x in it:
        y = next(it)
        calc_root = H(x, y)
    return calc_root == root
 
