import re

# text = "\tbc"

# 匹配某个字符
# ret = re.match('a', text)

# .: 匹配任意的字符（除了'\n')
# ret = re.match('.', text)

# \d: 匹配任意的数字
# ret = re.match("\d", text)

# \D: 匹配任意的非数字
# ret = re.match("\D", text)

# \s: 匹配的是空白字符（\n，\r，\t和空格）
# ret = re.match("\s", text)

# \S: 匹配非空白字符
# ret = re.match("\S", text)

# \w: 匹配a-z,A-Z,数字以及下划线
# ret = re.match("\w", text)

# \W: 匹配的和'\w'相反
# ret = re.match("\W", text)

# []: 组合方式，满足[]中任意一项都算匹配成功
# ret = re.match("[^\n\tac]", text)

# print(ret.group())


# text = "apple price is $99, orange price is $88"
# result = re.search('.+(\$\d+).+(\$\d+)', text)
# print(result.group())
# print(result.group(0))
# print(result.group(1))
# print(result.group(2))
# print(result.groups())

text = "apple price is $99, orange price is $88"

rr = re.compile(r'\$\d+')
res1 = rr.findall(text)
print(res1)

res2 = re.match(r'\w+ \w+', text)
print(res2.group())

res3 = re.search(r'\$\d+', text)
print(res3.group())

res4 = re.findall(r'\$\d+', text)
print(res4)

res5 = re.finditer(r'\$\d+', text)
print('----------------------')
for i in res5:
    print(i.group())
print('----------------------')

res6 = re.split(r' |,', text)
print(res6)

res7 = re.sub(r' |,', '*', text)
print(res7)
