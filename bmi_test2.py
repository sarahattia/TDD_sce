Ximport unittest
from src.bmi import BMI


class BMITest(unittest.TestCase):
    def test_result_BMI(self):
        # stub
        bmi = [18, 20.5, 26, 30, 37.56, 45]

        r = []

        # expected result
        e = ["Underweight", "Normal", "Overweight", "Obese class I", "Obese class II", "Obese class III"]

        for i in bmi:
            # fonction verification
            for j in r:
                j = BMI.result_BMI(i)

            # verification
        for k in e:
            for j in r:
                self.assertEqual(j, k)
                print("")


if __name__ == '__main__':
    unittest.main()
