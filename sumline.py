#! /usr/bin/python3

import sys

def main():
    inp = open(sys.argv[1],'rU').read().split('\n')
    outp = open(sys.argv[2],'w')
    wr = []
    for line in inp:        
      nums = [x.strip() for x in line.split(',') if x.strip().isdigit()]
      if nums:
        sm = sum(int(x) for x in nums)
        if sm > 0:
            wr.append(str(sm))    
    outp.write('\n'.join(wr))
    outp.close()
    
main()
