class ListNode:
    """双向链接表节点"""

    def __init__(self , val: int):
        """构造方法"""
        self.val: int = val
        #后继节点引用
        self.next: ListNode | None = None
        #前驱节点引用
        self.prev: ListNode | None = None

class LinkListDeque:
    """基于双向链表实现的双向队列"""

    def __init__(self) :
        """构造方法"""
        self._front: ListNode | None = None #头节点front
        self._rear: ListNode | None = None #尾节点 rear
        self._size: int = 0 #双向队列的长度

    def size(self) -> int:
        """获取双向队列的长度"""
        return self._size
    
    def is_empty(self) -> bool:
        """判断是否为空"""
        return self.size() == 0
    
    def push(self, num: int, is_front: bool):
        """入队操作"""
        node = ListNode(num)
        #若链表为空，则令front和rear都指向node
        if self.is_empty():
            self._front = self._rear = node
        #队首入队操作
        elif is_front:
            #将node添加至链表头部
            self._front.prev = node
            node.next = self._front
            self._front = node #更新头节点
        #队尾入队操作
        else:
            #将node添加至链表尾部
            self._rear.next = node
            node.prev = self._rear
            self._rear = node #更新尾节点
        self._size += 1 #更新队列长度

    def push_first(self, num: int):
        """队首入队"""
        self.push(num, True)

    def push_last(self, num: int):
        """队尾入列"""
        self.push(num, False)


    def pop(self, is_front:bool) -> int:
        """出队操作"""
        if self.is_empty():
            raise IndexError("双向队列为空")
        #队首出队操作
        if is_front:
            val : int = self._front.val #暂存头节点值
            #删除头节点
            fnext: ListNode | None = self._front.next
            if fnext != None:
                fnext.prev = None
                self._front.next = None
            self._front = fnext #更新头节点
            #队尾出队操作
        else:
            val: int = self._rear.val #暂存尾节点值
            #删除尾节点
            rprev: ListNode | None = self._rear.prev
            if rprev != None:
                rprev.next = None
                self._rear.prev = None
            self._rear = rprev  #更新尾节点
        self._size -= 1
        return val
         
    def pop_first(self) -> int:
        """队首出队"""
        return self.pop(True)
    
    def pop_last(self) -> int:
        """队尾出列"""
        return self.pop(False)
    
    def peek_first(self) -> int:
        """访问队首元素"""
        if self.is_empty():
            raise IndexError("双向队列为空")
        return self._front.val
    
    def peek_rear(self) -> int:
        """访问队尾元素"""
        if self.is_empty():
            raise IndexError("双向队列为空")
        return self._rear.val
    
    def to_array(self) -> list[int]:
        node = self._front
        res : list[int] = []
        for i in range(self.size()):
            res.append(node.val)
            node = node.next
        return res
    

s = LinkListDeque()
# s.push_first(3)
# s.push_first(2)
# s.push_last(22)
# s.push_last(33)
s.push(10,True)
s.push(20,True)
print(s.size())
print(s.to_array())

        
