#! /usr/bin/python3

import sys 

class Pqueue:
  
  def OrdinaryComparison(a,b):
    if a < b:
      return -1
    if a > b:
      return 1
    return 0
  
  def __init__(self, comparator = OrdinaryComparison):
    self.queue = []
    self.cmpfunc = comparator
      
  def push(self,data):
    currentIndex = len(self.queue)
    self.queue.append(data)
    while (currentIndex-1)/2 >= 0:
      if self.cmpfunc(self.queue[(currentIndex-1)/2],self.queue[currentIndex]) > 0:
        self.queue[currentIndex], self.queue[(currentIndex-1)/2] = self.queue[(currentIndex-1)/2], self.queue[currentIndex]
        currentIndex = (currentIndex-1)/2
      else:
        break
        
  def pop(self):
    if len(self.queue) < 1:
      return None
    retVal = self.queue[0]
    self.queue[0] = self.queue[-1]
    del self.queue[-1]
    currentIndex = 0
    while currentIndex*2+1 < len(self.queue):
      repeat = False
      if currentIndex*2+2 < len(self.queue):
        if self.cmpfunc(self.queue[currentIndex],self.queue[currentIndex*2+2]) > 0 and self.cmpfunc(self.queue[currentIndex*2+2],self.queue[currentIndex*2+1]) < 0:
          self.queue[currentIndex], self.queue[currentIndex*2+2] = self.queue[currentIndex*2+2], self.queue[currentIndex]
          currentIndex = currentIndex*2+2
          repeat = True
      if not repeat and self.cmpfunc(self.queue[currentIndex],self.queue[currentIndex*2+1]) > 0:
        self.queue[currentIndex], self.queue[currentIndex*2+1] = self.queue[currentIndex*2+1], self.queue[currentIndex]
        currentIndex = currentIndex*2+1
        repeat = True
      if not repeat:
        break
    return retVal
        
  def peek(self):
    if len(self.queue) > 0:
      return self.queue[0]
    return None
  
  def tolist(self):
    retList = []
    while len(self.queue) > 0:
      retList.append(self.pop())
    return retList      

def main():
  inp = open(sys.argv[1],'rU').read().split('\n')
  outp = open(sys.argv[2],'w')
  wr = []
  PQ = Pqueue()
  for line in inp:
    args = line.split(',')
    if 'push' in line:
        for x in args[1:]:
            PQ.push(int(x))
    elif 'peek' in line:
        wr.append(str(PQ.peek()))
    elif 'pop' in line:
        wr.append(str(PQ.pop()))
    else:
        wr.append(str(PQ.tolist()))
  outp.write('\n'.join(wr))
  outp.close()
    
main()
