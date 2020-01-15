import unittest
from src.bmi import BMI


class BMITest(unittest.TestCase):
	def test_BMI_Calcul(self):
		#stub
		w = 52
		h = 1.60

		#expected result
		e = 20.31

		#action
		r = BMI.BMI_Calcul(1.60, 52)

		#expect/assert
		self.assertEqual(r, e)

if __name__ == '__main__':
	unittest.main()
