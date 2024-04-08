from collections import deque

#初始化队列
#在python中，我们一般将双向队列类deque当作队列使用
#虽然queue.Queue()是纯正的队列类，但不太好用，因此不推荐
que : deque[int] = deque()

#元素入栈
que.append(1)
que.append(2)
que.append(3)
que.append(4)
que.append(5)

#访问队首元素
front : int = que[0]

#元素出列
pop : int = que.popleft()

#获取队列的长度
size : int = len(que)

#片段队列是否为空
is_empty : bool = len(que) == 0
