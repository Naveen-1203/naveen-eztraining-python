

#creating LL in ascending order
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def printList(self):
        temp=self.head
        if not temp:
            print('list is empty:')
            return
        else:
            print('start:',end=' ')
        while temp:
            print(temp.data,end='->')
            temp=temp.next
        print('end')
    def insert(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        elif self.head.data >=new_node.data:
            new_node.next=self.head
            self.head=new_node
        else:
            current=self.head
            while current.next and new_node.data > current.next.data:
                current= current.next
            new_node.next=current.next

            current.next=new_node
    def delete(self,key):
        if self.head is None:
            print('deletion error: list is empty')
            return
        if self.head.data==key:
            self.head=self.head.next
            return
        current=self.head
        while current:
            if current.data==key:
                break
            previous=current
            current=current.next
        if current is None:
            print('deletion error :key not found')
        else:
            previous.next=current.next
if __name__=='__main__':
    LL=LinkedList()
    print('')
    LL.insert(10)
    LL.insert(12)
    LL.insert(8)
    LL.insert(11)
    LL.insert(10)
    LL.printList()
    LL.delete(12)
    LL.delete(8)
    LL.delete(10)
    LL.printList()
     


import fn
fn.printing()
print(__name__)


print('before functipon')
def f1():
    print('f1')
def f2():
    print('f2')
def f3():
    print('f3')
if __name__=="__main__":
    f1()
    f2()
    f3()
print("name:",__name__)


#DOUBLE LINKED LIST
class Node:
    def __init__(self,data):
        self.data=data
        self.previous=None
        self.next=None
class dll:
    def __init__(self):
        self.head=None
    def display(self):
        if self.head is None:
            print("empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,"<-->",end=" ")
                temp=temp.next
l=dll()
n1=Node(100)
l.head=n1
n2=Node(200)
n2.prev=n1
n1.next=n2
l.display()


#insertion at start
class Node:
    def __init__(self,data):
        self.data=data
        self.previous=None
        self.next=None
class dll:
    def __init__(self):
        self.head=None
    def insert_start(self):
        n=Node(300)
        temp=self.head
        temp.prev=n
        n.next=temp
        self.head=n
    def display(self):
        if self.head is None:
            print('empty')
        else:
            temp=self.head
            while temp:
                print(temp.data,"<-->",end=" ")
                temp=temp.next
l=dll()
n1=Node(100)
l.head=n1
n2=Node(200)
n2.prev=n1
n1.next=n2
l.insert_start()
l.display()


#insertion at end
class Node:
    def __init__(self,data):
        self.data=data
        self.previous=None
        self.next=None
class dll:
    def __init__(self):
        self.head=None

        
    def insert_end(self):
        n=Node(300)
        temp=self.head
        while temp.next is not None:
            temp=temp.next
        temp.next=n
        n.prev=temp

        
    def display(self):
        if self.head is None:
            print('empty')
        else:
            temp=self.head
            while temp:
                print(temp.data,"<-->",end=" ")
                temp=temp.next
l=dll()
n1=Node(100)
l.head=n1
n2=Node(200)
n2.prev=n1
n1.next=n2
l.insert_end()
l.display()

#insertion at position
class Node:
    def __init__(self,data):
        self.data=data
        self.previous=None
        self.next=None
class dll:
    def __init__(self):
        self.head=None

        
    def insert_pos(self,pos):
        n=Node(300)
        temp=self.head
        for i in range(1,pos-1):
            temp=temp.next
        n.prev=temp
        n.next=temp.next
        temp.next.prev=n
        temp.next=n
    
    
        
    def display(self):
        if self.head is None:
            print('empty')
        else:
            temp=self.head
            while temp:
                print(temp.data,"<-->",end=" ")
                temp=temp.next
l=dll()
n1=Node(100)
l.head=n1
n2=Node(200)
n2.prev=n1
n1.next=n2
l.insert_pos(1)
l.display()


#deleting a node at start
class Node:
    def __init__(self,data):
        self.data=data
        self.previous=None
        self.next=None
class dll:
    def __init__(self):
        self.head=None
        
    def delete_beginning(self):
        temp=self.head
        self.head=temp.next
        temp.next=None
    
        
    def display(self):
        if self.head is None:
            print('empty')
        else:
            temp=self.head
            while temp:
                print(temp.data,"<-->",end=" ")
                temp=temp.next
l=dll()
n1=Node(100)
l.head=n1
n2=Node(200)
n2.prev=n1
n1.next=n2
l.delete_beginning()
l.display()

#deleting at end
class Node:
    def __init__(self,data):
        self.data=data
        self.previous=None
        self.next=None
class dll:
    def __init__(self):
        self.head=None
        
    def delete_end(self):
        temp=self.head.next
        prev=self.head
        while temp.next is not None:
            temp=temp.next
            prev=prev.next
        prev.next=None
    
        
    def display(self):
        if self.head is None:
            print('empty')
        else:
            temp=self.head
            while temp:
                print(temp.data,"<-->",end=" ")
                temp=temp.next
l=dll()
n1=Node(100)
l.head=n1
n2=Node(200)
n2.prev=n1
n1.next=n2
n3=Node(300)
n3.prev=n2
n2.next=n3
l.delete_end()
l.display()


#deleting at a particular position

class Node:
    def __init__(self,data):
        self.data=data
        self.previous=None
        self.next=None
class dll:
    def __init__(self):
        self.head=None
        
    def delete_pos(self,pos):
        temp=self.head.next
        prev=self.head
        for i in range(1,pos-1):
            temp=temp.next
            prev=prev.next
        prev.next=temp.next
        temp.next=None
    
        
    def display(self):
        if self.head is None:
            print('empty')
        else:
            temp=self.head
            while temp:
                print(temp.data,"<-->",end=" ")
                temp=temp.next
l=dll()
n1=Node(100)
l.head=n1
n2=Node(200)
n2.prev=n1
n1.next=n2
l.delete_pos(1)
l.display()


#circular linked list
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class CreateList():
    def __init__(self):
        self.head=Node(None)
        self.tail=Node(None)
        self.head.next=self.tail
        self.tail.next=self.head
    def add(self,data):
        newNode=Node(data)
        if self.head.data is None:
            self.head=newNode
            self.tail=newNode
            newNode.next=self.head
        else:
            self.tail.next=newNode
            self.tail=newNode
            self.tail.next=self.head
    def display(self):
        current=self.head
        if self.head is None:
            print('list is empty')
            return
        else:
            print('nodes of the circular linked list:')
            print(current.data,"-->")
            while (current.next !=self.head):
                current=current.next
                print(current.data,"-->")

class cll():
    cl=CreateList()
    cl.add("s")
    cl.add("m")
    cl.add("i")
    cl.add("l")
    cl.add("e")
    cl.display()
    
