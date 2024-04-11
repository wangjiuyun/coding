# 初始化哈希表
hmap: dict = {}

# 添加操作
# 在哈希表中添加键值堆6
hmap[12836] = "小哈"
hmap[15937] = "小罗"
hmap[16750] = "小算"
hmap[13276] = "小法"
hmap[10587] = "小鸭"

# 查询操作
# 向哈希表中输入键key,得到值value
name : str = hmap[15937]

# 删除操作
# 在哈希表中删除键值队（key,value)
hmap.pop(10587)

# 遍历哈希表
# 遍历键值队key ->value
for key,value in hmap.items():
    print(f"{key}->{value}")

# 单独遍历键key
for key in hmap.keys():
    print(key)

# 单独遍历值value
for value in hmap.values():
    print(value)