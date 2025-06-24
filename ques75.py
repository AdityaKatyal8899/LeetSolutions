nums = [2, 0, 2, 1, 1, 0]
i = 0
j= 0
k = len(nums) - 1

while i <= k:
  if nums[i] == 0:
    nums[j], nums[i] = nums[i], nums[j]

    i += 1
    j += 1
  elif nums[i] == 1:
    i += 1
  
  else:
    nums[j], nums[k] = nums[k], nums[j]
    k -= 1

print(nums)
