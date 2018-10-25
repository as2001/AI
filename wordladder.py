#! /usr/bin/python3

import sys
import heapq

f = open('dictall.txt','r')
inp = open(sys.argv[1],'r')
outp = open(sys.argv[2],'w')

inputs = [x.split(',') for x in inp.read().split()]
length = len(inputs[0][0])

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

def checkdiff(str1,str2):
    counter = 0
    for i in range(len(str1)):
        if str1[i,i+1] == str2[i,i+1]:
            counter += 1
    return counter

for x in inputs:
    heap = [(checkdiff(x[0],x[1]),x[0],[])]
    while heap[-1][1] != x[1]:
        word = d[heapq.heappop(heap)]
        for neighbor in d[word[1]]:
            heapq.heappush((checkdiff(neighbor,x[1]) + len(word[2]) + 1,neighbor,word[2].append(word[1])))


        

