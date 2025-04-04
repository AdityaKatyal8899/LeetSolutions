a = [0, 1, 2,2,3,0,4,2]
i = 0
val = 2

for j in range(0, len(a)-1):
    if a[j] != val:
        i += 1
print(i)


