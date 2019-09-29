import unittest
from FizzBuzz import *

'''
Unit tests for FizzBuzz script.
I have decided to use build in unittest package because provides very useful assertions.

When I was writing FizzBuzz script I was thinking about testability.
So it is quite easy to add new test because expected results can be False or True only.
The test coverage is quite wide. 
I think tests don not need additional comment
because each test name tells you exactly what is checking.

I do not test negative numbers or 0 because FizzBuzz script always starts iterating from 1

Tests 11 and 12 are checking FizzBuzz behavior in case of passing string instead of integer
'''

class FizzBuzzTest(unittest.TestCase):
	
	def test_01_contain_3_and_devide_3(self):
		self.assertTrue(checFizzBuzz(33,3))
	
	def test_02_contain_3_and_not_devide_3(self):
		self.assertTrue(checFizzBuzz(13,3))
	
	def test_03_not_contain_3_and_not_devide_3(self):
		self.assertFalse(checFizzBuzz(22,3))
	
	def test_04_not_contain_3_and_devide_3(self):
		self.assertTrue(checFizzBuzz(87,3))
	
	def test_05_contain_5_and_devide_3(self):
		self.assertTrue(checFizzBuzz(51,3))
		self.assertTrue(checFizzBuzz(51,5))
	
	def test_06_contain_5_and_not_devide_3(self):
		self.assertFalse(checFizzBuzz(52,3))
		self.assertTrue(checFizzBuzz(52,5))
	
	def test_07_contain_5_and_devide_5(self):
		self.assertTrue(checFizzBuzz(50,5))
	
	def test_08_not_contain_3_and_devide_5(self):
		self.assertTrue(checFizzBuzz(50,5))
	
	def test_09_devide_3_and_devide_5(self):
		self.assertTrue(checFizzBuzz(90,5))
		self.assertTrue(checFizzBuzz(90,3))
	
	def test_10_contain_3_and_devide_5(self):
		self.assertTrue(checFizzBuzz(30,3))
		self.assertTrue(checFizzBuzz(30,5))
	
	def test_11_contain_string(self):
		self.assertFalse(checFizzBuzz("one",3))
	
	def test_12_contain_string_with_3(self):
		self.assertFalse(checFizzBuzz("on3e",3))

if __name__ == '__main__':
	unittest.main()
