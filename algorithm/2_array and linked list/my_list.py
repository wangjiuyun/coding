"""
加深对列表工作原理的理解，尝试实现一个简易版列表，包括以下是三个重点设计
    初始容量: 选取一个合理的数组初始容量。在本实例中，选择10作为初始容量
    数量记录：声明一个变量size,用于记录列表当前元素数量，并且随着元素插入和删除实时更新。根据此变量，我们可以定位列表尾部，以及判断是否需要扩容
    扩容机制，若插入元素列表容量已满，则需要进行扩容。先根据扩容倍数创建一个更大的数组，再将当前数组的所有元素依次移动至新数组
"""

class MyList:
    """列表类"""
    def __init__(self):
        """构造方法"""
        self._capacity: int = 10  #列表容量
        self._arr: list[int] = [0] * self._capacity #数组（存储列表元素）
        self._size: int = 0 #列表长度（当前元素数量）
        self._extend_ratio: int = 2 #每次列表扩容后的倍数

    def size(self) -> int:
        """获取列表长度(当前元素数量)"""
        return self._size
    
    def capacity(self) -> int:
        """获取列表容量"""
        return self._capacity
    
    def get(self, index: int) -> int:
        """访问元素"""
        #索引如果越界，则抛出异常，下同
        if index < 0 or index >= self._size:
            raise IndexError("索引越界")
        return self._arr[index]
    
    def set(self, num:int ,index: int):
        """更新元素"""
        if index < 0 or index >= self._size:
            raise IndexError("索引越界")
        self._arr[index] = num

    def add(self, num : int):
        """在尾部添加元素"""
        #元素数量超出容量时，触发扩容机制
        if self.size() == self.capacity():
            self.extend_capacity()
        self._arr[self._size] = num
        self._size += 1

    def insert(self, num: int,index: int):
        """在中间插入元素"""
        if index < 0 or index >= self._size:
            raise IndexError("索引越界")
        #元素数量超出容量时，触发扩容机制
        if self._size == self.capacity():
            self.extend_capatify()
        #将索引index 以及之后的元素都想后移动一位
        for j in range(self._size - 1 , index - 1, -1):
            self._arr[j + 1] = self._arr[j]
        self._arr[index] = num
        #更新元素数量
        self._size += 1

    def remove(self, index: int) -> int:
        """删除元素"""
        if index < 0 or index >= self._size:
            return IndexError("索引越界")
        num = self._arr[index]
        #将索引index之后的元素向前都移动一位
        for j in range(index, self._size - 1):
            self._arr[j] = self._arr[j+1]
        #更新元素数量
        self._size -= -1
        #返回被删除的元素
        return num
    
    def extend_capacity(self):
        """列表扩容"""
        #新建一个长度为原数组，_extend_ratio倍的新数组，并将原数复制到新数组
        self._arr = self._arr + [0] * self.capacity() * (self._extend_ratio -1)
        #更新列表容量
        self._capacity = len(self._arr)

    def to_array(self)-> list[int]:
        """返回有效长度的列表"""
        return self._arr[: self._size]

