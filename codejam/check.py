#!/usr/bin/python3

import os
from os import path
from subprocess import call
import filecmp

tests = ['small','large']

def compare(fn1,fn2):
   f1 = open(fn1,'r')
   f2 = open(fn2,'r')
   fileOne = f1.readlines()
   fileTwo = f2.readlines()
   f1.close()
   f2.close()
   l = 0
   if len(fileOne)!=len(fileTwo):
      return 'ERROR: The two file size is different'
   for i in fileOne:
      if fileTwo[l] != i:
         return 'ERROR: Line '+str(l)+' is different '+i+' '+fileTwo[l]
      l += 1
   return 'OK'
         

def processdir(dirname):
   ls = os.listdir(dirname)
   cd = False
   for name in ls:
      p = dirname + '/' + name
      if (path.isdir(p)):
         processdir(p)
         cd = True
   if cd:
     return         
   if 'start.py' not in ls:
      print('ERROR no start.py in ' + dirname)     
   else:
      name = 'start.py'
      p = dirname + '/start.py'
      for test in tests:
         testin = dirname + '/' + test + '.in'
         testok = dirname + '/' + test + '.ok'
         if not path.exists(testin):
               print('ERROR: missing '+ testin) 
               continue
         if not path.exists(testok):
               print('ERROR: missing '+ testok) 
               continue
         tmpfname = '/tmp/output'
         call(['bash','-c','cat '+testin +' | '+p + '> '+tmpfname])
         result = compare(tmpfname,testok)
         print(p+' '+result)
         
         
if __name__ == '__main__':
   processdir('2008')
