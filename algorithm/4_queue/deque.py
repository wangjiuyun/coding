from collections import deque

#初始化双向队列
#type: ignore是告诉类型检查器*（如'mypy'或者pychram的类型检查功能）
#忽略这一代码的类型检查。如果不加这个注释，类型检查器会报错，认为deque的
#使用方式不符合预期的类型约束。
deque : deque[int] = deque() # type: ignore

#元素入栈
#添加至队尾
deque.append(2)
deque.append(3)
deque.append(10)
deque.append(6)
#添加至队首
deque.appendleft(20)
deque.appendleft(23)

#访问元素
front : int = deque[0]  #队首元素
rear : int = deque[-1]  #队尾元素

#元素出栈
#队尾出栈
deque.pop()
#队首出栈
deque.popleft()

#获取双向队列的长度
len : int = len(deque)

#判断双向队列是否为空
is_empty : bool = (len(deque) == 0)

