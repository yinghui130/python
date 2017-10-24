# -*- coding:utf-8 -*-
from operator import itemgetter
from student.Student import Student as St
from jsonEncode.jsonEncode import ComplexEncoder
import sys
import datetime
import os
import jsonplus  as  json
from multiprocessing import Process


print('hello world')
List1 = []
List1 = sorted(['bob', 'abc', 'Zoo', 'Monkey'], key=str.lower, reverse=True)

print(List1)

students = [('bob', 75), ('abc', 100), ('Zoo', 99), ('Monkey', 45)]

print(sorted(students, key=itemgetter(0)))
print(sorted(students, key=lambda x: x[1]))
print(sorted(students, key=itemgetter(1), reverse=True))


def log(func):
    def wrapper(*args,**kw):
        print('call %s()' % func.__name__)
        return func(*args,**kw)
    return wrapper

@log
def now(a):
    print('2017-09-24')
    print(a)

now("liuyinghui")

print(now.__name__)
print(sys.path)

std=St("liuyinghui",100)
std.score=85
std.Print()
print(std)
print(St)
print(std.GetGrade())

f=open("d:/hello.txt",'rb')
string1=f.readline()
print((string1))
string2=str(string1)
print((string2))
f.close()
with open("d:/hello.txt",'r') as f:
    string3=f.read()
    print(string3)

with open("d:/hello.txt",'a') as f:
    flag=f.writable()
    string3=f.write("\n刘颖慧，你好！！")
    print(string3)
    print(flag)

#os.mkdir('d:/liuyinghui')
#os.rmdir('d:/liuyinghui')
print(os.name,os.environ['OS'])
jsonDict= dict(name='liuyinghui',age=35,datetime=datetime.datetime.today())
jsonstr=json.dumps(jsonDict)
print(jsonstr)
print(jsonDict)
jsonDict2=json.loads(jsonstr)
print(jsonDict2)
print(json.dumps(std.__dict__))
print(type(std))
def jsonHanle(d):
    return St(d['name'],d['score'])
std1=json.loads(json.dumps(std.__dict__),object_hook=jsonHanle)
print(std1)
print(type(std1))
'''
print('Process (%s) start ...'%os.getpid())
pid = os.fork()
if pid==0:
    print('I am child process(%s) and my parent is %s'%(os.getpid(),os.getppid()))
else:
    print('I (%s) just created a child process(%s)' %(os.getpid(),pid))
'''
def run_proc(name):
    print('run childe process %s(%s)....'%(name,os.getpid()))

if __name__=='__main__':
    print("parent process %s."%os.getpid())
    p=Process(target=run_proc,args=('test',))
    print('child process will start...')
    p.start()
    p.join()
    print('child process end..')