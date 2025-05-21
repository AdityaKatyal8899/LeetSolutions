s = "ab "
i = len(s) - 1
res = ""

while s[i] == " ":
  i -= 1

while s[i] != " " and i >= 0:
  res += s[i]
  i -= 1
  
print(len(res[::-1]))
