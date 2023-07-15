# 1. create a node class
class node:
    def __init__(self,data):
        self.data = data
        self.next = None

# 2. create a linked list
class linkedList:
    def __init__(self):
        self.head = None
        
# create the function for printing the output values
    def output(self):
        temp = self.head
        while (temp != None):
            print(temp.data,end="-->")
            temp = temp.next

# object creation and setting data to the node
list = linkedList()       # creating object
first = node(10)          # create and initialize the value to node class
second = node(20)
third = node(30)

# setting the address to the node
list.head = first
first.next = second
second.next = third

# call the output function
list.output()
# aaaaaa
