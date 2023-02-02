class node:
    def __init__(self,data):
        self.data = data
        self.next = None

class linkedList:
    def __init__(self):
        self.head = None

 # Add the value at the begining:
    def addBegin(self,data):
        new_node = node(data)
        new_node.next = self.head
        self.head = new_node

 # Add the element at the end:
    def addEnd(self,data):
        new_node = node(data)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node

# Add the element or node after the given node:
    def addAfter(self, data, x):
        temp = self.head
        while temp is not None:  # check the cdn for not having the given value
            if temp.data == x:   # check the cdn for given value
                break
            temp = temp.next

        if temp is None:
            print("'", x, "' value is not there.")
        else:    # code for inserting the new element after the given node
            newNode = node(data)
            newNode.next = temp.next
            temp.next = newNode

# Add the node before the given node
    def addBefore(self, data, x):
        if self.head is None:
            print("linked list is empty")
            return
        if self.head.data == x:
            newNode = node(data)
            newNode.next = self.head
            self.head = newNode
            return

        temp = self.head
        while temp.next is not None:
            if temp.next.data == x:
                break
            temp = temp.next
        if temp.next is None:
            print("The given node not found")
        else:
            newNode = node(data)
            newNode.next = temp.next
            temp.next = newNode

# Add the node to the empty linkedList
    def addEmpty(self,data):
        if self.head is not None:
            print("Linked lst is not empty")
        else:
            new_node = node(data)
            self.head = new_node

# Removing the first node:
    def remFirst(self):
        if self.head is None:
            print("list is empty")
        else:
            self.head = self.head.next

# Remove the last node
    def remLast(self):
        if self.head is None:
            print("list is  empty")
        elif self.head.next is None:  # check whether the list contains only one node
            self.head = None
        else:
            temp = self.head
            while temp.next.next is not None:  # check the next node reference is null
                temp = temp.next
            temp.next = None

# Remove the node by its data
    def delNode(self,data):
        if self.head.data == data:
            self.head = self.head.next
        else:
            temp = self.head
            while temp.next is not None:
                if temp.next.data is data:
                    break
                temp = temp.next
            if temp.next is None:
                print("node not found")
            else:
                temp.next = temp.next.next


# Printing the elements or data field in the linked list
    def output(self):
        temp = self.head
        if temp == None:
            print("LL is empty")
        while temp!= None:
            print(temp.data)
            temp = temp.next



# main method for this block:
def main():
    li = linkedList()
    li.addEmpty(20)
    li.addBegin(21)
    li.addBegin(22)
    li.delNode(20)



# To get the input from the user or console:
    # dt = int(input("enter the total no of value to enter: "))
    # for i in range(dt):
    #     li.begin(input("enter the value: "))

    li.output()

 # used for execute the main inside this block only
if __name__ == '__main__':
    main()



