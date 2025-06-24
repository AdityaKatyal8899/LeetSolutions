class Stack:
  def __init__(self):
    self.arr = []

  def print(self):
    print(self.arr)

  def push(self, n):
   self.arr.append(n)
  
  def is_empty(self):
    if len(self.arr) == 0:
      return True
    return False
  
  def top(self):
    if self.is_empty():
      return None
    else:
      return self.arr[-1] #Start = -1 that is in reverse order
    
  def pop(self):
    if not self.is_empty():
      return self.arr.pop()
    else:
      print("Empty")
      return None
    
  def is_full(self):
    if not self.is_empty():
      print("Stack Full")
    else:
      print("Not Full")
  def size(self):
    return len(self.arr)

class Solution(Stack):
    def isValid(self, s):
        for char in s:
            if char in [")", "]", "}"]:
                if self.is_empty():
                    return False
                top = self.pop()
                if (char == ")" and top != "(") or \
                   (char == "]" and top != "[") or \
                   (char == "}" and top != "{"):
                    return False
            else:
                self.push(char)
        return self.is_empty() 
    
    