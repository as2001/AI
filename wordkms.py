#! /usr/bin/python3

import sys
import heapq

f = open('dictall.txt','r')
inp = open(sys.argv[1],'r')
outp = open(sys.argv[2],'w')

inputs = inp.read().split()
length = len(inputs[0])
lives = 5

words = {x for x in f.read().split() if len(x) == length}
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

wr = []s

for x in inputs:
    guesses = []
    path

outp.write('\n'.join(wr))

f.close()
inp.close()
outp.close()
