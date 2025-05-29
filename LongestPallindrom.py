class Solution:
    def longestPalindrome(self, s: str) -> str:
      # Handle edge cases
      if not s:
          return ""
      if len(s) == 1:
          return s

      def expand_around_center(left: int, right: int) -> str:
          while left >= 0 and right < len(s) and s[left] == s[right]:
              left -= 1
              right += 1
          return s[left + 1:right]

      res = ""

      for mid in range(len(s)):
          # Odd-length palindrome
          substr1 = expand_around_center(mid, mid)
          if len(substr1) > len(res):
              res = substr1

          # Even-length palindrome
          substr2 = expand_around_center(mid, mid + 1)
          if len(substr2) > len(res):
              res = substr2

          # Early exit if we found the full string as a palindrome
          if len(res) == len(s):
              break
      return res

s = Solution()
print(s.longestPalindrome("madamimadam"))  