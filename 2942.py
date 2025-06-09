from typing import List
class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        result = []
        for i, j in enumerate(words):
            if x in j:
                result.append(i)
        return result
                
    

s = Solution()
words = ["leet", "code"]

print(s.findWordsContaining(words, x = "e"))