#!/usr/bin/python
   
def biggest(arr):
   max = 0
   curr = 0
   for i in arr:
      if i == '0':
         curr +=1
      if i == '1':
         curr = 0
      if (curr>max):
         max = curr
   return max   
            
      
      
def process():
   [L,W] = [int(x) for x in input().split()]
   area = []
   for i in range(W):
      m = input().translate("".maketrans('SGWRT','00111'))
      size = len(m)
      val = eval('0b'+m)
      area.append(val)
   
   maxv = 1
   for a in range(W):
      t = area[a]
      for b in range(a+1,W):
         t = t | area[b]
         form = "{0:0>"+str(size)+"b}"
         bin = form.format(t)
         big = biggest(bin)
         maxv = max(maxv,big*(b-a+1))
   return maxv

if __name__ == '__main__':
   for i in range(int(input())):
      print("Case #{0}: {1}".format(i+1,process()))
         
      
