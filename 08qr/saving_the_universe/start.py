#!/usr/bin/python

def solve(sites,words):
   switch = 0
   current_sites = sites[:]
   while (len(words)>0):         
      while (len(current_sites)>0 and 0<len(words)):
         word = words[0]
         words = words[1:]
         if (word in current_sites):
            current_sites.remove(word)
      if (len(current_sites)==0):
         switch += 1
         current_sites = sites[:]
         current_sites.remove(word)
   return switch
     
   
def main():
   for i in range(input()):
      sites = [raw_input() for x in range(input())]
      words = [raw_input() for y in range(input())]
      print "Case #%s:"%(i+1),
      print solve(sites,words)

if __name__ == '__main__':
   main()
