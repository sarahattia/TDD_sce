class BMI:

	def BMI_Calcul(high, weigth):
		return weigth//(high**2)

	def result_BMI(high, weigth):
		x = BMI.BMI_Calcul(high, weigth)

		if x < 18:
			return "Underweight"

		if x >= 18 and x < 25:
			return "Normal"

		if x >= 25 and x < 30:
			return "Overweight"

		if x >= 30.0 and x < 35:
			return "Obese class I"

		if x >= 35 and x < 40:
			return "Obese class II"

		if x >= 40:
			return "Obese class III"





print(BMI.result_BMI(1.6, 52))
# assignment11
