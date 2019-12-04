class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    #insertion in end
    def insert_end(self):
        data = int(input('Enter the data to be appended: '))
        newnode = Node(data)
        current = self.head
        if self.head == None:
            self.head = newnode
        else:
            while current.next != None:
                current = current.next
            current.next = newnode
        print('Insertion in end is successfull: ')
    #insertion after a given element
    def insert_after(self):
        num = int(input('Enter the number after which the data is to be inserted: '))
        data = int(input('Enter the data to be inserted: '))
        #creating new node
        newnode = Node(data)
        ptr = self.head
        preptr = ptr
        while preptr.data != num:
            preptr = ptr
            ptr = ptr.next
        preptr.next = newnode
        newnode.next = ptr
        print('INSERTION AFTER A GIVEN ELEMENT SUCCESSFULL: ')
    def insert_before(self):
        num = int(input('Enter the numbere before which the data is to be inserted: '))
        data = int(input('Enter the data to be inserted: '))
        #creating new node
        newnode = Node(data)
        ptr = self.head
        preptr = ptr
        while ptr.data != num:
            preptr = ptr
            ptr = ptr.next
        preptr.next = newnode
        newnode.next = ptr
        print('INSERTION BEFORE A GIVEN ELEMENT IS SUCCESSFULL: ')
    #print the list
    def print(self):
        ele = []
        current = self.head
        while current != None:
            ele.append(current.data)
            current = current.next
        print(ele)
    #counting the total number of nodes in the list
    def total(self):
        total = 0
        current = self.head
        while current != None:
            total += 1
            current = current.next
        return total
def main():
    #creating object of the class LinkedList
    linklist = LinkedList()
    while True:
        print('----MAIN MENU----')
        print('1.INSERT_END\n2.INSERT_AFTER_NUM\n3.INSERT_BEFORE_NUM\n4.PRINT\n5.TOTAL NODES\n6.EXIT')
        ch = int(input('Enter your choice:'))
        if ch == 1:
            linklist.insert_end()
        if ch == 2:
            linklist.insert_after()
        if ch == 3:
            linklist.insert_before()
        if ch == 4:
            linklist.print()
        if ch == 5:
            count = linklist.total()
            print('The total number of nodes is: ',count)
        if ch == 7:
            exit()
main()
