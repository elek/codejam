#!/usr/bin/python3

def process():
   st = input()
   num = {}
   for i in range(len(st)):      
      num[st[i]] = 1
   base = len(num)
   if (base==1):
      base = 2
   values = {}
   summa = 0
   val = 2
   for i in range(len(st)):
      if st[i] in values:
         m = values[st[i]]
      else :
         if len(values)==0:
            values[st[i]] = 1
            m = 1
         elif len(values)==1:
            values[st[i]] = 0
            m = 0
         else:
            m = val
            val += 1
            values[st[i]] = m
         
      summa += m * base ** (len(st)-i - 1)
   return summa

if __name__ == '__main__':
   for i in range(int(input())):
      print("Case #{0}: {1}".format(i+1,process()))
