class Solution:
  def plusOne(self, digits: List[int]) -> List[int]:
        int_of_list = int("".join(map(str, digits)))
        incrementing_by_one = int_of_list + 1
        result = []

        for i in range(0, len(str(incrementing_by_one))):
            result.append(int(str(incrementing_by_one)[i]))
        return result
        
solution = Solution()

print(solution.plusOne([1,2,3]))
print(solution.plusOne([3,4,4,9]))