# -*- coding: utf-8 -*-
"""
Author: niziheng
Created Date: 2022/10/4
Last Modified: 2022/10/4
Description: 
"""
import re


pattern = 'this'
text = 'does this text match?'

# re.search()，文本搜索
match = re.search(pattern, text)

# 如果匹配成功则会返回一个Match对象，匹配失败则返回None

# 匹配起始索引，结束索引
start = match.start()
end = match.end()

# 匹配到的字符串
match_string = text[start: end]
print(match_string)
