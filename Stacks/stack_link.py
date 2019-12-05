#Here we will be implementing stack data structure using python
#We will be implenting stack using linked list in python

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class StackLink:
    def __init__(self):
        self.start = None
    
    #function to push element in the stack
    def push(self):
        data = int(input('Enter the value of the node: '))
        #to create a newnode
        newnode = Node(data)
        if self.start == None:
            newnode.next = None
            self.start = newnode
        else:
            newnode.next = self.start
            self.start = newnode
        print('Element inserted in the stack successfully')

    #function to pop element from stack
    def pop(self):
        ptr = self.start
        preptr = ptr        #this is to store the  node that is to be popped
        if ptr == None:
            print('No element present in the stack')
        else:
            self.start = ptr.next
            data1 = preptr.data
            print(f'Element popped is {data1}')

    #function to see the top element present
    def peep(self):
        ptr = self.start
        if ptr == None:
            print('No element is  present....')
        else:
            data1 = ptr.data
            print(f'Vale of the top node is : {data1}')

    #function to count the total number of nodes:
    def display(self):
        ele = []
        ptr = self.start
        while ptr != None:
            ele.append(ptr.data)
            ptr = ptr.next
        print(ele)
def main():
    stacklink = StackLink()
    while True:
        print('---STACK USING LINKED LIST----')
        print('1.PUSH\n2.POP\n3.PEEP\n4.DISPLAY\n5.EXIT')
        ch = int(input('Enter your choice: '))
        if ch == 1:
            stacklink.push()
        if ch == 2:
            stacklink.pop()
        if ch == 3:
            stacklink.peep()
        if ch == 4:
            stacklink.display()
        if ch == 5:
            exit()
main()
