from typing import List
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        og = image[sr][sc]

        if og == color:
            return image

        def DFS(row, col):
            if row < 0 or row >= len(image) or col < 0 or col >= len(image[0]):
                return
            if image[row][col] != og:
                return 
            image[row][col] = color

            DFS(row+1, col)
            DFS(row-1, col)
            DFS(row, col+1)
            DFS(row, col-1)

        DFS(sr, sc)
        return image 