import math 

pi = math.pi

r = 0
h = 100
vol = 0
g = 9.81
v = 20
t = 0
area_prev = 0
# h = h0 - 0.5 * g * t^2

t = 0
while h >= 0:
	t = math.sqrt((100 - h) / g)
	area = 2 * pi * v * t
	vol += (area - area_prev) * h
	area_prev = area
	h -= 0.00001

print(vol)