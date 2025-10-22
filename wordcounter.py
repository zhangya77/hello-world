import re
from collections import Counter

def count_words(filename):
    word_count = Counter()

    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                words = re.findall(r'\b\w+\b', line.lower())
                word_count.update(words)
    except FileNotFoundError:
        print(f"Error File:'{filename}' not found")
        return {}
    except Exception as e:
        print(f"Read file error:{e}")
        return {}

    return dict(word_count)

if __name__ == "__main__":
    test_content = """
    Hello world! This is a test file.
    Hello again, this is only a test.
    Testing, testing, 1, 2, 3. 2.
    """

    with open("test_content.txt", "w") as f:
        f.write(test_content)

    print("*" * 20)
    result=count_words("test_content.txt")
    for word,count in sorted(result.items()):
        print(f"{word}:{count}")
    try:
        with open("test_content.txt", "r") as f:
            f.readline()
    except FileNotFoundError:
        print(f"File not found")

str='123456789'
print(str)
print(str[0:1])
print(str[0:-2])
print(str[2:5])
print(str[3:])
print(str[1:5:2])
print("-"*10)
print(str+'hello',end="")
print(str*2)
print("hello\nworld")
print(r"hello\nworld")

# input("\n\n按下 enter 键后退出。")

import sys; x='fdsadfaf'; sys.stdout.write(x);sys.stdout.write(x+'\n');

from sys import argv,path

print('================Python import mode==========================')
print ('命令行参数为:')
for i in argv:
    print(i)
print('\n python path is',path)

# 变量定义
x = 10          # 整数
y = 3.14         # 浮点数
name = "Alice"   # 字符串
is_active = True # 布尔值

# 多变量赋值
a, b, c = 1, 2, "three"

# 查看数据类型
print(type(x))        # <class 'int'>
print(type(y))        # <class 'float'>
print(type(name))     # <class 'str'>
print(type(is_active)) # <class 'bool'>

# 不可变示例
x = 10
print(f"x的id: {id(x)}")  # 输出: x的id: 140736053260736 (示例值)

x = x + 1  # 看起来是修改，实际上是创建新对象
print(f"修改后x的id: {id(x)}")  # 输出不同的id值

# 另一个例子
a = 5
b = 5
print(f"a is b: {a is b}")  # 输出: True (Python会重用小整数对象)

t=(1,2,3)
t=(10,)+t[1:]
print(t)

list=[1,'123','haha',3.14,100]
list1=['abc',456]
print(list)
print(list+list1)
list[3]=3.1415
print(list)
print(list[0::1])
print(list[-1::-1])

s='abcdefg'
print(s[-1::-1])


def reverseWords(input):
    # 通过空格将字符串分隔符，把各个单词分隔为列表
    inputWords = input.split(" ")

    # 翻转字符串
    # 假设列表 list = [1,2,3,4],
    # list[0]=1, list[1]=2 ，而 -1 表示最后一个元素 list[-1]=4 ( 与 list[3]=4 一样)
    # inputWords[-1::-1] 有三个参数
    # 第一个参数 -1 表示最后一个元素
    # 第二个参数为空，表示移动到列表末尾
    # 第三个参数为步长，-1 表示逆向
    inputWords = inputWords[-1::-1]

    # 重新组合字符串
    output = ' '.join(inputWords)

    return output

input = 'I like runoob'
rw = reverseWords(input)
print(rw)

ss=set()
ss={1,2,2,3}
print(ss)
if(3 in ss):
    print("3 in ss")
else:
    print("3 not in ss")

a = set('abracadabra')
b = set('alacazam')

print(a)

print(a - b)
print(a | b)
print(a & b)
print(a ^ b)

dict3= {}
dict3['one'] = "111"
dict3[2] = '222'
print(dict3)
print(dict3[2])

tinydict = {'name': 'runoob','code':1, 'site': 'www.runoob.com'}
print(tinydict)
print(tinydict.keys())
print(tinydict.values())

dict1={x: x**2 for x in (2, 4, 6, 8)}
print(dict1)
dict2 = dict([('Runoob', 1), ('Google', 2), ('Taobao', 3)])
print(dict2)

a = 20
b = 20

if (a is b):
    print("1 - a 和 b 有相同的标识")
else:
    print("1 - a 和 b 没有相同的标识")

if (id(a) == id(b)):
    print("2 - a 和 b 有相同的标识")
else:
    print("2 - a 和 b 没有相同的标识")

b = 30
if (a is b):
    print("3 - a 和 b 有相同的标识")
else:
    print("3 - a 和 b 没有相同的标识")

if (a is not b):
    print("4 - a 和 b 没有相同的标识")
else:
    print("4 - a 和 b 有相同的标识")

import time

for i in range(101): # 添加进度条图形和百分比
    bar = '[' + '=' * (i // 2) + ' ' * (50 - i // 2) + ']'
    print(f"\r{bar} {i:3}%", end='', flush=True)
    #time.sleep(0.05)
print()

x = True
country_counter = {}

def addone(country):
    if country in country_counter:
        country_counter[country] += 1
    else:
        country_counter[country] = 1

addone('China')
addone('Japan')
addone('China')

print(len(country_counter))

a=set()
b={1,2,3,4}
print(a^b)

thisset = set(("Google", "Runoob", "Taobao"))
thisset.update("Facebook")
print(thisset)

thisset.update({"Facebook"})
print(thisset)

ms = [i for i in range(100) if i % 3 == 0 ]
print(ms)

listdemo = ['Google','Runoob', 'Taobao']
nd = {key:len(key) for key in listdemo}
print(nd)

l2 = {x: x**2 for x in (2, 4, 6)}
print(l2)

a = {x for x in 'abdsdafsdfwfd' if x not in 'abc'}
print(a)

print("===="*5)
t = (x**2 for x in range(10))
b = tuple(t)
print(b)
for i in t:
    print("*")
    print(i)

# 创建生成器
gen = (x**2 for x in range(5))
print("生成器已创建，但尚未计算任何值")
# 只有在迭代时才会计算
for value in gen:
    print(f"计算得到: {value}")

list=[1,2,3,4]
it = iter(list)

while True:
    try:
        print(next(it))
    except StopIteration:
        sys.exit()


print('+'*10)
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x


myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))





