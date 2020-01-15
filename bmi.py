class BMI:

	@staticmethod
	def BMI_Calcul(high, weigth):
		result = weigth/(high**2)
		return round(result, 2)

	@staticmethod
	def result_BMI(bmi):

		if bmi < 18.5:
			return "Underweight"

		if bmi >= 18.5 & bmi < 25:
			return "Normal"

		if bmi >= 25 & bmi < 30:
			return "Overweight"

		if bmi >= 30 & bmi < 35:
			return "Obese class I"

		if bmi >= 35 & bmi < 40:
			return "Obese class II"

		if bmi >= 40:
			return "Obese class III"



#assignment11
# TDD_sce
# TDD_sce
