#! /usr/bin/python3

import sys

fin = open("dictall.txt","rU")
inp = open(sys.argv[1],"rU")
outp = open(sys.argv[2],"w")

req = inp.read().split()
length = len(req[0])
words = {x for x in fin.read().split() if len(x) == length}
d = dict()

for x in words:
    d[x] = []
    for i in range(length):
        for a in "abcdefghijklmnopqrstuvwxyz":
            if a == x[i:i+1]:
                continue
            tmp = x[:i] + a + x[i+1:]
            if tmp in d:
                d[x].append(tmp)
                d[tmp].append(x)

wr = []

for x in req:
    wr.append(x + "," + str(len(d[x])))

outp.write("\n".join(wr))

fin.close()
inp.close()
outp.close()
                        
                    
