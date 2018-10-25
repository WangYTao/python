# 基本
name = input("Please enter your name: ")
print("Hello, " + name + "!")

# 多行提示
prompt = "Hi!"
prompt += "\nWhat is your name?"
name = input(prompt)
print("Hello, " + name + "!")

# 获取数值输入
age = input("How old are you? ")
age = int(age)