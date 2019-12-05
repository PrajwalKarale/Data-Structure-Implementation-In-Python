#NOTE:
#Deletion before a given node and after a given node is as same as deletion in a singly linked list

#This will create the node
class Node:
    def __init__(self,data):
        self.data = data    #this will assign value  to the node
        self.next = None    #this will set the address to the next node from current node
class CircularList:
    def __init__(self):
        self.head = None    #this is the start node that helds the address of the first node
    
    #function to insert the node at the end of the list
    def insertend(self):
        data = int(input('Enter the data of the newnode: '))
        newnode = Node(data)    #creating newnode
        if self.head == None:
            self.head = newnode
            newnode.next = self.head
        else:
            current = self.head     #points to the first node
            while current.next != self.head:
                current = current.next
            current.next = newnode
            newnode.next = self.head
        print(f'Node with data {data } inserted successfully!!!')
    
    #delete the starting node
    def delete_beg(self):
        current = self.head
        ptr = current
        while ptr.next != self.head:
            ptr = ptr.next
        ptr.next = current.next
        self.head = ptr.next
        print('Starting node deleted successfully!!!!')
    
    #function to delete the end element in the linked list
    def delete_end(self):
        ptr = self.head     #points to the first node.
        preptr = ptr
        while ptr.next != self.head:
            preptr = ptr
            ptr = ptr.next
        preptr.next = self.head
        print('Last node of the linked list deleted successfully!!')
    
    #function to print the list
    def printlist(self):
        ele = []            #list to display the elements of the linked list
        ptr = self.head     #pointer to the start node.
        while ptr.next != self.head:
            ele.append(ptr.data)
            ptr = ptr.next
        ele.append(ptr.data)
        print(f'The linked list is: {ele}')
    
    #function to count the number of nodes in the list
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

#main function
def main():
    circularlist = CircularList()   #creating object of class CircularList
    print('-----CIRCULAR  LINKED LIST--------')
    while True:
        print('-----MAIN MENU------')
        print('1.INSERT END\n2.DELETE BEG\n3.DELETE END\n4.PRINT LIST\n5.COUNT NODES\n6.EXIT')
        ch = int(input('Enter your choice: '))
        if  ch == 1:
            circularlist.insertend()
        if ch == 2:
            circularlist.delete_beg()
        if ch == 3:
            circularlist.delete_end()
        if ch == 4:
            circularlist.printlist()
        if ch == 5:
            circularlist.count()
        if ch == 6:
            exit()
main()
