class ArrayQueue:
    """基于环形数组实现的队列"""

    def __init__(self ,size : int):
        """构造方法"""

        #用于存储队列元素的数组
        self._nums : list[int] = [0] * size 
        #队首指针，指向队首元素
        self._front : int = 0
        #队列长度
        self._size : int = 0

    def capacity(self) -> int:
        """获取队列的容量"""
        return len(self._nums)
    
    def size(self) -> int:
        """获取队列的长度"""
        return self._size
    
    def is_empty(self) -> bool:
        """判断队列是否为空"""
        return self._size == 0
    
    def peek(self) -> int:
        """访问队首元素"""
        if self.is_empty():
            raise IndexError("队列为空")
        return self._nums[self._front]
    
    def pop(self) -> int:
        """出队列"""
        num : int = self.peek()
        #队首指针向后移动一位，若超过尾部，则返回数组头部
        self._front = (self._front + 1) % self.capacity()
        self._size -= 1
        return num
    
    def push(self, num : int):
        """入队"""
        if self.size == self.capacity:
            raise IndexError("队伍已经满了")
        #计算队尾指针，指向队尾索引+1
        #通过区域操作实现rear越过数组尾部回到同步
        rear : int = (self._front + self._size) % self.capacity()
        #将num添加至队尾
        self._nums[rear] = num
        self._size += 1


    def to_list(self) -> list[int]:
        """返回列表用于打印"""
        res = [0] * self._size
        j : int = self._front
        #考虑队列有可能不是从0索引开始的，可以正确处理队列的头部元素不在数组开头的情况
        for i in range(self._size):
            res[i] = self._nums[( j % self.capacity())]
            j += 1
        return res
    
s = ArrayQueue(20)
s.push(1)
s.push(2)
s.push(3)
s.push(5)
print(s.to_list())
s.pop()
print(s.to_list())
print(f"队列的容量{s.capacity()}")
print(f"队列的长度{s.size()}")