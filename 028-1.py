d1_last = 14
d2_last =  10
total = 1 + d1_last + d2_last
side_len = 5
perimeter  = 4 * (side_len - 1)

# print(f"for a s={side_len} the diagonal sum is {total}")
while side_len <= 1001:
	d1_last += perimeter * 2
	d2_last += perimeter * 2
	total += d1_last + d2_last
	print(f"for a s={side_len} the diagonal sum is {total}")
	side_len += 2
	perimeter  = 4 * (side_len - 1)

print(f"\n\n\nthe total is {total}")