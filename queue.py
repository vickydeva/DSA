queue = []

def enqueue():
    a = input("enter the element to add in the queue: ")
    queue.append(a)
    print(queue)

def dequeue():
    if not queue:
        print("queue is empty.")
    else:
        p = queue.pop(0)
        print(p, " is the removed element from the queue.")

while True:
    i = input("enter the option, 1.enqueue, 2.dequeue, 3.exit. : ")
    if i == '1':
        enqueue()
    elif i == '2':
        dequeue()
    elif i == '3':
        print("Exit from the queue.")
        break
    else:
        print("enter the correct option.")
