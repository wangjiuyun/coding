def dunction() -> int:
    #执行某些操作
    pass

def loop(n : int):
    """循环空间复杂度为O(1)"""
    for _  in range(n):
        function()

def recur(n : int):
    """递归空间复杂度为O(n)"""
    if n == 1:
        return 1
    return recur(n-1)