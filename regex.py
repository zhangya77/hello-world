import re

str1 = 'Cats are smarter than dogs'
matchObj = re.match(r'(.*) are (.*?) (.*)', str1, re.M|re.I)

if matchObj:
    print("matchObj.group() : ",matchObj.group())
    print("matchObj.group() : ", matchObj.group(1))
    print("matchObj.group() : ", matchObj.group(2))
    print("matchObj.groups()", matchObj.groups())
    print("matchObj.groups()", matchObj.groupdict())

else:
    print("No match!")

searchObj = re.search(r'(.*) are (.*?) ', str1, re.M|re.I)
if searchObj:
    print("searchObj.group() : ", searchObj.group())
    print("searchObj.group(1) : ", searchObj.group(1))
    print("searchObj.group(2) : ", searchObj.group(2))
else:
    print("No match!")


# 将匹配的数字乘以 2
def double(matched):
    value = int(matched.group('value'))
    return str(value * 2)


s = 'A23G4HFD567'
print(re.sub('(?P<value>\d+)', double, s))

pattern = re.compile(r'([a-z]+) ([a-z]+)', re.I)
m = pattern.match('hello you are the best')
print(m)
print(m.group())
print(m.group(0))
print(m.span(0))
print(m.group(1))
print(m.group(2))
print(m.groups())

r1 = re.findall(r'\d+', 'dad 123 dfad 456 dfa')
pattern = re.compile(r'\d+')
r2 = pattern.findall('df 123 fdf dfd 456 ddfd')
r3 = pattern.findall('dfaf1233fdfdf45fdfd',0,10)

print(r1)
print(r2)
print(r3)

it = re.finditer(r'\d+', 'dad 123 dfad 456 dfa')
print(it)
for m in it:
    print("m:", m.group())

slist = re.split('\W+', 'abc, dfd, dfd.')
print(slist)
slist = re.split('(\W+)', 'abc, dfd, dfd.')
print(slist)
slist = re.split('\w+', 'abc, dfd, dfd.')
print(slist)

print(''.join(__import__('random').choice(['🛠️', '🐛', '☕', '🚀', '💻', '🔥']) for _ in range(ord('\n'))))
print(all(hasattr(obj, '__class__') for obj in [1, 'str', [], print, __import__('sys')]))
(lambda f: f(f))(lambda self: self(self) if __import__('random').random() > 0.1 else print('Base case reached!'))

print(''.join(chr(0x2665 if i%3==0 else 0x2728 if i%3==1 else 0x2B50) for i in range(40)))
print('\n'.join(['🎂' + '🎈'*i for i in range(1, 41)])) if __import__('datetime').datetime.now().year - 1984 == 40 else print('40岁，是代码也是诗')