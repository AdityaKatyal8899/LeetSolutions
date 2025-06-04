def stairs(n):
  i, j = 1,1 

  for k in range(n-1):
    i, j = i, j+1
  return j

print(stairs(4))