from ListNode import ListNode
class LinkedListQueue:
    "基于链表实现的队列"
    
    def __init__(self):
        """构造方法"""
        self._front : ListNode | None = None #头节点
        self._rear : ListNode | None = None #尾节点
        self._size = 0

    def size(self) -> None:
        """获取列表的长度"""
        return self._size

    def is_empty(self) -> bool:
        """判断队列是否为空"""
        """return self._front is None 通过判断头节点是否为空来判断队列是否为空"""
        return not self._front

    def  push(self, num : int):
        """向队列中加入数据"""
        node : ListNode = ListNode(num)
        #如果队列为空，则令头，尾节点都指向该节点
        if self._front is None:
            self._front = node
            self._rear = node
        #如果队列不为空，则将该节点添加到尾节点后
        else:
            """
                这里不适用node = self._rear是因为这只是一个赋值操作，键尾结点
                的引用赋值给另一个变量
                self._rear = node是用来更新队列的尾部节点，确保队列的结构随着新节点的添加而更新
            """
            self._rear.next = node
            self._rear = node
        self._size += 1

    def pop(self) -> int:
        """出队"""
        num : int = self.peek()
        self._front = self._front.next
        #在出队列后判断是否为空
        if self._front is None:
            self._rear = None
        self._size -= 1
        return num
    
    def peek(self) -> int:
        """获取首元素"""
        if self.is_empty():
            raise IndexError("队列为空")
        return self._front.val
    
    def to_list(self) -> list[int]:
        """转化为列表用于打印"""
        queue = []
        temp = self._front
        while temp:
            queue.append(temp.val)
            temp = temp.next
        return queue
    
num = LinkedListQueue()
num.push(1)
print(num.to_list())
num.pop()
print(num.to_list())