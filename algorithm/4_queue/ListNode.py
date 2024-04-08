class ListNode:
    """构建链表的结构"""
    def __init__(self, val : int):
        self.next : ListNode | None = None 
        self.val : int = val