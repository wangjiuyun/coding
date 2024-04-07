class ListNode:
    """构造节点"""
    def __init__(self, next, val) :
        """构造节点"""
        self.next : ListNode | None = None
        self.val : int = val