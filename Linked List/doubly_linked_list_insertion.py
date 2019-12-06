#class for creating the node
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.start = None   #start is the pointer that points to the first node in the list
    
    #function to insert the node in the beginning
    def insert_beg(self):
        data = int(input('Enter the data of the node: '))
        newnode = Node(data)

        ptr = self.start
        newnode.next = ptr
        ptr.prev = newnode
        self.start = newnode

        print(f'Node with value {data} inserted successfully at the start.')

    #function to insert the node in the end
    def insert_end(self):
        data = int(input('Enter the data of the node: '))
        newnode = Node(data)        #newnode with data is created
        
        #When there is no node present in the list
        if self.start == None:
            self.start = newnode
        else:
            ptr = self.start
            while ptr.next != None:
                ptr = ptr.next
            ptr.next = newnode
            newnode.prev = ptr
        print(f'Node with value {data} inserted successfully.')
    
    #function to insert a node after a given node
    def insert_after(self):
        num = int(input('Enter the value of the node  after which the newnode is to be inserted: '))
        data = int(input('Enter the data of the newnode: '))
        newnode = Node(data)
        ptr = self.start
        while ptr.data != num:
            ptr = ptr.next
        newnode.next = ptr.next
        newnode.prev = ptr
        ptr.next = newnode
        ptr.next.prev = newnode
        print(f'Node with value {data} inserted successfully after node {num}')
    
    #function to insert a node before a given node
    def insert_before(self):
        num = int(input('Enter the value of the node  before which the newnode is to be inserted: '))
        data = int(input('Enter the data of the newnode: '))
        newnode = Node(data)
        ptr = self.start
        while ptr.data != num:
            ptr = ptr.next
        newnode.next = ptr
        newnode.prev = ptr.prev
        ptr.prev.next = newnode
        ptr.prev = newnode
        print(f'Node with value {data} inserted successfully before node {num}')
    
    #function to print the list
    def  printlist(self):
        ele = []                #list to store the elements
        ptr = self.start        #pointer the points to the first node
        if ptr == None:
            print('List is empty')
        else:
            while  ptr.next != None:
                ele.append(ptr.data)
                ptr = ptr.next
            ele.append(ptr.data)
        print(f'Linked list is {ele}')
    #function to count the number of nodes
    def count(self):
        total = 0
        ptr = self.start
        if ptr == None:
            print('Total number of nodes is 0')
        else:
            while ptr != None:
                total += 1
                ptr = ptr.next
        print(f'The total number of nodes in the linked list are: {total}')

def main():
    doublylist = DoublyLinkedList()     #object creation
    while True:
        print('\n')
        print('DOUBLY LINKED LIST')
        print('1.INSERT BEG\n2.INSERT END\n3.INSERT  AFTER\n4.INSERT BEFORE\n5.PRINT LIST\n6.COUNT NODES\n7.EXIT')
        ch = int(input('Enter your choice: '))
        if ch == 1:
            doublylist.insert_beg()
        if ch == 2:
            doublylist.insert_end()
        if ch == 3:
            doublylist.insert_after()
        if ch == 4:
            doublylist.insert_before()
        if ch == 5:
            doublylist.printlist()
        if ch == 6:
            doublylist.count()
        if ch == 7:
            exit()
#main function
main()
