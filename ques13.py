
def RtoI(s):
    pre_defs = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    i = len(s) -1

    total = 0 
    prev = 0
    
    while (i != -1):
      value = pre_defs[s[i]]

      if value < prev:
        total -= value
        
      else:
        total += value
        prev = value

      i -= 1
    return total


print(RtoI("MCMXCIV"))