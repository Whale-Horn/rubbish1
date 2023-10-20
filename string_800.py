import random
import string

# 定义函数，生成随机字符串
def random_string():
    x = string.ascii_letters
    y = [random.choice(x) for i in range(800)]
    return y

# 调用函数生成随机字符串
y = random_string()

# 创建字典，统计字符频率
d = dict()
for ch in y:
    d[ch] = d.get(ch, 0) + 1

# 对字典按键进行排序
s = sorted(d.items(), key=lambda x: x[0], reverse=True)

# 遍历输出结果
for k, v in s:
print(k, ":", v)






---------------------------------------------------------------------------------------------------------------------------------

import random
import string

#定义字符生成器
def generate_chars():
    x = string.ascii_letters  
    for _ in range(800):
        yield random.choice(x)  

# 生成器实例化
y = generate_chars()  

# 创建空字典，用于统计字符出现的次数
d = dict()  
for ch in y:
    d[ch] = d.get(ch, 0) + 1  

# 对字典按照键进行降序排序
s = sorted(d.items(), key=lambda x: x[0], reverse=True)  

# 逐行输出键值对
for k, v in s:
print(k, '：', v)
