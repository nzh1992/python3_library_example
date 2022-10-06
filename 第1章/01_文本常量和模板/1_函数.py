# -*- coding: utf-8 -*-
"""
Author: niziheng
Created Date: 2022/10/4
Last Modified: 2022/10/4
Description: 
"""
import string

# 1.string.capwords()
# 把一个字符串中所有单词的首字母都改为大写
s1 = "this a string"
cap_s1 = string.capwords(s1)
# print(cap_s1)   # output: "This A String"


# 2.string.Template()
# 创建一个字符串模板，用$标识符表示变量($var, 或${var})
template = string.Template("""
name: $name,
age: ${age},
address: china $address, 
""")

data = {
    'name': 'aaa',
    'age': 20,
    'address': 'shanghai'
}

result = template.substitute(data)
print(result)

# 注意：
# 1. $ 和 % 作为触发字符串，如果想作为字符使用时，需要转义。连续输入两次表示转义
t2 = string.Template("""
name: $$,
age: $$${age}
""")

result2 = t2.substitute(data)
print(result2)