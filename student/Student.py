#-*- coding:utf-8 -*-
'''学生类，用来测试类的，哈哈哈~~'''
class Student(object):

    def __init__(self,name,score):
        self.name=name
        self.score=score

    def Print(self):
        print("%s:%d"%(self.name,self.score))
    def GetGrade(self):
        if self.score>90:
            return 'A'
        elif self.score>80:
            return 'B'
        else:
            return 'C'
