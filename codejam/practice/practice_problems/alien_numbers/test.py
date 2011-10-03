#!/usr/bin/python

import start
import unittest

class NumberTest(unittest.TestCase):
	def test_decimalValue(self):
		number = start.Number('0123456789')
		self.assertEqual(1,number.decimalValue('1'))
		self.assertEqual(5,number.decimalValue('5'))
		self.assertEqual(0,number.decimalValue('0'))

		number = start.Number('01')
		self.assertEqual(1,number.decimalValue('1'))

	def test_parse(self):
		number = start.Number('0123456789')
		self.assertEqual(123,number.parse('123'))
		self.assertEqual(0,number.parse('0'))
		self.assertEqual(9999,number.parse('9999'))

		number = start.Number('01')
		self.assertEqual(4,number.parse('100'))
		self.assertEqual(3,number.parse('11'))
	def test_format(self):
		self.assertEqual('10001',start.Number('01',17).format())
		self.assertEqual('ABBBA',start.Number('BA',17).format())
		self.assertEqual('16',start.Number('0123456789',16).format())
		number = start.Number('0123456789',12345678)
		self.assertEqual('12345678',number.format())
	
if __name__ == '__main__':
	unittest.main()


