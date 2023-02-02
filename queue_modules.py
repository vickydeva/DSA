import collections
ls = collections.deque()
# 1. first method using append and popleft:
ls.append(10)
ls.append(20)
print(ls)
print(ls.popleft())
print(ls)

# 2. second method using appendleft and pop:
ls.appendleft(30)
ls.appendleft(40)
print(ls)
ls.pop()
print(ls)

# Hint: use any method you want but always stick with fifo or lilo methology.

#                        HAPPY CODING:)
