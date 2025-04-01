#Two Pointers approach
#This approach is used to find two numbers in a sorted array that add up to a specific target number.
#The algorithm uses two pointers, one starting at the beginning of the array and the other at the end.
a = [3, 2, 11, 18]
a.sort()
target = 20

#Declare left and right pointers to trverse accordingly
left = 0
right = len(a) - 1

while left <= right:
    b = a[left] + a[right]

    if target < b:
        right -= 1
    elif target > b:
        left += 1
    else: 
        print(f"[{left}, {right}]") 
        break
if left > right:
    print("No such pair found")