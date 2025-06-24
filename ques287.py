from collections import Counter

def dupli(nums: list[int]) -> int:

  freq = Counter(nums)

  for i in freq:
    if freq[i] > 1:
      return i
    

print(dupli([1, 2, 2]))