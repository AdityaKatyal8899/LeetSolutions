class STOI:
    def stoi(self, s):
        res = 0
        n = False
        start = 0

        if s[0] == "-":
            n = True
            start = 1
        elif s[0] == "+":
            start = 1

        for i in range(start, len(s)):
            digi = ord(s[i]) - ord("0")
            if digi < 0 or digi > 9:
                return 
            res = (res * 10) + digi

        if n:
            return res
        return -res