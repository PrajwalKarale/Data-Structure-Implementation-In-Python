class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
    
class Circular_doubly_list:
    def __init__(self):
        self.head = None    #initialising the start pointer to null
    def insert_beg(self):
        data = int(input('Enter the data of the node: '))
        newnode = Node(data)
        ptr = self.head
        while ptr.next != self.head:
            ptr = ptr.next
        ptr.next = newnode
        newnode.prev = ptr
        newnode.next = self.head
        self.head.prev = newnode
        self.head = newnode

    def insert_end(self):
        data = int(input('Enter the data of the node: '))
        #form a newnode
        newnode = Node(data)
        #firstcondition is when there is no node present in the list
        if self.head == None:
            self.head = newnode
            newnode.next = self.head
        else:                       #this is the condition when there are some nodes present in the list 
            ptr = self.head
            while ptr.next != self.head:
                ptr = ptr.next
            ptr.next = newnode
            newnode.prev = ptr
            newnode.next = self.head
            self.head.prev = newnode
    
    def insert_before(self):
        num = int(input('Enter the data of the node before which the newnode is to be inserted: '))
        data = int(input('Enter the data of the node: '))
        newnode = Node(data)
        ptr = self.head
        while ptr.data != num:
            ptr = ptr.next
        newnode.next = ptr
        newnode.prev = ptr.prev
        ptr.prev.next = newnode
        ptr.prev = newnode

    def insert_after(self):
        num = int(input('Enter the data of the node before which the newnode is to be inserted: '))
        data = int(input('Enter the data of the node: '))
        newnode = Node(data)
        ptr = self.head
        while ptr.data != num:
            ptr = ptr.next
        newnode.next = ptr.next
        newnode.prev = ptr
        ptr.next = newnode
        ptr.next.prev = newnode

    def printlist(self):
        ele = []
        ptr = self.head
        while ptr.next != self.head:
            ele.append(ptr.data)
            ptr = ptr.next
        ele.append(ptr.data)
        print(f'The list is:{ele}')
    def countnodes(self):
        pass
def main():
    circular_doubly = Circular_doubly_list()
    while True:
        print('--------MAIN MENU--------')
        print('1.INSERT_BEG\n2.INSERT_END\n3.INSERT_BEFORE\n4.INSERT_AFTER\n5.PRINT_LIST\n6s.EXIT')
        ch = int(input('Enter your choice: '))
        if ch == 1:
            circular_doubly.insert_beg()
        if ch == 2:
            circular_doubly.insert_end()
        if ch == 3:
            circular_doubly.insert_before()
        if ch == 4:
            circular_doubly.insert_after()
        if ch == 5:
            circular_doubly.printlist()
        if ch == 6:
            exit()
main()