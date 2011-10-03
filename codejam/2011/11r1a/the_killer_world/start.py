#!/usr/bin/python3
import math
import sys

def printe(*st):
   sys.stderr.write(",".join([str(x) for x in st])+"\n")
   
   
def pattern(w,word,ignore):
   p = []
   j = 0
   for i in word:
      if i in ignore:
         continue
      if w == i:
         p.append(j)
      j+=1
   return p
         
      
      
   
def split(w,words,ignore):
   groups = {}
   for word in words:
      p = pattern(w,word,ignore)
      l = len(word)
      key = "_".join([str(x) for x in p])+"X"+str(l)

      if key not in groups:
         groups[key] = []
      groups[key].append(word)      
   return groups         

   
def calc(wordlist,abc,idx):
   if (idx==len(abc)):
      return(0,wordlist)
   if len(wordlist)==1:
      return(0,wordlist)
      
   printe("A",wordlist,abc,idx)
   if len(abc) == 0:
      return(0,wordlist)
         
   w = abc[idx]
      
   ml = []
   mv = -1
   groups = split(w,wordlist,abc[0:idx])
   printe(groups)
   result = []
   
   for g in groups.values():
      (v,ok) = calc(g,abc,idx+1)
      result.append((v,ok,g))
      if mv==-1 or v > mv:
         ml = ok
         mv = v
   l = []
   printe(result)
   
   for r in result:
      if r[0] == mv:
         printe(r[1])
         for x in r[1]:
            l.append(x)
   printe("R",wordlist,abc,idx,1+mv,l)
   return (1+mv,ml)
      


def simulate():
   [N,M] = [int(a) for a in input().split()]
   words = []
   for i in range(N):
      words.append(input())
   result = []
   for j in range(M):
      abc = input()
      res = calc(words,abc,0)[1]
      res.sort()      
      result.append(res[0])
   printe("RESULT",res)
   return " ".join(result)
   
      

      
if __name__ == '__main__':
   for i in range(int(input())):
      print("Case #{}: {}".format(i+1,simulate()))
