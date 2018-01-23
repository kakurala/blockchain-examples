#!/usr/bin/python

from merkleTree import * 
import hashlib

for i in range(0, 1):
	print(str(i)+'  '+hashlib.sha256(str(i)).hexdigest())
X = merkle_tree(range(0,1))
print "Tree:", X
print "Height:", len(X) - 1
P = merkle_path(1, X)
print "Path:", P
print "Valid path:", merkle_proof(H(1), P, X[-1][0])
