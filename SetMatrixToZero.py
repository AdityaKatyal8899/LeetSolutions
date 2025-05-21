class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        if matrix == None or matrix[0] == None:
            return
        TBZ_rows = set()
        TBZ_columns = set()

        rows = len(matrix)
        columns = len(matrix[0])

        i = 0
        while i < rows:
            j = 0
            while j < columns:
                if matrix[i][j] == 0:
                    TBZ_rows.add(i)
                    TBZ_columns.add(j)
                j += 1
            i += 1
        for i in range(0, rows):
            for j in range(0, columns):

                if i in TBZ_rows or j in TBZ_columns:
                    matrix[i][j] = 0
solution = Solution()    
matrix = [[1,1,1],[1,0,1],[1,1,1]]
Solution().setZeroes(matrix)
print(matrix)
