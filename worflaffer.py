#! /usr/bin/python3

import sys
import heapq

f = open('dictall.txt','r')

length = 4

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
        if str1[i:i+1] != str2[i:i+1]:
            counter += 1
    return counter

kek = []
inputs = []

for x in d:
    for y in d:
        if x != y and checkdiff(x,y) == length and (y,x) not in inputs:
            inputs.append((x,y))
print(inputs)
for x in inputs:
    print(x)
    frontier = [(checkdiff(x[0],x[1]),x[0],[x[0]])]
    explored = set()
    while True:
        if not frontier:
            solution = [x[0],x[1]]
            break
        word = heapq.heappop(frontier)
        if word[1] in explored:
            continue
        if word[1] == x[1]:
            solution = word[2]
            break
        for neighbor in d[word[1]]:
            print(neighbor)
            new2 = word[2][:]
            new2.append(neighbor)
            heapq.heappush(frontier,(checkdiff(neighbor,x[1]) + len(word[2]),neighbor,new2))
        explored.add(word[1])
    if len(solution) > len(kek):
        kek = solution

print(kek)

f.close()
