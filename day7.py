import math

def day7_task_naive_thought_avg(positionz, force_needed_level = -1):
	# simply calculate the average, that will be the lowest fuel usage
	sum = 0
	for p in positionz:
		sum += p
	avg = sum * 1.0 / len(positionz)
	needed_level = int(round(avg))
	if not force_needed_level == -1:
		needed_level = force_needed_level
	fuel = 0
	for p in positionz:
		fuel += abs(p - needed_level)
	return needed_level, fuel

def day7_trying_least_square(positionz):
	# we still need the avg
	sum = 0
	for p in positionz:
		sum += p
	length = len(positionz) * 1.0
	avg = sum * 1.0 / length
	# now calculate the sum of squares deviating from the avg
	sum_sq = 0.0
	for p in positionz:
		sum_sq += (p * 1.0 - avg) * (p * 1.0 - avg) # we need to minimize this sum_sq somehow
	print("sum_sq -> {}".format(sum_sq))
	print("sqrt(sum_sq) -> {}".format(math.sqrt(sum_sq)))
	print("sqrt(sqrt(sum_sq)) -> {}".format(math.sqrt(math.sqrt(sum_sq))))
	half_forth_root = 0.5 * math.sqrt(math.sqrt(sum_sq))
	print("1/2 root_4 (sum_sq) -> {}".format(half_forth_root))
	root_of_half_root = math.sqrt(0.5 * math.sqrt(sum_sq))
	print("root of 1/2 root(sum_sq) -> {}".format(root_of_half_root))
	print("avg -> {}".format(avg))
	# minus the sum?
	length = len(positionz) * 1.0
	#new_level_float = (avg - sum) / length
	#new_level_float = abs(avg - math.sqrt(math.sqrt(sum_sq)))
	new_level_float = avg - root_of_half_root
	needed_level = int(round(new_level_float))

	fuel = 0
	for p in positionz:
		fuel += abs(p - needed_level)
	return needed_level, fuel

example=[16,1,2,0,4,2,7,1,2,14]
needed_level,fuel = day7_task_naive_thought_avg(example, -1)
print("Naive approach:")
print("needed_level -> {}".format(needed_level))
print("fuel -> {}".format(fuel))

print("\nbut what if I tried level 2?\n")

needed_level_2,fuel_2 = day7_task_naive_thought_avg(example, 2)
print("needed_level -> {}".format(needed_level_2))
print("fuel -> {}".format(fuel_2))

if fuel_2 < fuel:
	print("\n\nFAIL!")
	print("\nProbably I need the least squares method??")
	print("\n\nWill try again")
	needed_level,fuel = day7_trying_least_square(example)
	print("needed_level -> {}".format(needed_level))
	print("fuel -> {}".format(fuel))
