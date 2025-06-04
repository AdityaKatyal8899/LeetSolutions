def func(nums):
  forward_hash = {}
  backward_hash = {}
  n = len(nums)
  ans = []

  if n == 1:
    return nums[0]
  if n == 2:
    return [nums[1], nums[0]]
  
  forward_hash[0] = 1
  for i in range(1, n):
      forward_hash[i] = forward_hash[i-1] * nums[i-1]

  backward_hash[n-1] = 1
  for i in range(n-2, -1, -1):
      backward_hash[i] = backward_hash[i+1] * nums[i+1]

  for i in range(n):
    ans.append(forward_hash[i] * backward_hash[i])
      
  return ans


print(func([1,2,3,4]))