class Node:

    '''
        Creating a node value to be inserted into the linked list
    '''

    data=None
    next_node=None
    prev_node=None

    def __init__(self, data):
        self.data=data
    
    def __repr__(self):
        return "Node value is %s" % self.data 

class DLinkedList:
    '''
    Creating a doubly linked list in which we will be
     able to traverse from either ends
    '''

    def __init__(self):
        self.head=None
    
    #adding new node values
    def add(self,data):
        n=Node(data)
        if self.head==None:
            self.head=n
        else:
            self.head.prev_node=n
            n.next_node=self.head
            self.head=n

        return n

    #inserting into the list
    def insert(self,data,idx):
        count=0
        current=self.head
        
        n=Node(data)
        if idx==0:
            self.add(n)
        else:
            while current and count<idx:
                if count==idx-1:
                    current.prev_node.next_node=n
                    n.prev_node=current.prev_node
                    current.prev_node=n
                    n.next_node=current
                    return "Insertion Successful"
                current=current.next_node
                count+=1
                    


    #checking if the linked list is empty
    def is_empty(self):
        return self.head==None

    #checking the size of the linked list
    def size(self):
        count=0
        current=self.head
        while current:
            count+=1
            current=current.next_node
        return count

    #visualitaion of the linked list
    def __repr__(self):
        l1=[]
        current=self.head
        while current:
            if current==self.head:
                l1.append(['Head is: %s' % current.data]) 
            elif current.next_node==None:
                l1.append(['Tail is: %s' % current.data])
            else:
                l1.append([current.data])
                
            current=current.next_node
        return '-> '.join(str(element) for element in l1)



l=DLinkedList()
l.add(10)
l.add(20)
l.add(30)
a=l.add(40)
b=l.add(50)
c=l.add(56)
print(l)