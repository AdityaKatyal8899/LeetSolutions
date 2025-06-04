def func(nums):
  n = len(nums)
  forward = [1] * n
  backward = [1] * n
  
  ans = [1] * n

  if n == 1:
    return nums[0]
  if n == 2:
    return [nums[1], nums[0]]
  
  for i in range(1, n):
      forward[i] = forward[i-1] * nums[i-1]

  
  for i in range(n-2, -1, -1):
      backward[i] = backward[i+1] * nums[i+1]

  for i in range(n):
    ans[i] = (forward[i] * backward[i])
      
  return ans


print(func([1,2,3,4]))