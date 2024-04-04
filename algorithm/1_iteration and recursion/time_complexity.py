def contast(n : int) -> int:
    """常数阶"""
    count = 0
    size = 100000
    for _ in range(size):
        count += 1
    return count

def linear(n : int ) -> int:
    """线性阶"""
    count = 0
    for _ in range(n):
        count +=1
    return count

def array_traversal(nums : int) -> int:
    """线性阶(遍历数组)"""
    count = 0
    #循环次数与数组长度成正比
    for num in nums:
        count += 1
    return count

def quadratic(n : int) -> int:
    """平方阶"""
    count = 0
    #循环次数与数据大小n成正比
    for i in range(n):
        for j in range(n):
            count += 1
    return count

def  bubble_sort(nums : list[int]) -> int:
    """平方阶(冒泡排序)"""
    count = 0 #计数器
    #开始外循环
    for i in range(len(nums)-1 , 0 , -1):
        #开始内循环
        for j in range(i):
            #从小到大排序
            if nums[j] > nums[j+1]:
                tmp : int = nums[j]
                nums[j] = nums[j + 1]
                nums[j + 1] = tmp
                count += 3
    return nums
nums = [2,4,12,656,23,1]
print(bubble_sort(nums))

def expoential(n : int ) -> int:
    """指数阶(循环实现)"""
    count = 0
    base = 1
    #(等比数列)
    #细胞每轮一分为二,形成数列1，2，4，8.....2的(n-1)次方
    for _ in range(n):
        for _ in range(base):
            count += 1
        base *= 2
    #count = 1+2+4+8+.....
    return count

def exp_recur(n : int) -> int:
    """指数阶(递归实现)"""
    if n == 1:
        return 1
    return exp_recur(n - 1) + exp_recur(n - 1) + 1


def logarithmic(n : int) -> int:
    """对数阶"""
    count = 0
    while n > 1:
        n /= 2
        count += 1
    return count

def log_recur(n : int) -> int:
    """对数阶(递归实现)"""
    if n <= 1:
        return 0
    return log_recur(n / 2) + 1



#有一点迷惑，递归确实有点晕
def linear_log_recur(n : int) -> int:
    """线性对数"""
    if n <= 1:
        return 1
    count : int = linear_log_recur(n // 2) * 2
    for _ in range(n):
        count += 1
    return count
    

def factorial_recur(n : int) -> int:
    """阶乘阶(递归实现)"""
    if n == 0:
        return 1
    count = 0
    #从1 个分裂出n个
    for _ in range(n):
        count += factorial_recur(n - 1)
    return count
