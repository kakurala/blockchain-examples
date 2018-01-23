#!/usr/bin/python

import hashlib

def mine(target):
  nounce=0
  data= 'Hello World'
  currentHash =  hashlib.sha256(b'Hello World'+ bytes(nounce)).hexdigest()
  currentHashInDecimal = int(currentHash, 16)
  # compare current solution satisfied the given difficulty (i.e 5 leading zero's in hash)
  while currentHashInDecimal >= target:
    dataTmp = data + str(nounce)
    hash_object = hashlib.sha256(bytes(dataTmp))
    currentHash = hash_object.hexdigest()
    nounce=nounce+1
    currentHashInDecimal=int(currentHash, 16)
    # comment below line to speed up the mining
    print('Hash  :'+ str(nounce)+' - '+currentHash)
  return {"hash":currentHash, "nounce":nounce, "data": data}
  
print(mine(int('00000000f0000000000000000000000000000000000000000000000000000000', 16)))
