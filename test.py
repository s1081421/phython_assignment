###字串
phrase=("don't smoke")#string
number=69

print(phrase.lower())#小寫
print(phrase.upper())#大寫

print(phrase.islower())#是否小寫
print(phrase.isupper())#是否大寫

print(phrase.index("n"))#判斷n在第幾位

print(phrase.replace("n","!"))#將n換成!

print(str(number)+phrase)#str(number),轉string
### number
mnumber=-69

print(abs(mnumber))#abs(number),絕對值

print(pow(2,4))#pow(x,y),x的y次方

print(max(55,99,999,758,1000000000))#max(),找到最大值

print(round(4.5),round(4.6))#五捨六入

from math import *

print(floor(5.9))#無條件捨去
print(ceil(5.1))#無條件進位

print(sqrt(64))#開根號

print("//////////////////////////")
##list

numberlist=[1,2,3,4,5,6,7,8,9]
stringlist=["幹","你","娘"]

print(numberlist[0:])#從0開始取到底
print(stringlist[0:5])#從0到5

numberlist.extend(stringlist)#extend,從後面加
print(numberlist)

numberlist.append(69)#加一個元素
print(numberlist)

numberlist.insert(5,"!")#插入
print(numberlist)

numberlist.remove(69)#將()中的物件移除
print(numberlist)

numberlist.pop()
print(numberlist)#末位移除

newlist=[999,12,888,757,3,6969,999,82154,3,3]

newlist.sort()#小到大排序
print(newlist)
newlist.reverse()#反轉
print(newlist)

print(newlist.count(3))#數有幾個()中的元素

print(len(newlist))#計算長度

print("//////////////////////////")
###tuple元組 無法被修改

tuple1=(1,2,3,5)

print(tuple1)

print("//////////////////////////")
###Fuction 

def test(word):
    print("work"+word)

def re(num1,num2):
    return num1+num2

print("your  input")
word=input()
test(word)

print(re(11111,22222))
print("//////////////////////////")
###if

check=0
check2=1
if check==1:
    print("yes")
elif check==0:
    print("nooooo")

if check==0 and check2==0:
    print("no way")
else:
    print("that's right")

if check==0 and not (check2 ==0):
    print("OK")

############

dic={0:"jett",1:"viper",2:"sova",3:"sage"}

print(dic[1])

print("//////////////////////////")
### for loop

for num in range(5):
    print(num)

def power (base_num,times):
    answer=base_num
    for num in range(times-1):
        answer=answer*base_num
    return answer

print(power(3,3))
print("//////////////////////////")
###二維陣列及巢狀迴圈

Num_List=[
    [1,2,3,4],
    [5,6,7,8],
    [9,69],
    [6969]
]

for row in Num_List: #每個Num_List 元素 row=行
    for col in row:  #每一行的元素 col=列
        print(col)
print("//////////////////////////")
###讀檔
file=open("infile.txt",mode="a",encoding="utf-8")#mode="r" 只讀,mode="w" 只寫,mode="a" 修改,encoding="utf-8"支援中文

#print(file.read())
#print(file.readline())#只讀一行
#file.write("don't get in my way")
file.write("\n__viper我老婆")

file.close()

print("//////////////////////////")
###module

import tool

print(tool.BMI(tool.height,tool.weight))

import token
import sys

print(sys.path)
##pip套件管理工具 terminal-> pip install XXX

import numpy as np # as 將numpy 改名成np
print("//////////////////////////")
###CLASS   

class Phone:
    def __init__(self,os,numberr,is_waterproof):
        self.os=os
        self.numberr=numberr
        self.is_waterproof=is_waterproof

phone1 =Phone("Android","09888888888" ,True)
print("//////////////////////////")
### 問答程式

test2 =[
    "1+3=?\n(a) 2\n(b)3\n(c)4\n\n",
    "1公尺=幾公分\n(a)10\n(b)100\n(c)1000\n\n",
    "香蕉甚麼顏色\n(a)黑色\n(b)黃色\n(c)藍色\n\n"
]

from tool import Question

questions =[
    Question(test2[0],"c"),
    Question(test2[1],"b"),
    Question(test2[2],"b")
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.description)#question.desription 會被print出來
        if answer == question.answer:
            score += 1
    print("你得到"+str(score)+"分")

run_test(questions)
print("//////////////////////////")
###繼承

from tool import Person

class Student(Person):
    def __init__(self, name, age,school):
        self.name=name
        self.age=age
        self.school=school
    def student_school(self):
        print(self.school)
        
student1 = Student("David",21,"元智")

student1.person_name()
student1.person_age()
student1.student_school()
