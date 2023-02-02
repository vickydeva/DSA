# 1. using list but it is not a right or recommended way
l=[]
l.append(10)
l.append(100)
l.append(50)
l.append(20)
print(l)
l.sort()  # sort the elements in the ascending order, here i have taken the smaller has high priority.
print(l)
print("The removed element: ", l.pop(0))   # remove the elements based on the priority.
print("The removed element: ", l.pop(0))
print(l)

# 2. using the priorityQueue class
import queue
ls= queue.PriorityQueue()
ls.put(10)
ls.put(100)
ls.put(20)
print(ls.get())
print(ls.get())

# 3. using the tuple which stores the value and priority numbers inside the list
lst = []
lst.append((1,"20"))
lst.append((3,"vk"))
lst.append((2,"mk"))
lst.append((10,24))
print(lst)
lst.sort(reverse=True)  # sort the queue in the reverse order.
print(lst)
print("The removed element: ", lst.pop(0))
print("The removed element: ", lst.pop(0))
print("the final queue is: ", lst)
