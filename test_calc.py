import unittest
import calc

class testAdd(unittest.TestCase):
	def test_add(self):
		self.assertEqual(calc.addition(10,5),15)
		self.assertEqual(calc.substraction(5,10),-5)
		self.assertEqual(calc.multiplication(5,10),50)
		self.assertEqual(calc.division(5,10),.5)
if __name__ == '__main__':
	unittest.main()

