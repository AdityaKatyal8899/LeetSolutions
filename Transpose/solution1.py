from typing import List
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        n = len(matrix)
        #For non-square matrix

        rows, cols = len(matrix), len(matrix[0])
        l1= [[0 for i in range(rows)] for j in range(cols)]

        for i in range(rows):
          for j in range(cols):
            
              l1[i][j], l1[j][i] = matrix[i][j], matrix[j][i]
            
        return l1
    

#Run time: 55ms, beats 1.87%
#Space: 29.4MB, beats 6.14%