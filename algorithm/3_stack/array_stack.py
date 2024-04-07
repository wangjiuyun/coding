class ArrayStack:
    """基于数组实现的栈"""

    def __init__(self) :
        """构造方法"""
        self._stack: list[int] = []
    
    def size(self) -> int:
        """获取栈的长度""" 
        return len(self._stack)
    
    def is_empty(self) -> bool:
        """判断栈是否为空"""
        return self._stack == []
    
    def push(self, item: int):
        """入栈"""
        self._stack.append(item)

    def pop(self) -> int:
        """出栈"""
        if self.is_empty():
            raise IndexError("栈为空")
        return self._stack.pop()
    
    def peek(self) -> int:
        """访问栈顶元素"""
        if self.is_empty():
            raise IndexError("栈为空")
        #-1就是从后向前数第一个，python独有标记
        return self._stack[-1]
    
    def to_list(self) -> list[int]:
        """返回列表用于打印"""
        return self._stack
    
stack = ArrayStack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)

print(stack.to_list())
stack.pop()
print(stack.to_list())
print(stack.peek())