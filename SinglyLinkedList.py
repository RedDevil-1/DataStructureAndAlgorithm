class Node:
    data=None
    next_node=None
    
    def __init__(self, data):
        self.data=data
    
    def __repr__(self):
        return "Node value is > %s" % self.data


class LinkedList:

    #defining self
    def __init__(self):
        self.head=None
    
    #get size of the linked list
    def size(self):
        count=0
        current=self.head
        while current:
            count+=1
            current=current.next_node
        return count

    #add function for adding data
    def add(self, data):
        n1=Node(data)
        if self.head==None:
            self.head=n1
        else:
            n1.next_node=self.head
            self.head=n1 
    
    #remove element from the linked list using the element
    def element_remove(self, element):
        current=self.head
        previous=None
        while current:
            if current.data==element and current==self.head:
                self.head=current.next_node
                return True
            elif current.data==element:
                previous.next_node=current.next_node
                return True
            previous=current
            current=current.next_node
        return "Not found"

    #removing by index
    def index_remove(self,idx):
        count=1
        current=self.head
        prev=None
        while current and count<=idx:
            if idx==1:
                self.head=current.next_node
                return True
            if count==idx:
                prev.next_node=current.next_node
                return True
            prev=current
            current=current.next_node
            count+=1
        return False
    
    #search by index
    def index_search(self, index):
        count=1
        current=self.head
        while current and count<=index:
            if index==1:
                return self.head
            elif count==index:
                return current
            count+=1
            current=current.next_node
    
    #search by value
    def value_search(self,value):
        current=self.head
        while current:
            if current.data==value:
                return True
            current=current.next_node
        return False
    
    #insert at index
    def index_insert(self, value, idx):
        count=1
        current=self.head
        prev=None
        n=Node(value)
        while current and count<=idx:
            if idx==1:
                LinkedList().add(value)
                return LinkedList()
            elif count==idx:
                prev.next_node=n
                n.next_node=current
                return 'Insertion completed'
            prev=current
            current=current.next_node
            count+=1
        return 'Index greater than link size or false value inserted'
        
    #defning __repr__ function for better visualization
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


