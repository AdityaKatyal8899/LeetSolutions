def bitofonecount(n):
  ans = []

  for i in range(n+1):
    count = 0
    temp = i

    while temp > 0:
      if temp%2 == 1:
        count += 1
        
      temp //= 2
    ans.append(count)  
  
  return ans


print(bitofonecount(5))