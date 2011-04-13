#!/usr/bin/python
def process():
   input()
   red = []
   blue = []
   for st in input().split():
      if st[-1]=='R':
         red.append(int(st[0:-1]))
      else:
         blue.append(int(st[0:-1]))
   
   red.sort(reverse=True)
   blue.sort(reverse=True)
   
   a = min(len(red),len(blue))
   s = 0
   for x in range(a):
      s += red[x] - 1
      s += blue[x] - 1
   return s
    

if __name__ == '__main__':
   for i in range(int(input())):
      print("Case #{0}: {1}".format(i+1,process()))
         
      
