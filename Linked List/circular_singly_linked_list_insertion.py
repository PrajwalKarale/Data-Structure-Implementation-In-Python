#this is used to create newnode
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class CircularList:
    def __init__(self):
        self.head = None
    def insert_beg(self):
        data = int(input('Enter the data of the node: '))
        newnode = Node(data)
        ptr = self.head
        while ptr.next != self.head:
            ptr = ptr.next
        newnode.next = self.head
        ptr.next = newnode
        self.head = newnode
        print(f'Element {data} is inserted in the beginning successfully!!')
    def insert_end(self):
        data = int(input('Enter the data of the node: '))
        newnode = Node(data)
        print(f'Node with value {data} created successfully!!!')
        if self.head == None:
            self.head = newnode
            newnode.next = self.head
        else:
            #this will act as a pointer to the first node
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = newnode
            newnode.next = self.head
        print(f'Node with value {data} inserted successfully')
    #for inserting the given node after a certain node
    def insert_after(self):
        num = int(input('Enter the value of the node after which the new node is to be inserted: '))
        data = int(input('Enter the data of the new node: '))
        #creating newnode
        newnode = Node(data)
        ptr = self.head
        preptr = ptr
        while preptr.data != num:
            preptr = ptr
            ptr = ptr.next
        preptr.next = newnode
        newnode.next = ptr
        print(f'Element {data} is inserted successfully after {num}')
    #for inserting the given node before a certain node
    def insert_before(self):
        num = int(input('Enter the value of the node before which the new node is to be inserted: '))
        data = int(input('Enter the data of the new node: '))
        #creating newnode
        newnode = Node(data)
        ptr = self.head
        preptr = ptr
        while ptr.data != num:
            preptr = ptr
            ptr = ptr.next
        preptr.next = newnode
        newnode.next = ptr
        print(f'Element {data} is inserted successfully before {num}')
    def printlist(self):
        ele = []
        #creates a pointer to the starting node
        current = self.head
        if current == None:
            print('The list is empty!!')
        else:
            while current.next != self.head:
                ele.append(current.data)
                current = current.next
            ele.append(current.data)
        print(ele)
    def count(self):
        total = 0
        current = self.head
        if current == None:
            print('The list is empty!')
        else:
            while current.next != self.head:
                total += 1
                current = current.next
            total += 1
        print(f'The total number of nodes in the list is: {total}')
def main():
    circularlink = CircularList()
    print('.......CIRCULAR LINKED LIST.........')
    while True:
        print('------MAIN MENU------')
        print('1.INSERT BEG\n2.INSERT END\n3.INSERT_AFTER\n4.INSERT_BEFORE\n5.PRINTLIST\n6.COUNT NODES\n7.EXIT')
        ch = int(input('Enter your choice: '))
        if ch == 1:
            circularlink.insert_beg()
        if ch == 2:
            circularlink.insert_end()
        if ch == 3:
            circularlink.insert_after()
        if ch == 4:
            circularlink.insert_before()
        if ch == 5:
            circularlink.printlist()
        if ch == 6:
            circularlink.count()
        if ch == 7:
            exit()
main()
