

#linkedlist

class Node:
  def __init__(self,data=None,next=None):
    self.data=data
    self.next=next

class Linkedlist:
  def __init__(self):
    self.head=None


  #new node at beginnng
  def insert_at_beginning(self,data):
    newnode=Node(data,self.head)
    self.head=newnode

  #new node at the end
  def insert_at_last(self,data):
    if self.head is None:
      self.head=Node(data,None)
    else:
      itr=self.head
      while itr.next:
       itr=itr.next

      itr.next=Node(data,None)

  #print
  def printll(self):
    if self.head is None:
      print('Linked list is empty')
      return
    
    itr=self.head
    llstr=''
    while itr:
      llstr+=str(itr.data)+'--->'
      itr=itr.next
    
    print(llstr)



if __name__=='__main__':
  ll=Linkedlist()
  ll.insert_at_beginning(50)
  ll.insert_at_beginning(89)
  ll.insert_at_last(0)
  ll.insert_at_last(1)
  ll.printll()
    