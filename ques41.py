# def adder(arr):
#   result = 0
#   for i in range (0, len(arr)):
#     if arr[i] > 0:
#       result += arr[i]
#   return result


# def missing(arr, n):
#   real_sum = adder(arr)
#   unreal_sum = n*(n+1) // 2

#   return unreal_sum - real_sum

def firt_missing_posi(arr):
  nums = {}

  for i, num in enumerate(arr):
    if num > 0:
      nums[num] = i

  i = 1
  while True:
    if i in nums:
        i += 1
    return i
  

li = [1, 2, 0]

print(firt_missing_posi(li))


