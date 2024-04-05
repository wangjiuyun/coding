import random
#初始化数组
arr : list[int] = [0] * 5
nums : list[int] = [1, 2, 4, 6, 7 ]

#访问元素
def random_access(num : list[int]) -> int:
    """随机访问元素"""
    #在区间[0,len(num)-1]中随机抽取一个数字
    random_index = random.randint(0 , len(num)-1)
    #返回随机数
    random_num : int = num[random_index]
    return random_num

#插入元素
def insert(nums : list[int] , num : int , index : int):
    """在数组的索引index处插入元素num"""
    #把索引index以及之后的所有元素都向后移动一位
    for i in range(len(nums)-1 , index - 1 , -1):
        nums[i] = nums[i - 1]
    nums[index] = num

#删除元素
def remove(nums : list[int] , index : int):
    """删除索引index处的元素"""
    #索引index之后的索引元素向前移动一位
    for i in range(index , len(nums) - 1):
        nums[i] = nums[i + 1]
#遍历数组
def traverse(nums : list[int] ):
    """遍历数组"""
    count : int = 0
    #通过索引遍历数组
    for i in range(len(nums)-1):
        count += nums[i]
    for num in nums:
        num += num
    #同时遍历数据索引和元素
    #enumerate是在遍历一个序列时，同时获取每个元素的索引和值
    for i , num in enumerate(nums):
        count += nums[i]
        count += nums
#查找元素
def find(nums : list[int] , target : int) -> int:
    """在数组中查找指定元素"""
    for i in range(len(nums) - 1):
        if target == nums[i]:
            return i
    return -1

#扩容数组
def extend(nums : list[int], enlarge : int) -> list[int]:
    """扩展数组长度"""
    #初始化一个扩展长度后的数组
    res : int = [0] * (len(nums) + enlarge)
    #将原数组复制到新的数组里面
    for i in range(len(nums) - 1):
        res[i] = nums[i]
    #返回扩展后的新数组
    return res


#运行函数的地方
if __name__ == "__main__":
    # receive_num : int = random_access(nums)
    # print(f"接受的数字为：{receive_num}")
    # insert(nums , 100 , 2)
    print(nums)
    remove(nums , 2)
    print(nums)