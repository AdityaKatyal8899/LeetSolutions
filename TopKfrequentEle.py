import heapq
def topKfrequent(nums, k):
  frequency = {}

  for i in nums:
    frequency[i] = frequency.get(i, 0) + 1

  top_k = heapq.nlargest(k, frequency.items(), key = lambda x: x[1])

  return [num for num, frq in top_k]
