pre_rom = {
   1000: "M",
   900: "CM",
   500: "D", 
   400: "CD",
   100: "C",
   90: "XC",
   50:"L",
   40: "XL",
   10: "X",
   5: "V",
   4: "IV",
   1: "I"
}


def intToRoman(self, num: int) -> str:
  res = "" 
  for nums in sorted(pre_rom.keys(), reverse=True):
    while num >= nums:
        res += pre_rom[nums]
        a -= nums
  return res


