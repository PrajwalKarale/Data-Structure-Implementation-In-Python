#defining the structure of the node
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.start = None   #initializing the start pointer
    
    #function to insert node
    def insert_end(self):
        data = int(input('Enter the data of the newnode: '))
        #creation of the newnode
        newnode = Node(data)
        #first condition is when there are no existing node:
        if  self.start == None:
            self.start = newnode
        #condition when there are nodes present in the list
        else:
            ptr = self.start    #this is the pointer to the starting node
            while ptr.next != None:
                ptr = ptr.next
            ptr.next = newnode
            newnode.prev = ptr
    
    #function to delete in the beginning
    def insert_beg(self):
        ptr = self.start
        data = ptr.data
        self.start = self.start.next
        self.start.prev = None
        print(f'The node in the beginning having data {data}')

    #function to delete the node at the end
    def delete_end(self):
        ptr = self.start        #ptr is the pointer pointing to the first node
        preptr = ptr            #preptr is also the pointer pointing to the fisrtnode of the list
        while ptr.next != None:
            preptr = ptr
            ptr = ptr.next
        data = ptr.data
        preptr.next = None
        print(f'The node at the end with data {data} is deleted')

    #function to delete the node  before a given node
    def delete_before(self):
        num = int(input('Enter the value of the node whose before node is to be deleted: '))
        ptr = self.start
        while ptr.data != num:
            ptr = ptr.next
        temp = ptr.prev
        temp.prev.next = ptr
        ptr.prev = temp.prev
        print(f'Node deleted successfuly!!!!...')
    
    #function to delete the node after a given node
    def delete_after(self):
        num = int(input('Enter the value of the node whose afterwards node is to be deleted: '))
        ptr = self.start
        while ptr.data != num:
            ptr = ptr.next
        temp = ptr.next
        data1 = temp.data
        ptr.next = temp.next
        temp.next.prev = ptr
        print(f'After: {data1} -> after the node Num:{num} is deleted')
    #function to printlist
    def printlist(self):
        ele = []
        ptr = self.start
        while ptr.next != None:
            ele.append(ptr.data)
            ptr = ptr.next
        ele.append(ptr.data)
        print(f'The doubly linked list is: {ele}')
    #function to count the nodes
    def count(self):
        total = 0
        ptr = self.start
        while ptr.next != None:
            total += 1
            ptr = ptr.next
        total += 1
        print(f'The total number of nodes in the doubly linked list are : {total}')
    
#main function
def main():
    doublylist = DoublyLinkedList()
    while True:
        print('--DOUBLY LINKED LIST--')
        print('1.INSERT END\n2.DELETE BEG\n3.DELETE END\n4.DELETE AFTER\n5.DELETE BEFORE\n6.PRINT LIST\n7.COUNT NODES\n8.EXIT')
        ch = int(input('Enter your choice: '))
        if ch == 1:
            doublylist.insert_end()
        if ch == 2:
            doublylist.insert_beg()
        if ch == 3:
            doublylist.delete_end()
        if ch == 4:
            doublylist.delete_after()
        if ch == 5:
            doublylist.delete_before()
        if ch == 6:
            doublylist.printlist()
        if ch == 7:
            doublylist.count()
        if ch == 8:
            exit()
main()