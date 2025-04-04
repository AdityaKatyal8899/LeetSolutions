def LongPrefix(strs):
    i = 0 
    p = strs[i]

    while i != len(strs) - 1:
        j = 0 
        M = min(len(p), len(strs[i+1]))

        t = ""

        while j < M:
            if p[j] == strs[i+1][j]:
                t += p[j]
                j += 1
            else: 
                break
        p = t
        i += 1
    return p

a = ["dog", "doggy", "doggu"]
print(LongPrefix(a))