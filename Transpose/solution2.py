class Solution:
  def transpose(self, l):
    col = len(l[0])
    row = len(l)

    if not all(len(row) == col for row in l):
      return 
      
        
    if col == 0:
      return [[]]
    
    if row == col:
      for i in range(row):
        for j in range(i+1, col):
          l[i][j], l[j][i] = l[j][i], l[i][j]
      return l

    else:
      l1 = [[l[i][j] for i in range(row)] for j in range(col)]
      return l1
  

#Run time: 0ms, beats 100%
#Space: 18.46MB, beats 69.47%