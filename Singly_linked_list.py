class Node:
  def __init__(self, data, next):
    self.data = data
    self.next = next

class LL:
  def __init__(self):
    self.head = None             #Represent the head or the initilaizer of the list 

  def empty(self):
    return self.head is None      #self.head == None both are the same
  
  def strt_insert(self, data):
    new = Node(data, self.head)             #Createing a Node new
    self.head = new                       #Intializing new as head node
    #print(f"Inserted {new.data} at the start")

  def end_insert(self, data):
    new = Node(data, None)
    if not self.empty():
      temp = self.head
      while temp.next is not None:      #temp.next != None both are the same
        temp = temp.next            #Jumping to next till last node is found
      temp.next = new               #Assign the refernce of new to last node founded
    else:
      self.head = new               #if list is empty, directly assigning new as head
    #print(f"Inserted {new.data} at last")
  
  def searcher(self, n):
    temp = self.head

    while temp is not None:
      if temp.data == n:
        return temp
      temp = temp.next
    return None
  
  def after_insert(self, af, n):
    yes = self.searcher(af)

    if yes is not None:
      new = Node(n, yes.next)
      yes.next = new
    else:
      print(f"No such element{af} Found")

  def printer(self):
    current = self.head
    while current is not None:
      print(f"{current.data}", end = " ")
      current = current.next
    print()

mine = LL()
n = int(input("Enter no. of elements in the List: "))

for i in range(n):
  a = int(input(f"Enter for {i}th index: "))
  mine.end_insert(a)
mine.printer()