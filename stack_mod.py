# 1. using dequeue class in collections module
import collections
stack = collections.deque()
stack.append(10)
stack.append(20)
print(stack)
stack.pop()
print(stack)

# 2.using LifoQueue class in Queue module
import queue
stack2 = queue.LifoQueue(4)
stack2.put(10,timeout = 1)
stack2.put(20,timeout= 1)
stack2.put(30,timeout=1)
print(stack2.put(23))
# this class doesn't show all the output using the print method
