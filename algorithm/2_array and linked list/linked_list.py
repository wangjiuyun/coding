import random
class ListNode:
    """链表节点类"""
    def __init__(self , val : int):
        #节点值
        self.val = val 
        #指向下一个节点的引用(有可能是listNode或者None)
        self.next : ListNode | None = None 
#创建节点并且形成链表
def create_List(head : ListNode,len : int) -> ListNode | None:
    """创建节点,返回一个链表"""
    for _ in range(len):
        c_node = ListNode(random.randint(0,100))
        c_node.next = head.next
        head.next = c_node

    return head

#插入节点
def insert(n0 : ListNode , P :ListNode):
    """在链表的节点n0之后插入节点P"""
    P.next = n0.next
    n0.next = P

#删除节点
def delete(n0 : ListNode ):
    """删除链表节点n0之后的首个节点"""
    if not n0.next:
        return
    #n0->n1
    S = n0.next
    n1 = S.next
    n0.next = n1
    # n0.next = n1.next
#访问节点
def access(head : ListNode , index : int) -> ListNode | None:
    """访问链表中索引为index的节点"""
    for _ in range(index):
        if not head:
            return None
        head = head.next
    return head

#查找节点
def find(head : ListNode , target : int) -> ListNode | None:
    """在链表中查找值为target的首个节点"""
    index = 0
    while head:
        if head.val == target:
            return index
        head = head.next
        index += 1
    return -1

#遍历链表
def traverse(head : ListNode ) :
    """遍历输出链表每一个值"""
    #先判断链表是否为空
    if not head:
        return -1
    while head.next:
        print(f"{head.val}",end="->")
        head = head.next
    print("None")


if __name__ == "__main__":
    #初始化链表1->2->3->5->6
    #初始化各个节点
    n0 = ListNode(1)
    # n1 = ListNode(2)
    # n2 = ListNode(3)
    # n3 = ListNode(5)
    # n4 = ListNode(6)
    # n5 = ListNode(100)
    #构建节点之间的引用
    # n1.next = n2
    # n2.next = n3
    # n3.next = n4
    create_List(n0,10)
    traverse(n0)
    delete(n0)
    traverse(n0)
