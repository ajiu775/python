# Variable Type
# Python 是敏感类语言对大小写敏感
number = 10
Number = 20
point = 10.1
string = 'string'
is_right = True
lists = [1, 2, 3, 4, 5]
tuples = (5, 4, 3, 2, 1)
print(number)
print(Number)
print(point)
print(string)
print(is_right)

# Python internal method
# name = input('你的名字是？')
# print('你好' + name)
# 类型转换
int()
float()
bool()

# ''用来表示字符串 如果字符串含有""可以用''来表示
# ""也可以用来表示字符串 如果字符串含有''可以用""来表示
# ''' '''用来表示文本
single = '含有"双引号"'
double = "'含有双引号'"
text = ''' 
你好，

    欢迎开始学习python。
    
祝好，
阿旧

'''
print(single)
print(double)
print(text)

# 数组下标问题
message = '0123456'
# 数组下标是从0开始的
print(message[0])
# Index -1 表示最后一个字符
print(message[-1])
# array[0:3]是从index[0] 开始到 index[3] 结束的，不包括 index[3]
print(message[0:3])
# 开始索引和结束索引可以缺省
print(message[:3])
print(message[0:])

# 字符串格式化以 f 开头变量部分用{Variable}
first = 'Lee'
last = 'Allen'
str_format = f'{first} [{last}]'
print(str_format)

# 字符串方法
str_method = 'string'
len(str_method)  # 返回字符串长度
str_method.upper()  # 字符串变成大写
str_method.lower()  # 字符串变成小写
'str' in str_method  # 查询是否有该字符串
str_method.find('str')  # 查询字符串是否在本串中存在

# 运算符
add = 10 + 3  # 加号
sub = 10 - 3  # 减号
multi = 10 * 3  # 乘号
div_double = 10 / 3  # 除法 结果取浮点型
div_integer = 10 // 3  # 除法 结果取整形
exponentiation = 10 ** 3  # 幂运算

# 条件判断
is_beautiful = True
is_tall = True
if is_beautiful:
    print(" You have a chance ")
elif is_tall:
    print(" You also have a chance ")
else:
    print(" You have no chance ")
# 或操作
if is_beautiful and is_tall:
    print(" You are nice ")
# 与操作
if is_beautiful or is_tall:
    print(" You can continue ")
# 否操作
if not is_beautiful:
    print(" You have no change ")

# 比较操作 > < >= <= ==
compare = 50
if compare > 60:
    print(" I'm old ")
else:
    print(" I'm young ")



