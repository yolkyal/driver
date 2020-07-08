import unittest
import math
import trig_utils


class TestTrigUtils(unittest.TestCase):
	def testCalcPoint(self):
		point = (100, 200)
		angle = math.pi / 4
		magnitude = 10

		expected_result_x = point[0] + magnitude * math.cos(angle)
		expected_result_y = point[1] + magnitude * math.sin(angle)

		result = trig_utils.calc_point(point, angle, magnitude)

		self.assertEqual(result, (expected_result_x, expected_result_y))

	def testCalcMidPoint(self):
		point = (100, 200)
		angle = math.pi / 4
		magnitude = 10

		expected_result1_x = point[0] + magnitude * 0.5 * math.cos(angle)
		expected_result1_y = point[1] + magnitude * 0.5 * math.sin(angle)

		expected_result2_x = point[0] - magnitude * 0.5 * math.cos(angle)
		expected_result2_y = point[1] - magnitude * 0.5 * math.sin(angle)

		result = trig_utils.calc_mid_point(point, angle, magnitude)

		self.assertEqual(result, ((expected_result1_x, expected_result1_y), (expected_result2_x, expected_result2_y)))

if __name__ == '__main__':
	unittest.main()