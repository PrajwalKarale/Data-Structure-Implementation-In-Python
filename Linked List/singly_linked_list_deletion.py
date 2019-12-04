class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def insert_end(self):
        data = int(input('Enter the data to be inserted: '))
        #creation of newnode:
        newnode = Node(data)
        #condition when the list is empty
        if self.head == None:
            self.head = newnode
        #condition when there are elements present in the list
        else:
            #creating a pointer to traverse the list
            current = self.head
            while current.next != None:
                current = current.next
            current.next = newnode
        print(f'{data} Element is inserted successfully:')
    #to delete the starting node
    def delete_start(self):
        if self.head == None:
            print('List is empty:')
        else:
            self.head = self.head.next
            print('First element is successfully deleted')
    #to delete the ending node:
    def delete_end(self):
        ptr = self.head
        preptr = ptr
        while ptr.next != None:
             preptr = ptr
             ptr = ptr.next
        preptr.next = None
        print('Last Element deleted successfully!!')
    #to delete the node after a given value
    def delete_after(self):
        num = int(input('Enter the value of the node after which the data is to be deleted: '))
        ptr = self.head
        preptr = ptr
        while preptr.data != num:
            preptr = ptr
            ptr = ptr.next
        preptr.next = ptr.next
        print(f'Element after {num} is deleted successfully!!!!!')
    #to count the number of nodes in the list
    def count(self):
        total = 0
        #this will point to the starting node
        current = self.head
        if current == None:
            print('THE LIST IS EMPTY!!!!')
        while current != None:
            total += 1
            current = current.next
        print(f'THE TOTAL NUMBER OF NODES IN LIST ARE: {total}')
    #to print the list
    def printlist(self):
        #initializing empty list
        ele = []
        #pointer to the starting element
        current = self.head
        while current != None:
            ele.append(current.data)
            current = current.next
        print(f'THE GIVEN LIST IS: {ele}')
def main():
    linklist = LinkedList()
    print('DELETION IN LINKED LIST')
    while True:
        print('-------MAIN MENU-------')
        print('1.INSERT END\n2.DELETION IN END\n3.DELETION IN START\n4.DELETION AFTER A GIVEN ELEMEN\n5.PRINT LIST\n6.COUNT NODES\n7.EXIT')
        ch = int(input('Enter the choice: '))
        if ch == 1:
            linklist.insert_end()
        if ch == 2:
            linklist.delete_end()
        if ch == 3:
            linklist.delete_start()
        if ch == 4:
            linklist.delete_after()
        if ch == 5:
            linklist.printlist()
        if ch == 6:
            linklist.count()
        if ch == 7:
            #exiting the program
            exit()
main()
