nums = [2, 0, 2, 1, 1, 0]

final = [i for i in nums if i == 0] + [i for i in nums if i == 1] + [i for i in nums if i == 2]

print(final)
