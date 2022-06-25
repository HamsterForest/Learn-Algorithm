from collections import deque
a=[[1,2,3],[5,6,7]]
queue=deque()
queue.extend(a)
print(queue)
z,x,y=queue.popleft()
print(z,x,y)
