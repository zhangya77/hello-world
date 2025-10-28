# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import sys

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm2,zhangya')
    print_hi('hello,world')

print('\n\nPython 路径为：', sys.path, '\n')


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
# See PyCharm help at https://www.jetbrains.com/help/pycharm/

tt = (1, 2, 3, 4, 5, 6)
it = iter(tt)
while True:
    try:
        print(next(it))
    except StopIteration:
        break

print( "="*10 )
class MyIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.data):
            value = self.data[self.index]
            self.index += 1
            return value
        else:
            raise StopIteration

# 使用
my_iter = MyIterator((1,2,3,'a'))
for num in my_iter:
    print(num)

def my_generator(data):
    for i in data:
        yield i * 2

gen = my_generator(('a','d','a','f'))
for doubled in gen:
    print(doubled)

def fabonacci(n):
    a, b, counter = 0,1,0
    while True:
        if (counter > n):
            return
        yield a
        a, b = b, a + b
        counter += 1
f = fabonacci(10)

while True:
    try:
        print(next(f),end=" ")
    except StopIteration:
        break

print()
with open(r"E:\pythonProject\learnPY2\test_file.txt",'r') as file:
    content = file.read()
    print(content)
def pizza_slicer(pizza_size):
    """无限切披萨的生成器"""
    slices = pizza_size // 8  # 计算能切多少片
    print(slices)
    for slice_num in range(slices):
        yield f"第{slice_num + 1}片披萨"

    yield "披萨切完了！"


# 使用披萨切片机
pizza = pizza_slicer(16)  # 一个16寸的披萨

for slice in pizza:
    print(f"享用: {slice}")


class Timer:
    def __enter__(self):
        import time
        self.start = time.time()
        print(f"start: {self.start:.2f}")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        import time
        self.end = time.time()
        print(f"end: {self.end:.3f}")
        print(f"耗时: {self.end - self.start:.3f}秒")
        return False


# 使用示例
with Timer() as t:
    # 执行一些耗时操作
    sum(range(1000000))

def printinfo(arg1, *vartuple):
     print("output:")
     print(arg1)
     for var in vartuple:
         print(var)
     return

printinfo(10)
printinfo(10,20,30)


def printinfo1(arg1, **vardict):
    print("output:")
    print(arg1)
    print(vardict)
    return


printinfo1(10)
printinfo1(10, a=20, b=30)

sum = lambda a,b: a+b
print("sum:",sum(10,20))

def myfunc(n):
    return lambda a:a*n

mydouble=myfunc(2)
mytriple=myfunc(3)

print(mydouble(11))
print(mytriple(11))


def sum1(arg1, arg2):
    # 返回2个参数的和."
    total = arg1 + arg2
    print("函数内 : ", total)
    print(id(total))
    return total


# 调用sum函数
total = sum1(10, 20)
print("函数外 : ", total)
print(id(total))

def draw_rectangle(x, y, width, height, /, color="black", p=5, *, fill=False):
    print(f"在({x},{y})绘制{width}x{height}的矩形，颜色:{color}, p:{p},填充:{fill}")
draw_rectangle(10, 20, 100, 50)                    # 正确
draw_rectangle(10, 20, 100, 50, color="red",p=4)       # 正确
draw_rectangle(10, 20, 100, 50, fill=True)

def my_decorator(func):
    def wrapper():
        print("before original func running")
        func()
        print("after original func running")
    return wrapper

@my_decorator
def say_hello():
    print("hello")
say_hello()

import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args,**kwargs)
        end = time.time()
        print(f"{func.__name__} run time: {end - start:.2f} seconds")
        return result
    return wrapper

@timer
def slow_func():
    time.sleep(1)
    return("done")

result=slow_func()
print(result)

from collections import deque

q = deque()

q.append('a')
q.append('b')
q.append('c')

print(q)
first_element=q.popleft()
print(first_element)

vec=[2,4,6]
vec1=[3*x for x in vec]
print(vec)
print(vec1)

vec2=[[x,x**2] for x in vec]
print(vec2)

vec3=[1,2,3]
vec4=[x*y for x in vec for y in vec3]
print(vec4)

matrix=[[1,2,3,4],
        [5,6,7,8],
        [9,10,11,12]
        ]
print(matrix)

matrix_r=[[row[i] for row in matrix] for i in range(4)]
print(matrix_r)

matrix_r1=[]
for i in range(4):
    new_row=[]
    for row in matrix:
        new_row.append(row[i])
    matrix_r1.append(new_row)
print(matrix_r1)

import fibo

fibo.fib(100)

print(dir())
print(dir(sys))

print(f"模块的 __name__ 值: {__name__}")

with open("test2.txt",'w+') as fw:
    fw.write("Python 是一个非常好的语言。\n是的，的确非常好!!\n")
    fw.write("确实\n")
    fw.seek(0)
    ct1=fw.read()
print("content:",ct1)
print("done")

with open("test2.txt",'r') as fw:
    i=0
    for line in fw:
        print("line{}:{}".format(i,line),end='')
        i+=1

import pickle,pprint

# 使用pickle模块将数据对象保存到文件
data1 = {'a': [1, 2.0, 3, 4+6j],
         'b': ('string', u'Unicode string'),
         'c': None}

selfref_list = [1, 2, 3]
selfref_list.append(selfref_list)

output = open('data.pkl', 'wb')

# Pickle dictionary using protocol 0.
pickle.dump(data1, output)

# Pickle the list using the highest protocol available.
pickle.dump(selfref_list, output, -1)

output.close()

pkl_file = open('data.pkl', 'rb')

data1 = pickle.load(pkl_file)
pprint.pprint(data1)

data2 = pickle.load(pkl_file)
pprint.pprint(data2)

pkl_file.close()

import os
cur_dir=os.getcwd()
subs=os.listdir()
print(cur_dir)
print(subs)

try:
    with open("test2.txt1",'r') as fw:
        data=fw.read()
except FileNotFoundError as fnf_error:
        print(fnf_error)
else:
    print("no exceptions")
finally:
    print("done")

def add_numbers(a: int, b: int) -> int:
    return a + b

result = add_numbers(5, 3)
print(result)

