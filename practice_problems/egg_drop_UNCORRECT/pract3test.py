#!/usr/bin/python

import unittest
from pract3 import EggBreak

class  Pract3TestCase(unittest.TestCase):
    
    def testMaxLevel(self):
        self.assertEquals(7, EggBreak(3,3,3).maxLevel())
        self.assertEquals(25, EggBreak(7,5,3).maxLevel())
        self.assertEquals(22, EggBreak(3,20,3).maxLevel())
        self.assertEquals(15,EggBreak(4,4,4).maxLevel())
    def testMinTry(self):
        self.assertEquals(2, EggBreak(3,3,3).minTry())
        self.assertEquals(3, EggBreak(7,5,3).minTry())
        self.assertEquals(7, EggBreak(15,5,2).minTry())
        self.assertEquals(2, EggBreak(3,3,1).minTry())
    def testMinBreak(self):
        self.assertEquals(1, EggBreak(3,3,3).minBreak())
        self.assertEquals(2, EggBreak(7,5,3).minBreak())
        self.assertEquals(1, EggBreak(3,3,1).minBreak())
        self.assertEquals(2, EggBreak(7,5,2).minBreak())
        

if __name__ == '__main__':
    unittest.main()

