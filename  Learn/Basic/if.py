# 基本格式
age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
else:
    price = 5

print(price)

# 检查特定值是否包含在列表中
cars = ['bmw', 'audi', 'toyota']
car = 'car'
if car not in cars:
    print(car)

# 确定列表不为空
list = []

if list:
    print('not null')
else:
    print('null')