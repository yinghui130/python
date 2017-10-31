#-*-coding:utf-8-*-
import re

obj=re.match(r'^\d{3}-\d{3,8}$','010-8970987')
print(obj.string)
print(type(obj))
str=re.split(r'[\s\,\;]+','a,b;;c d  e')
print(type(str))
print(str)
obj=re.match(r'^(\d{3})-(\d{3,8})$','010-8970987')
print(obj.group(0))
for item in obj.group():
    print(item)