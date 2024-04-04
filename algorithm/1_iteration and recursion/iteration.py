def for_loop(n:int)->int:
    """for循环"""
    res = 0
    #循环求和 1,2,3,..,n-1,n
    for i in range(1,n+1):
        res += i
    return res
print(for_loop(120))


def while_loop(n:int)->int:
    """while循环"""
    res = 0
    i = 1
    #循环求和1,2,3,...n-1,n
    while i <= n:
        res += i
        i += 1
    return res
print(while_loop(100))

def nested_for_loop(n:int)->int:
    """双层for循环"""
    res = ""
    #循环i = 1,2,3...,n-1,n
    for i in range(1,n+1):
        #循环 j = 1,2,3,,,,n-1,n
        for j in range(1,n+1):
            #f-string格式
            res += f"({i},{j}),"
    return res
n = nested_for_loop(9)
print(n,type(n))
print("\n")

def recur(n: int)-> int:
    """递归"""
    #终止条件
    if n == 1:
        return 1
    #递：递归调用
    res = recur(n-1)
    #归：返回结果
    return n+res
print(recur(10))


def tail_recur(n:int ,res:int)->int:
    """尾递归"""
    #终止条件
    if n == 0:
        return res
    #尾递归调用
    return tail_recur(n - 1, res + n)
n=tail_recur(10,0)
print(n)


#使用递归来解决斐波拉契问题
def fib(n: int)->int:
    """斐波拉契数列递归"""
    #终止条件f(1)=0,f(2)=1
    if n == 1 or n == 2:
        return n - 1
    #递归调用f(n)=f(n-1)+f(n-2)
    res = fib(n - 1) + fib( n - 2)
    return res
print(fib(3))


#使用一个显示的栈来模拟调用栈的行为
def for_loop_recur(n : int) -> int :
    """使用迭代模拟递归"""
    #使用一个显式的栈来模拟系统调用栈
    stack = []
    res = 0
    #递归：递归调用
    for i in range(n , 0 , -1):
        #通过"入栈操作"模拟"递"
        stack.append(i)
    #归，返回结果
    while stack:
        #通过出栈模拟归
        res += stack.pop()
    #res = 1+2+3+4...
    return res    
print(f"__name__,{__name__}")
if __name__ == "__main__":
    n = 10
    res = for_loop_recur(n)
    print(f"调用栈的结果{res}")