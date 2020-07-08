import math

def calc_point(point, angle, magnitude):
	return (point[0] + magnitude * math.cos(angle), point[1] + magnitude * math.sin(angle))

def calc_mid_point(point, angle, magnitude):
	return (calc_point(point, angle, magnitude * 0.5), calc_point(point, angle, magnitude * -0.5))