# 初始化列表
# 无初始值
nums1 : list[int] = []
# 有初始化
nums : list[int] = [1, 2, 3, 4]

#访问元素
num : int = nums[1] #访问索引1处的元素

#更新元素
nums[1] = 0 #将索引1处的元素更新为0

#清空列表
nums.clear()

#在尾部添加元素
nums.append(1)
nums.append(2)
nums.append(2)
nums.append(3)
nums.append(5)
nums.append(10)

#在中间插入元素
nums.insert(3, 6) #在索引3处插入数字6

#删除元素
nums.pop(3)   #删除索引3处的元素


#通过索引遍历列表
count = 0
for i in range(len(nums)):
    count += nums[i]

#直接遍历列表元素
for num in nums:
    count += num

#拼接列表
nums1 : list[int] = [6, 3, 1, 8]
nums += nums1

#排序列表
nums.sort()

