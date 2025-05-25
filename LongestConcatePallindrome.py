class Solution:
    def longestPalindrome(self, l: list[str]) -> int:
        count = {}
        length = 0
        used_middle = False

        for i in l:
            count[i] = count.get(i, 0) + 1

        for i in list(count.keys()):
            rev = i[::-1]

            if i == rev:
                pairs = count[i] // 2
                length += pairs * 4
                count[i] -= pairs * 2

                if not used_middle and count[i] > 0:
                    length += 2
                    used_middle = True

            elif rev in count:
                pairs = min(count[i], count[rev])
                length += pairs * 4
                count[i] -= pairs
                count[rev] -= pairs

        return length

s = Solution()

l = ["lc", "cl", "gg"]

print(s.longestPalindrome(l))