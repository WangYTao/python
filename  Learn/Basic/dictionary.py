# 字典声明
user = {
    'name': 'wangyantao',
    'age': 22
}
print(user)

# 访问字典中的值
print(user['name'])

# 添加键值对
user['sex'] = 'Male'
user['test'] = 'test1'
print(user)

# 修改键值对
user['test'] = 'test2'
print(user)

# 删除键值对
del user['test']
print(user)

# 字典不仅可以存储对象，也可以存储多对象的同一种信息
# 每个人喜欢的编程语言
favorite_languages = {
    'wyt': 'Java',
    'wytao': 'Python',
    'wangyantao': 'C'
}

# 遍历所有的键值对
for key, value in user.items():
    print("Key:" + key)
    print("Value: " + str(value))
# 声明的两个变量可以使用任何名称
for name, languages in favorite_languages.items():
    print(name.title() + "'s favorite language is " + languages + ".")

# 遍历字典中的所有键
for name in favorite_languages.keys():
    print(name)
# 遍历字典时，会默认遍历所有的键，因此keys()可省略
for name in favorite_languages:
    print(name)

# 遍历字典中的所有值
for language in favorite_languages.values():
    print(language)

# 嵌套
users = [
    {
        'name': 'root',
        'favorite': ['game','music'],
        'mother': {
            'name': 'admin',
            'age': 40
        }
    },
    {
        'name': 'admin',
        'favorite': ['game','music'],
        'mother': {
            'name': 'root',
            'age': 40
        }
    }
]