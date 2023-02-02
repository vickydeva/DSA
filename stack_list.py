# example program for stack using list
stack = []
def push():
    if len(stack) == limit:
        print("stack is full!")
    else: # We shouldn't get value from the user, bcz it follows stacks, FILO or LIFO sequence or method.
        e = input("enter the value: ")
        stack.append(e)
        print('value added ', e)
        print(stack)


def pop():
    if not stack:
        print("stack is empty.")
    else:
        a = stack.pop()
        print("value removed", a)
        print(stack)


limit = int(input("Enter the limit of the stack: "))
while True:
    val = input("Enter the value: 1. push, 2. pop, 3. quit: ")
    if val == '1':
        push()
    elif val == '2':
        pop()
    elif val == '3':
        print("exit from stack.")
        break
