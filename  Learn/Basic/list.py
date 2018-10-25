# 列表
names = ['wangyantao', 'wytao']
print(names)

# 1 访问列表元素
#	Python为访问最后一个列表元素提供了一种特殊的语法。
#	通过将索引制定为-1，可让Python返回最后一个列表元素。
print(names[-1])
print(names[-2])

# 2 在列表中添加元素
# 	2.1 在列表末尾添加元素
names.append('wsm')
print(names)
# 	2.2 在列表中插入元素
names.insert(0, 'wyt')
print(names)


# 3 从列表中删除元素
# 	3.1 使用del语句删除元素
del names[0]
print(names)
# 	3.2 使用方法pop()删除元素
#	方法pop()可以将列表中元素删除，并返回删除的值
#	删除末尾元素
poped_names = names.pop()
print(poped_names)
print(names)
#	删除指定位置的元素
names.pop(0)
print(names)
#	3.3 根据值删除元素
#	方法remove()可删除指定值的元素,remove()方法只删除第一个指定的值
names.remove('wytao')
print(names)

# 3 组织列表
#	3.1 使用方法sort()对列表进行永久性排序
cars = ['bmw', 'audi', 'toyota']
print(cars)
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)
#	3.2 使用函数sorted()对列表进行临时排序（返回排序后列表，列表本身不变）
cars = ['bmw', 'audi', 'toyota']
print(cars)
sorted_cars = sorted(cars)
print(cars)
print(sorted_cars)
#	3.3 反转列表元素的排列顺序
print(cars)
cars.reverse()
print(cars)
#	3.4 确定列表长度
print(len(cars))

# 4 检查特定值是否包含在列表中
car = 'car'
if car not in cars:
    print(car)

# 5 确定列表不为空
list = []

if list:
    print('not null')
else:
    print('null')

# 6 元组
dimensions = (200, 50)
print(dimensions[0])

#   Python不能给元组的元素赋值
#dimensions[0] = 100  <-错误

#   Python可以给存储元组的变量赋值
dimensions = (400, 100)
