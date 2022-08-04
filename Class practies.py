                            #Day 1 class practice
# python file extension in.py
# Python language was developed using C language

# python allocate memory dynamically based ont the value
"""a=7669986746767576697098079685744355235465789098324657890435678908898542076857354345658
print("python allocate memory:-",a)"""
# python memory
"""tsr1=10
tsr2=10
tsr3=10
tsr4=10
tsr5=10                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
tsr6=10
tsr7=10
print("id() gives address of the variable:-",id(tsr1))
print(id(tsr2))
print(id(tsr3))
print(id(tsr4))
print(id(tsr5))"""

# The print output
"""print("hello")
print("welcome to python progamming")
print("chittoor")
print("123")
print("welcome to python class")
print("data types, numb list, string, set, tuple, dict")"""
# comments
# single line comments "#"
# multi line comments " """ """ "

# indexing
# bwd;-5,-4,-3,-2,-1
"""tkg=[10,20,30,40,50]
# fwd 0, 1, 2, 3, 4
print("0 index of tkg:",tkg[0])
print("1st index of tkg:",tkg[1])
print("2nd index of tkg:",tkg[2])
print("3thd index of tkg:",tkg[3])
print("4th index of tkg:",tkg[4])

# Bwd
print("-1 index of tkg:",tkg[-1])
print("-2 index of tkg:",tkg[-2])
print("-3 index of tkg:",tkg[-3])
print("-4 index of tkg:",tkg[-4])
print("-1 index of tkg:",tkg[-5])


# Data Types
# Numbers,list,Strings,Tuple,Set, Dict

# Numbers
# 1. Int       10
# 2. Float     78.998
# 3. Complex   1+2j

t = 10,19,29,30,40,50
s = 78.998,49.5559,49559.000,3000.500
r = 1+2j
print("int:-",(t))
print("float:-",(s))
print("complex:-",(r))
# type(), Gives the type of the object
print("type(), Gives the type of the object:-",type(t))
print("type(), Gives the type of the object:-",type(s))
print("type(), Gives the type of the object",type(r))
"""

# List
"""tsrlist =[10,20,"hell0",40.59,30,40]
print(tsrlist)
print("can store any type of Data Type with []:-",tsrlist)
print("type of the tsr:-",tsrlist)

#tuple
tsrtuple=(10,20,"python",30,40,40,45.4555)
print(tsrtuple)
print("type(), Gives the type of the object",type(tsrtuple))
print("can store any type of Data Type with():-",tsrtuple)

#string
tsrstr="welcome to python programming"
print(tsrstr)
print("type(), Gives the type of the object",type(tsrstr))
print("can store any type of Data Type with "":-",tsrstr)"""

#set
"""tsrset = {1,2,4,5}
print(tsrset)
print("type(), Gives the type of the object",type(tsrset))"""

#Dict
"""tsrdict = {1: 100, 2:200}
print(tsrdict)
print("type(), Gives the type of the object",type(tsrdict))"""

                            # Day 2 class practice

                                    # List
# Collection - Order - Means supports indexing
# Mutability - Mutable(Changable)

"""tsrlist = [10,20,30,40,"hello",(10,20,30,),{1:909099,3:34444,45:000}]
print("tsrlist is",tsrlist)
print("type(),Gives the type of the object",type(tsrlist))
print("1st index of tsrList is ",tsrlist[1])
print("-1 index of tsrList is ",tsrlist[-1])
print("-2 index of tsrList is ",tsrlist[-2])
print("3trd index of tsrList is ",tsrlist[3])
print("4th  index of tsrList is ",tsrlist[4][0])
print("6th index of tsrList is ",tsrlist[6][1])
print("-1[0] index of tsrList is ",tsrlist[-2][0])"""
#reassing list elements
"""tsr1list = [10,20,30,40,"hello",(10,20,30,),{1:909099,3:34444,45:000}]
tsr1list[2]=344
print("tsr1List after update is ",tsr1list)
tsr1list[4]="welcome to python programming language"
print("tsr1List after update is ",tsr1list)
tsr1list[-1][45]="hello"
print("tsr1List after update is ",tsr1list)
tsr1list[6][1]="sasidhr"
print("tsr1List after update is ",tsr1list)
tsr1list[6][3]=2323
print("tsr1List after update is ",tsr1list)"""

                                    #tuple
# Collection - Order - Means supports indexing
# Mutability - ImMutable(Not Changable)
tsrtuple = (10,20,30,40,50,55,60)
"""print("type(),Gives the type of the object",type(tsrtuple))
print("1st index of tsrtuple is ",tsrtuple[1])
print("-1 index of tsrtuple is ",tsrtuple[-1])
print("-2 index of tsrtuple is ",tsrtuple[-2])
print("3trd index of tsrtuple is ",tsrtuple[3])
print("2nd index of tsrtuple is ",tsrtuple[2])
print("tsrtuple is ",tsrtuple)"""

"""tsrtuple[2]=500
print("myTuple after update is ",tsrtuple)
TypeError: 'tuple' object does not support item assignment"""

                                    # String
# Collection - Order - Means supports indexing
# Mutability - ImMutable(Not Changable)
"""
tsrstr1 = "welcome to python"
print("type(),Gives the type of the object",type(tsrstr1))
print("1st index of tsrstr1 is ",tsrstr1 [1])
print("-1 index of tsrstr1  is ",tsrstr1 [-1])
print("-2 index of tsrstr1 is ",tsrstr1 [-2])
print("3trd index of tsrstr1 is ",tsrstr1[3])
print("2nd index of tsrstr1 is ",tsrstr1[2])
print("tsrstr1 is ",tsrstr1)
"""
"""
tsrstr1[4]="wilkldlkfhslf"
print("tsrstr1 after update is ",tsrstr1)
TypeError: 'str' object does not support item assignment
"""


                                        # Set
# Collection - UnOrder - Means supports doesnt indexing
# Mutability - Mutable(Changable)
"""
tsr3set = {1,2,4,5,6,7,8}
print(" tsr3of mySet is ",type(tsr3set))
print("mySet is",tsr3set)
tsr3set.add(50)
print(tsr3set)
tsr3set.add(34)
print(tsr3set)
tsr3set.add(343434)
print(tsr3set)
tsr3set.add(454)
print(tsr3set)
tsr3set.remove(1)
print(tsr3set)
tsr3set.remove(2)
print(tsr3set)
tsr3set.remove(5)
print(tsr3set)

#Can not support index
#print("1st index of tsr3set is ",tsr3set [1])
#TypeError: 'set' object is not subscriptable
"""

                                # Dict
# Collection - UnOrder - Means supports doesnt indexing
# Mutability - Mutable(Changable)

# Important Note-
# Keys - Only immutable data types eligible
# Values - Can be of any type

tsr3dict = {200:234, 12: 45, "number":6, (14,5,4,4): 300,"chittoor":143}
print("tsr3dict[12] is ",tsr3dict)
tsr3dict[200] = "python"
print(tsr3dict)
tsr3dict[12] = 3059
print(tsr3dict)
tsr3dict["number"] = 103848
print(tsr3dict)
tsr3dict[(14,5,4,4)] = "sasidhar"
print(tsr3dict)
tsr3dict["chittoor"] = "welcome to python programming language"
print(tsr3dict)


# Understanding the True/False with data type context

# Number

# True - Except 0(ZERO) everything is True only even if it is negative num(-23)
# False - Only 0(ZERO)

# List :
# True - Other than empty list all are True only(Ex: myList = [1,2,3])
# False- Empty List (Ex: myList = [])

# Tuple :
# True - Other than empty tuple all are True only(Ex: myTuple = (1,2,3))
# False- Empty Tuple (Ex: myTuple = ())

# String:
# True - Other than empty string all are True only(Ex: myStr= "India")
# False- Empty String (Ex: myStr = "" )

# Set:
# True - Other than empty set all are True only(Ex: mySet={1,2,3})
# False- Empty Set (Ex: mySet = set() )

# Dict:
# True - Other than empty dict all are True only(Ex: myDict={1:100,2:500})
# False- Empty Dict (Ex: myDict = dict() )


# Conditional Statements
"""Equals: 10== 10
Not Equals: 10 != 9
Less than: 8 < 9
Less than or equal to: 10<= 10
Greater than: 100 > 99
Greater than or equal to: 10 >= 0"""

#if only:-

"""if 10>5:
    print("10>5 is:-",10>5)
if 10 > 4:
  print("10 is greater than 4")
if 3<5:
    print("3<5 is ",3<5)
if 100>99:
    print("100>99 is ",100>99)
if 100>=100:
    print("100>=100 is",100>=100)
if 100<=1000:
        print("100<=23 is",100<=23)
if 100<=123:
        print("100<=23 is", 100<= 23)
if 100==100:
    print("100==100 is",100==100)"""


# if and else:-
"""
if 5>3:
    print("true")
else:
    print("false")
if 5<10:
    print("true")
else:
    print("false")

if 15>=343:
    print("true")
else:
    print("false")
if 25 >100:
  print("true")
else:
  print("false")
"""
#elif
"""
if 10 > 5:
  print("true")
elif 10==5:
  print("false")
else:
  print("false")


if 8 > 8:
  print("false")
elif 19<20:
  print("true")
else:
  print("false")

if 8 > 8:
  print("false")
elif 19<15:
  print("false")
else:
  print("true")

if 8> 8:
  print("false")
elif 19<15:
  print("false")
elif 10==10:
  print("True")
else:
  print("true")
"""
#And -Both conditions are True
"""
if 10 >8 and 5>2:
  print("Both conditions are True")

if 5>8 and 1>2:
  print("Both conditions are False")

if 200 >34 and 34>24:
  print("Both conditions are True")

if 1>8 and 19>2231:
  print("Both conditions are False")
"""
#or - At least one of the conditions is True
"""
if 10 > 3 or 10 > 11:
  print("At least one of the conditions is True")

if 1 > 3 or 12> 11:
  print("At least one of the conditions is True")

if 1 > 10 or 9 > 11:
  print("All conditions are false conditions - false")
"""

# Membership Operators
# in , not in
# in
tsrList = [2,3,4,34,56,98]
print(2 in tsrList)
print(34 in tsrList)
print(56 in tsrList)
print(45 in tsrList)
print(69 in tsrList)
print(1 in tsrList)

#not in

print(2 not in tsrList)
print(34 not in tsrList)
print(56 not in tsrList)
print(45 not in tsrList)
print(69 not in tsrList)
print(1 not in tsrList)

                                    # Day 4 class practice
"""
tsrList = [2,3,4,34,"hello",(1,2,3),{"keyword":98},{32,45,67}]
print(2 in tsrList)
print("hello" in tsrList)
print((1,2,3) in tsrList)
print("keyword" in tsrList)
print({32,45,67} in tsrList)
print(1 in tsrList)

#not in

print(2 not in tsrList)
print("hello"not in tsrList)
print((1,2,3) not in tsrList)
print("keyword" not in tsrList)
print({32,45,67} not in tsrList)
print(1 not in tsrList)
"""
"""
tsrtuple = [2,3,4,34,"hello",(1,2,3),{"keyword":98},{32,45,67}]
print(2 in tsrtuple)
print("hello" in tsrtuple)
print((1,2,3) in tsrtuple)
print("keyword" in tsrtuple)
print({32,45,67} in tsrtuple)
print(1 in tsrtuple)

#not in

print(2 not in tsrtuple)
print("hello"not in tsrtuple)
print((1,2,3) not in tsrtuple)
print("keyword" not in tsrtuple)
print({32,45,67} not in tsrtuple)
print(1 not in tsrtuple)

"""
"""
tsrset = {2,3,4,34,"python",(1,2,3)}
print(2 in tsrset)
print("python" in tsrset)
print((1,2,3) in tsrset)
print(3 in tsrset)
print({32,45,67} in tsrset)
print(1 in tsrset)

#not in

print(2 not in tsrset)
print("python"not in tsrset)
print((1,2,3) not in tsrset)
print(4 not in tsrset)
print({32,45,67} not in tsrset)
print(1 not in tsrset)
"""
"""
tsrdict = {"keyword":12,"python":"welcome",1232:"sasdihar"}
print("keyword" in tsrdict)
print("python" in tsrdict)
print(1232 in tsrdict)

#not in

print("keyword" not in tsrdict)
print("python" not in tsrdict)
print((1232) not in tsrdict)

tsrstr = "welcome to python programming"
print("o" in tsrstr)
print("p" in tsrstr)
print("c" in tsrstr)
print("r" in tsrstr)
print("t" in tsrstr)
print("mm" in tsrstr)

#not in

print("r" not in tsrstr)
print("t" not in tsrstr)
print("mm" not in tsrstr)
print("o" not in tsrstr)
print("p" not in tsrstr)
print("c" not in tsrstr)
print("r" not in tsrstr)
"""



"""
if 8<3:
    print("India")
elif 4<3:
    print("AUS")
elif 9<3:
    print("EU")
else:
    print("USA")
"""
"""
if 10<20 :
    print("gowthami")
elif 4<3:
    print("mounika")
elif 9<3:
    print("vidya")
elif 10==10:
    print("KXN")
else:
    print("sasidhar")

if 10<9 :
    print("gowthami")
elif 4<13:
    print("mounika")
elif 9<3:
    print("vidya")
elif 10==10:
    print("KXN")
else:
    print("sasidhar")

if 10<9 :
    print("gowthami")
elif 4<3:
    print("mounika")
elif 9<10:
    print("vidya")
elif 10==10:
    print("KXN")
else:
    print("sasidhar")

if 10<9 :
    print("gowthami")
elif 4<3:
    print("mounika")
elif 9<3:
    print("vidya")
elif 10==10:
    print("KXN")
else:
    print("sasidhar")

if 10<9 :
    print("gowthami")
elif 4<3:
    print("mounika")
elif 9<3:
    print("vidya")
elif 10==9:
    print("KXN")
else:
    print("sasidhar")
"""
"""
import time
for item in [1,2,3,4]:
    print(item)
    time.sleep(1)

for item in (1,2,3,4):
    print(item)
    time.sleep(1)

for item in ("welcome"):
    print(item)
    time.sleep(1)

for item in {1,2,3,(1,2,3)}:
    print(item)
    time.sleep(1)

for item in {"key:valu","value:12",(10,20,30)}:
    print(item)
    time.sleep(1)
"""
#import time
"""
tsrlist =range(10)
for item in tsrlist:
    if item %3==0:
        print(item)
    time.sleep(0.5)

tsrlist =range(15)
for item in tsrlist:
    if item %5==0:
        print(item)
    time.sleep(0.5)
"""
"""tsrlist =range(15)
for item in tsrlist:
    if item %3==0:
        print(item)"""
"""
tsrlist =range(15)
for item in tsrlist:
    if item %2==0:
        print("Even number",item)
    #else:
        #print("odd number",item)


tsrlist =range(15)
for item in tsrlist:
    if item %2==0:
        print("Even number",item)
    #else:
       #print("odd number",item)

tsrlist =range(230)
for item in tsrlist:
    if item %2==0 and item%3==0:
        print("Even number",item)
    else:
        print("odd number",item)
        time.sleep()
"""

 # 5th day class
#for loop:
"""
for item in [1,2,3,4]:
    print(item)
"""
#for t in [1,2,3,4]:
   # print(t)
#for t in "sasidhar":
   # print(t)

#while loop
"""s=0
while s<20:
    print(s)
    s=s+2
"""
"""
n=int(input("Enter the n value"))
i=0
while i<=n:
    print(i,end=" ")
    i=i+1
"""
"""
tsrlist =range(10)
for sagar in tsrlist:
    if sagar %3==0:
        print("sagar is hero:-",sagar)
"""
"""
tsrlist =range(10)
for item in tsrlist:
    if item %3==0:
        print(item)
"""
"""
import time
sasidhar =range(23)
for item in sasidhar:
    if item %2==0 and item%3==0:
        print("Even number",item)
    else:
        print("odd number",item)
        time.sleep(0.5)
"""
""""
i=0
while i<120:
    print(i,end=" ")
    i=i+1
"""
#a=20
#while a<100:
    #print(a,end=" ")
    #a=a+5
"""
# function:
# a functions i a block of reusable code which executes when we call the fuction
"""
# systax
"""
"""
"""
def<function_name> (<parameters>):
        <statements>"""

# function definitions:
"""def functionname (input1,input2):
    print("Fuction name is ",input1,input2)
functionname(20,40)
"""

#addition:-
"""
def addition (input1,input2):
    print("addition",input1,input2)
addition(20,40)

def additon(a,b):
    print("additionis",a+b)
additon(20,40)

def additon(sasidhar,b):
    print("additionis",sasidhar+b)
additon(20,40)

def apple (sasidhar,gowthami):
    print("aplles ate",sasidhar+gowthami)
apple (20,40)
"""

#multiplication

"""
def multiplication(a,b):
    print("Mutiplication is",a*b)
multiplication(19,23)

def multiplication (input1,input2):
    print("mutiplication is ",input1*input2)
multiplication(39,600)

def multiplication (sasidhar,b):
    print("multiplication is",sasidhar*b)
multiplication(45,40)

def apple (sasidhar,gowthami):
    print("apples muliplication is",sasidhar*gowthami)
apple (223,40)
"""


#Subtraction

"""
def Subtraction(a,b):
    print("Subtractionis",a-b)
Subtraction(19,23)

def Subtraction (input1,input2):
    print("Subtraction is ",input1-input2)
Subtraction(39,600)

def Subtraction (sasidhar,b):
    print("Subtraction is",sasidhar-b)
Subtraction(45,40)

def apple (sasidhar,gowthami):
    print("apples Subtractionis",sasidhar-gowthami)
apple (223,40)
"""

#Division:

"""
def Division(a,b):
    print("Divisionis",a/b)
Division(19,23)

def Division (input1,input2):
    print("Division is ",input1/input2)
Division(39,600)

def Division (sasidhar,b):
    print("Division is",sasidhar/b)
Division(45,40)

def apple (sasidhar,gowthami):
    print("apples Divisionis",sasidhar/gowthami)
apple (223,40)
"""

#list in operator

""""
def list(a,b):
    print("list of addition",a,b)
list(a=[12,34,56],b=[34,45,45])

def list(a,b):
    print("list of addition",a+b)
list(a=[12,34,56],b=[34,45,45])
"""
"""
def tuple(a,b):
    print("tuple function ",a,b)
tuple(a=(12,34,56),b=(22,43,54,54))

def tuple(a,b):
    print("tuple of addition", a+b)
tuple(a=(12,34,56),b=(22,43,54,54))

def set(a,b):
    print("set function", a,b)
set(a={12,34,34,55,45},b={12,343,5433,5344})

def set(a,b):
    print("set function", a+b)
set(a={12,34,34,55,45},b={12,343,5433,5344})
TypeError: unsupported operand type(s) for +: 'set' and 'set'

"""

"""def addition(input1,input2):
    print("type of input1 is",type(input1))
    print("type of input2 is",type(input2))
    if type(input1)==int and type(input2)==int:
        print("addition is",input1+input2)
    else:
     if type (input1)!=int:
        print("input1 is invalied value for operator")
     if type (input2) !=int:
        print("input2 is invalied please pass only inter type")
addition(10,12)
"""

"""
def addition(t,s):
    print("type of t is",type(t))
    print("type of s is",type(s))
    if type(t)==int and type(s)==int:
        print("addition is",t+s)
    else:
     if type (t)!=int:
        print("t is invalid value for operator")
     if type (s) !=int:
        print("s is invalid please pass only inter type")
addition("sasidhar",20)


def addition(input1,input2):
    print("type of input1 is",type(input1))
    print("type of input2 is",type(input2))
    if type(input1)==int and type(input2)==int:
        print("addition is",input1+input2)
    else:
     if type (input1)!=int:
        print("input1 is invalied value for operator")
     if type (input2) !=int:
        print("input2 is invalied please pass only inter type")
addition(10,"sasidhr")
"""
"""
def multiplication(a,b):
    print("type of a is",type(a))
    print("type of b is",type(b))
    if type(a)==int and type(b)==int:
        print("multiplication is",a*b)
    else:
     if type (a)!=int:
        print("a invalid value for operator")
     if type (b) !=int:
        print("b is invalid please pass only inter type")
multiplication(1023,1212)
"""
"""
def Subtraction(python,java):
    print("type of pyhton is",type(python))
    print("type of java is",type(java))
    if type(python)==int and type(java)==int:
        print("Subtraction is",python-java)
    else:
     if type (python)!=int:
        print("input1 is invalied value for operator")
     if type (java) !=int:
        print("input2 is invalied please pass only inter type")
Subtraction(10,12)

"""

"""
def Subtraction(python,java):
    print("type of pyhton is",type(python))
    print("type of java is",type(java))
    if type(python)==int and type(java)==int:
        print("Subtraction is",python-java)
    else:
     if type (python)!=int:
        print("python is invalied value for operator")
     if type (java) !=int:
        print(" java is invalid please pass only inter type")
Subtraction(10,34)

"""
"""
def addition (tsr,kxn):
    print("type of tsr is",type(tsr))
    print("type of kxn is",type(kxn))
    if type(tsr)==float and type(kxn)==float:
        print("addition is",tsr+kxn)
    else:
     if type (tsr)!=float:
        print("tsr is invalid value for operator please enter only float")
     if type (kxn)!=float:
        print("kxn is invalid please pass only float type")
addition(10.23,10)

def subtraction (kcr,ysr):
    print("type of kcr is",type(kcr))
    print("type of ysr is",type(ysr))
    if type(kcr)==float and type(ysr)==float:
        print("subraction is",kcr-ysr)
    else:
        if type (kcr)!=float:
            print("kcr is invalid value for operator please enter only float")
        if type (ysr)!=float:
            print("ysr is invalid please pass only inter type")
subtraction(23.23,"sasdhar")


def Multiplication (sagar,hyt):
    print("type of sagar is",type(sagar))
    print("type of hyt is",type(hyt))
    if type(sagar)==float and type(hyt)==float:
        print("Multiplication is",sagar*hyt)
    else:
     if type (sagar)!=float:
        print("sagar is invalid value for operator please enter only float")
     if type (hyt)!=float:
        print("hyt is invalid please pass only float type")
Multiplication(1033.09889,92.4555)

"""
def Division (chittoor,tirupati):
# defin a function with meaning fullname which suility for the functionalty with required paramerts
    print("type of chittoor is",type(chittoor))
# check the type of parament for our debugging purpose
    print("type of tirupati is",type(tirupati))
    if type(chittoor)==float and type(tirupati)==float:
# put condition to check given input parameters float type or not,if condition satisfied do division functionlty
        print("Division is",chittoor%tirupati)
    else:
# if above condition in failed send the properesponse to the end user to notily proper error mes
     if type (chittoor)!=float:
        print("chittoor is invalid value for operator please enter only float")
     if type (tirupati)!=float:
        print("tirupati is invalid please pass only float type")
Division(1033.09889,3492.4555)

"""                                           #function
#a functions i a block of reusable code which executes when we call the function
# systax
def<function_name> (<parameters>):
        <statements>

#function definitions
def function_name(a,b):
    print(a,b)
function_name(10,30)
#function call

def add(a,b):
    print("addition is",a+b)
add(20,30)


def add(a1.b2):
    C=a1+b2
    print(c)
add(c)

def addition(a,b):
    print("type of a is",type(a))
    print("type of a is",type(b))
    if type(a)==int and type(b)==int:
        print("addition is", a+b)
    else:
        if type(a)!=int:
            print("a is invalid please enter only integers ")
        if type(b)!=int:
            print("b is invalid please enter only integers")
addition(100,30)


"""
"""
#sequenltial execution: if
a=1
if a==1:
    print(a)

#condtional statement: (if else,if elif,else,)
#if else
if a>b:
    print("a is big")
else:
    print("b is big")

#if elif,else
if 10<20 :
    print("sr puram")
elif 4<3:
    print("chittoor")
elif 9<3:
    print("tiurpati")
elif 10==10:
    print("KXN")
else:
    print("sasidhar")

a=int(input("enter the a:"))
b=int(input("enter the b:"))
if a>b:
    print("a is greater than b")
elif a<b:
    print("a is smaller than b")
else:
    print("both are equal")

#iterative statments 
#while loop
s=0
while s<20:
    print(s)
    s=s+2
n=int(input("enter the n value:")
i=0
while i<=n:
    print(i)
    i=i+1
#for loop
for item in[1,2,3,4,5]:
    print(item)
for item in "sasidhar":
    print(item)
tsrlist=range(20)
for item in tsrlist:
    if item %2==0:
        print(item)
tsrlist1=range(30)
for item in tsrlist1:
    if item %3==0: and %5==0:
      print("Even number")
    else:
        print("odd number")

tsrlist1=range(30)
for item in tsrlist1:
    if item %2==0 and item %1==0:
      print("Even number")
    else:
      print("odd number")   

#member ship operatior(in, not in)
tt=[12,34,45,67,"hello",(1,2,3,4),{"key":12,"hight":1},{1,2,3,45}]
t=(30,40,50,56,70)
print(34 in t)
print(40 in t)
print(34 not in tt)
print(40 not in tt)
"""

"""
                            #list practices
#List is mutalbe(changable)
#list is ordered
#list is index support
a=[12,34,45,67,"hello",(1,2,3,4),{"key":12,"hight":1},{1,2,3,45}]#creating list
print("type is",type(a))
print("index number is", a[4])#indexing(0,1,2,3,4)
a[5]="welcome to python"#reassing the value
print(a)
print(a[2:6])#slicing

t=[23,45,"python",45,56]
t1=[34,56,90,45,66]
#basic operation
print("addition is",t+t1)#concatenation
print("mulitification is",t1*4)
print("len of the t",len(t))
print("max of the t",max(t1))
print("min of the t",min(t1))
print("sum of the t",sum(t1))

#built-in methods
s=[23,43,45,65,66,78]
s1=[23,43,45,65,66,78]
s.append(10)# adds an element at the end of the list
print(s)
s.extend([345665,898,899,990])
print("add the more number",s)
s1.insert(3,34)#add an elements at the specified postiion
print(s1)
s1.remove(23)# remove the specified value
print(s1)
s1.pop(5)#pop remove the index value
print(s1)
s1.sort()#sort the list
print(s1)
s2=[23,43,45,65,66,78]
print(s2.count(45))
s2.reverse()
print(s2)


                                             ##tulpe##                   
#tulpe is immutalbe (not changable)
#tuple is ordered
#tuple is index support

tt=(12,34,45,67,"hello",(1,2,3,4),{"key":12,"hight":1},{1,2,3,45})#creating tuple
print("creating tuple",tt)#print
print("indexing",tt[2])#indexing
print("slicing",tt[2:6])#slicing
"""
# tt[3]=45
# print("reassing is",tt)
# TypeError: 'tuple' object does not support item assignment
"""
ss1=(12,34,54)
ss11=(34,56,90,45,66)
#basic operass1ion
print("addiss1ion is",ss1+ss11)#concass1enass1ion
print("muliss1ificass1ion is",ss11*4)
print("len of ss11 is",len(ss11))
print("max of ss11 is",max(ss11))
print("min of ss11 is",min(ss11))
print("sum of ss11 is",sum(ss11))

"""
# strings#

# strings is immutalbe (not changable)
# strings is ordered
# string is index support

"""
s1="welcome to python programming"#creating tuple
print("creating string",s1)#print
print("creating string",type(s1))#print
print("indexing",s1[2])#indexing
print("slicing is",s1[2:])#slicing


str1="sasdihr"
str2="chittoor"
#basic operass1ion
print("addiss1ion is",str1+str2)#concass1enass1ion
print("muliss1ificass1ion is",str2*4)
print("len of str2 is",len(str2))
print("max of str2 is",max(str2))
print("min of str2 is",min(str2))
#print("sum of str2 is",sum(str2))
#TypeError: 'str' is an invalid keyword argument for print()

str3="sasidhar"
str4="alad123"
str5="1234543"
print(str3.capitalize())
print(str3.center(23,"*"))
print(str3.count("s"))
print(str3.endswith("har"))
print(str3.startswith("sasi"))
print(str3.find("a"))# find the index value
print(str3.index('a'))
print(str3.rfind("a"))
print(str4.isalpha())
print(str5.isdigit())
print(str3.isspace())
print(str3.islower())
print(str3.title())
print(str3.lower())
print(str3.isupper())
print(str3.strip(" "))
print(str3.lstrip())
print(str3.rstrip())
print(str3.ljust(10,"_"))
print(str3.rjust(10,"_"))
print(str3.replace("s","i"))
print(str3.split(" "))
print(str3.swapcase())
print(str3.zfill(20))
"""
# set{}#

# set is mutalbe (changable)
# set is unordered
# setis index not support

"""
s9={12,34,554,56,67,10}#creating
print("creating string",s9)#print
print("creating string",type(s9))#print
"""
# print("indexing",s9[2])#indexing
# TypeError: 'set' object is not subscriptable
# print("slicing is",s9[2:])#slicing
# TypeError: 'set' object is not subscriptable
"""

"""
s19 = {1, 2, 3, 4, 5, 6}
# buil in methods
print(s19.add(5))
print(s19.remove(2))

                                 # Dictionary
# Dict is mutalbe (changable)
# set is unordered
# setis index not support

a={"keyword":"values"}#creating dict
print(a)

                        #Today practices
"""
#Function
#1 call by value
#2 call by refernce

#1 call by value
# function define
def add(a,b):
    print(a,b)
#function call
add(12,34) # call by value

#2 call by refernce
#function define
def add(x,y):
    print(x,y)
x=200
y=400
#function call
add(x,y)# call by reference



#local variable

def addition():
    tsr_list=[1,2,3,4,5,"hello",(10,20,30,40),{1,2,3,4,},{"key":"value"}]
    tsr_list2=[6,7,8,6]
    print("tsrlist is, tsrlist is",tsr_list+tsr_list2)
addition()

def string_fun_add():
    tsr_str="sasidhar"
    tsr_str1="kxn"
    print("string_fun and string_fun",tsr_str+tsr_str1)
string_fun_add()

def tuple_fun_add():
    tsr_tuple=(1,2,3,4,5)
    tsr_tuple1=(6,7,8,9)
    print("tupel_wtih function is",tsr_tuple+tsr_tuple1)
tuple_fun_add()

def set_fun_add():
    tsr_set={10,20,40,50,50}
    tsr_set1={20,30,40,50,67}
    print("set with function is",tsr_set+tsr_set1)
set_fun_add()

"""
                    #Global variable

"""
x=100
def add():
    # Local variables - Lifetime is within the function means outside
    #                   of the function it will not accessible
    x = 10
    y = 20
    print( x + y )
add()
print("x is ", x)

tsr_list = [200, 300, 400, 500]
def addition_list_fun():
    tsr_list = [1, 2, 3, 4, 5, "hello", (10, 20, 30, 40), {1, 2, 3, 4, }, {"key": "value"}]
    tsr_list2 = [6, 7, 8, 6]
    print("list_fun_addition_local", tsr_list + tsr_list2)
addition_list_fun()
print("list_fun_global",tsr_list)

tsr_str="Tirupati"
def string_fun_add():
    tsr_str = "sasidhar"
    tsr_str1 = "kxn"
    print("string_fun_local",tsr_str+tsr_str1)
string_fun_add()
print("string_fun_global",tsr_str)

tsr_tuple=(500,600,700,800,900)
def tuple_fun_add():
    tsr_tuple = (1, 2, 3, 4, 5)
    tsr_tuple1 = (6, 7, 8, 9)
    print("tupel_fun_Local",tsr_tuple+tsr_tuple1)
tuple_fun_add()
print("tuple_fun_global",tsr_tuple)
"""
"""
tsr_set = {1000, 2000, 40000, 50000, 60000}
def set_fun_add():
    tsr_set = {10, 20, 40, 50, 50}
    tsr_set1 = {20, 30, 40, 50, 67}
    print("set_fun_local",tsr_set+tsr_set1)
set_fun_add()
print("set_fun_local",tsr_set)
#TypeError: unsupported operand type(s) for +: 'set' and 'set'
"""

"""
tsr_list = [200, 300, 400, 500]
def addition_list_fun():
    tsr_list = [1, 2, 3, 4, 5, "hello", (10, 20, 30, 40), {1, 2, 3, 4, }, {"key": "value"}]
    tsr_list2 = [6, 7, 8, 6]
    print("list_fun_addition_local", tsr_list + tsr_list2)
addition_list_fun()
print("list_fun_global",tsr_list)

tsr_str="Tirupati"
def string_fun_add():
    tsr_str = "sasidhar"
    tsr_str1 = "kxn"
    print("string_fun_local",tsr_str+tsr_str1)
string_fun_add()
print("string_fun_global",tsr_str)

tsr_tuple=(500,600,700,800,900)
def tuple_fun_add():
    tsr_tuple = (1, 2, 3, 4, 5)
    tsr_tuple1 = (6, 7, 8, 9)
    print("tupel_fun_Local",tsr_tuple+tsr_tuple1)
tuple_fun_add()
print("tuple_fun_global",tsr_tuple)

"""

                                    # L E G B RULE
# ------>
"""
L - Local
E - Enclosing
G - Global
B - BuiltIn
"""

x = 1
def add():
    print("Local x is ", x)
    def sub():
        print("X is ", x)
    sub()
add()

tsr_list = [1, 2, 3, 4, 5, "hello", (10, 20, 30, 40), {1, 2, 3, 4, }, {"key": "value"}]
def addition_list_fun():
        print("list_fun_addition_local", tsr_list)
        def sub():
            print("List_sub is",tsr_list)
        sub()
addition_list_fun()

tsr_str="Tirupati"
def string_fun_add():
        print("string_fun_local",tsr_str)
        def sub_string():
            print("string_sub is",tsr_str)
        sub_string()
string_fun_add()

tsr_tuple=(500,600,700,800,900)
def tuple_fun_add():
    print("tupel_fun_Local",tsr_tuple)
    def sub_tuple():
        print("tuple_sub is",tsr_tuple)
    sub_tuple()
tuple_fun_add()

tsr_set={50,60,70,80,90}
def set_fun():
    print("set_fun_Local",tsr_set)
    def sub_set():
        print("set_sub is",tsr_set)
    sub_set()
set_fun()

tsr_dict={"keyvalue":18,"sasidhar":23,"chittoor":517004}
def dect_fun():
    print("dict_fun_local",tsr_dict)
    def sub_dect():
        print("dict_sub is",tsr_dict)
    sub_dect()
dect_fun()




                #local varibale -meaning life time is only in sub function
a=1
def add():
    print("local a is",a)
    def add_sub():
        a=500
        print("a is",a)
    add_sub()
add()

tsr_list = [1, 2, 3, 4, 5, "hello", (10, 20, 30, 40), {1, 2, 3, 4, }, {"key": "value"}]
def addition_list_fun():
        print("list_fun_addition_local", tsr_list)
        def sub():
            tsr_list=[2000,3000,4009,4005005,30030]
            print("List_sub is",tsr_list)
        sub()
addition_list_fun()

tsr_str="Tirupati"
def string_fun_add():
        print("string_fun_local",tsr_str)
        def sub_string():
            tsr_str="chittoor"
            print("string_sub is",tsr_str)
        sub_string()
string_fun_add()

tsr_tuple=(500,600,700,800,900)
def tuple_fun_add():
    print("tupel_fun_Local",tsr_tuple)
    def sub_tuple():
        tsr_tuple=(1,2,3,4)
        print("tuple_sub is",tsr_tuple)
    sub_tuple()
tuple_fun_add()

tsr_set={50,60,70,80,90}
def set_fun():
    print("set_fun_Local",tsr_set)
    def sub_set():
        tsr_set=(1,2,3,4)
        print("set_sub is",tsr_set)
    sub_set()
set_fun()

tsr_dict={"keyvalue":18,"sasidhar":23,"chittoor":517004}
def dect_fun():
    print("dict_fun_local",tsr_dict)
    def sub_dect():
        tsr_dict={"tirupati":23,"chittor":34}
        print("dict_sub is",tsr_dict)
    sub_dect()
dect_fun()


                        #only global variable

a=1
def add():
    a=400
    print("local a is",a)
    def sub():
        global a #use only global variable
        print("a is",a)
    sub()
add()

tsr_list = [1, 2, 3, 4, 5, "hello", (10, 20, 30, 40), {1, 2, 3, 4, }, {"key": "value"}]
def addition_list_fun():
        tsr_list = [2000, 3000, 4009, 4005005, 30030]
        print("list_fun_addition_local", tsr_list)
        def sub():
            global tsr_list#use only global varibale
            print("List_sub is",tsr_list)
        sub()
addition_list_fun()

tsr_str="Tirupati"
def string_fun_add():
        tsr_str="chittoor"
        print("string_fun_local",tsr_str)
        def sub_string():
            global tsr_str
            print("string_sub is",tsr_str)
        sub_string()
string_fun_add()

tsr_tuple=(500,600,700,800,900)
def tuple_fun_add():
    tsr_tuple=(1,23,45,454)
    print("tupel_fun_Local",tsr_tuple)
    def sub_tuple():
        global tsr_str
        print("tuple_sub is",tsr_tuple)
    sub_tuple()
tuple_fun_add()

tsr_set={50,60,70,80,90}
def set_fun():
    tsr_set={23,45,56,78}
    print("set_fun_Local",tsr_set)
    def sub_set():
        global tsr_set
        print("set_sub is",tsr_set)
    sub_set()
set_fun()

tsr_dict={"keyvalue":18,"sasidhar":23,"chittoor":517004}
def dect_fun():
    tsr_dict = {"tirupati": 23, "chittor": 34}
    print("dict_fun_local",tsr_dict)
    def sub_dect():
        global tsr_dict
        print("dict_sub is",tsr_dict)
    sub_dect()
dect_fun()

                            #Enclosing

a=1
def add():
    a=400
    print("local a is",a)
    def sub():
        print("a is",a)
    sub()
add()


tsr_list = [1, 2, 3, 4, 5, "hello", (10, 20, 30, 40), {1, 2, 3, 4, }, {"key": "value"}]
def addition_list_fun():
        tsr_list = [2000, 3000, 4009, 4005005, 30030]
        print("list_fun_addition_local", tsr_list)
        def sub():
            print("List_sub is",tsr_list)
        sub()
addition_list_fun()

tsr_str="Tirupati"
def string_fun_add():
        tsr_str="chittoor"
        print("string_fun_local",tsr_str)
        def sub_string():
           print("string_sub is",tsr_str)
        sub_string()
string_fun_add()

tsr_tuple=(500,600,700,800,900)
def tuple_fun_add():
    tsr_tuple=(1,23,45,454)
    print("tupel_fun_Local",tsr_tuple)
    def sub_tuple():
        print("tuple_sub is",tsr_tuple)
    sub_tuple()
tuple_fun_add()

tsr_set={50,60,70,80,90}
def set_fun():
    tsr_set={23,45,56,78}
    print("set_fun_Local",tsr_set)
    def sub_set():
        print("set_sub is",tsr_set)
    sub_set()
set_fun()

tsr_dict={"keyvalue":18,"sasidhar":23,"chittoor":517004}
def dect_fun():
    tsr_dict = {"tirupati": 23, "chittor": 34}
    print("dict_fun_local",tsr_dict)
    def sub_dect():
        print("dict_sub is",tsr_dict)
    sub_dect()
dect_fun()

#take a vaue from enclosing function as per LEGB rule

a=1
z=455
def add():
    a=400
    print("local a is",a)
    def sub():
        print("a is",a)#take a vaue from enclosing function as per LEGB rule
        def mul():
            print("z is",z)#take z from global as per LEGB rule
        mul()
    sub()
add()

a=1
def add():
    a=400
    print("local a is",a)
    def sub():
        print("a is",a)
    sub()
add()

tsr_str="Tirupati"
tsr_z="chittoor"
def string_fun_add():
        tsr_str="tpt"
        print("string_fun_local",tsr_str)
        def sub_string():
           print("t is",tsr_str)
           def mul_string():
                print("tsr_z",tsr_z)
           mul_string()
        sub_string()
string_fun_add()

a=1
z=20000
def add():
    a=200
    z=1000
    print("local ais",a)
    def sub():
        print("a is",a)
        def mul():
            print("z is",z)
            print("type of z",type(z))
        mul()
    sub()
add()

chittoor=111
tirupati=222
def sasidhar():
    chittoor=333
    print("sasidhar is",chittoor)#local variable ref;(LEGB)
    def kxn():
        print("kxn is",chittoor)#enclosing variable ref;(LEGB)
        def ysr():
            chittoor=2323
            print("ysr is ",chittoor)#local variable ref;(LEGB)
            def tsr():
                global chittoor
                print("tsr is",chittoor)#gloval variable ref;(LEGB)
                def str():
                    print("str is ",tirupati)#only global variable
                    print("type of str",type(tirupati))#define the builtin function
                str()
            tsr()
        ysr()
    kxn()
sasidhar()


def surname(name):
    return name+ " Tiruttani"
print(surname("sasidhr"))

def middlename(first_name, middle_name):
        return first_name+middle_name+" tiruttani"
print(middlename("sasi","dhar"))



                        #*agrument
def sum_sub(*a):
    return sum(a) #sum is a built function
print(sum_sub(23,34,45,56,66))

def max_sub(*b):
    return max(b)#max is a built function
print(max_sub(23,4,4,4,5454,6,4554,6,46,45,54))

def len_sub(*c):
    return len(c) #len is a built function
print(len_sub(232,4343,5353,654,5445.,64564,6454,6454,645,4))

def min_sub(*d):
    return min(d)
print(min_sub(100,2394,474,848,45))

                                #** keyword agruments
def sample (**sasidhar):
    print(sasidhar)
sample(t=100,s=500,r=233)

def kxn_sub(**kxn):
    return kxn
print(kxn_sub(kkk=78,sss=28,yyy=67))


                            #list practices

a=[12,34,45,67,"hello",(1,2,3,4),{"key":12,"hight":1},{1,2,3,45}]#creating list
print("type is",type(a))
print("index number is", a[4])#indexing(0,1,2,3,4)
a[5]="welcome to python"#reassing the value
print(a)
print(a[2:6])#slicing

t=[23,45,"python",45,56]
t1=[34,56,90,45,66]
#basic operation
print("addition is",t+t1)#concatenation
print("mulitification is",t1*4)
print("len of the t",len(t))
print("max of the t",max(t1))
print("min of the t",min(t1))
print("sum of the t",sum(t1))

#built-in methods
s=[23,43,45,65,66,78]
s1=[23,43,45,65,66,78]
s.append(10)# adds an element at the end of the list
print(s)
s.extend([345665,898,899,990])
print("add the more number",s)
s1.insert(3,34)#add an elements at the specified postiion
print(s1)
s1.remove(23)# remove the specified value
print(s1)
s1.pop(5)#pop remove the index value
print(s1)
s1.sort()#sort the list
print(s1)
s2=[23,43,45,65,66,78]
print(s2.count(45))
s2.reverse()
print(s2)



tt=(12,34,45,67,"hello",(1,2,3,4),{"key":12,"hight":1},{1,2,3,45})#creating tuple
print("creating tuple",tt)#print
print("indexing",tt[2])#indexing
print("slicing",tt[2:6])#slicing
"""
"""
ss1=(12,34,54)
ss11=(34,56,90,45,66)
#basic operass1ion
print("addiss1ion is",ss1+ss11)#concass1enass1ion
print("muliss1ificass1ion is",ss11*4)
print("len of ss11 is",len(ss11))
print("max of ss11 is",max(ss11))
print("min of ss11 is",min(ss11))
print("sum of ss11 is",sum(ss11))

"""

"""
s1="welcome to python programming"#creating tuple
print("creating string",s1)#print
print("creating string",type(s1))#print
print("indexing",s1[2])#indexing
print("slicing is",s1[2:])#slicing


str1="sasdihr"
str2="chittoor"
#basic operass1ion
print("addiss1ion is",str1+str2)#concass1enass1ion
print("muliss1ificass1ion is",str2*4)
print("len of str2 is",len(str2))
print("max of str2 is",max(str2))
print("min of str2 is",min(str2))
#print("sum of str2 is",sum(str2))
#TypeError: 'str' is an invalid keyword argument for print()

str3="sasidhar"
str4="alad123"
str5="1234543"
print(str3.capitalize())
print(str3.center(23,"*"))
print(str3.count("s"))
print(str3.endswith("har"))
print(str3.startswith("sasi"))
print(str3.find("a"))# find the index value
print(str3.index('a'))
print(str3.rfind("a"))
print(str4.isalpha())
print(str5.isdigit())
print(str3.isspace())
print(str3.islower())
print(str3.title())
print(str3.lower())
print(str3.isupper())
print(str3.strip(" "))
print(str3.lstrip())
print(str3.rstrip())
print(str3.ljust(10,"_"))
print(str3.rjust(10,"_"))
print(str3.replace("s","i"))
print(str3.split(" "))
print(str3.swapcase())
print(str3.zfill(20))

                    #set{}#


s9={12,34,554,56,67,10}#creating
print("creating string",s9)#print
print("creating string",type(s9))#print

#print("indexing",s9[2])#indexing
#TypeError: 'set' object is not subscriptable
#print("slicing is",s9[2:])#slicing
#TypeError: 'set' object is not subscriptable


""
                               # list methods
#append - add value to list at single index position
tsrlist = [10, 20 , 40]
tsrlist.append(50)
print(tsrlist)

tsrlist1=[50,60,70,80]
tsrlist1.append({23,45,343,454})
print(tsrlist1)

tsrlist2=[200,300,400,500]
tsrlist2.append("hello")
print(tsrlist2)

tsrlist3=[34,45,65,76,98]
tsrlist3.append((45,34,343,45,56))
print(tsrlist3)

tsrlist4=[54,454,565,76,6676,89]
tsrlist4.append({"key":20})
print(tsrlist4)

#add value to list at different index position
tsrlist6=[23,45,45,6]
tsrlist6.extend([60,70,80])
print(tsrlist6)
tsrlist7=[23,34,34]
tsrlist7.extend([23,34,34,"hello",{23,34,56},{"name":"sasi"}])
print(tsrlist7)

tsrlist8=[90,89,78]
tsrlist8.extend([23,34,545,65,45,34,])
print(tsrlist8)

tsrlist9=[34,35,56,50,90]
tsrlist9.extend([{23,34,34,34},{34,89,34,67},(2,34,343,45,56)])
print(tsrlist9)

tsrlist10=[23,45,23,56,90]
tsrlist10.extend([{23,34},{45,45},[23,45],[98,89],"sasdihar","hello",(23,45,34),(23,34,56),{"name":"sasidhar",}])
print(tsrlist10)

tsrlist11=[56,98,98,51]
tsrlist11.extend([{"name":"KXN","age":32,"place":"chittor"},{"name":"tsr","age":43,"place":"tpt"} ])
print(tsrlist11)



#print(myString.split())# Split at space

tsrstr1="welcome to python programming"
print(tsrstr1.split("o"))
tsrstr2="sasidhar"
print(tsrstr2.split("a"))

tsrstr3="tirupati"
print(tsrstr3.split("r"))
tsrstr4="chittoor"
print(tsrstr4.split("o"))


tsrstr6 = "ABC"
tsrs= "India".join(tsrstr6)
print(tsrs)

tsrstr7="welcome"
x="sasidhar".join(tsrstr7)
print(x)

tsrstr8="kxn"
t="welcome".join(tsrstr8)
print(t)
class car:
    name="BMW"
    price="2 cr"
    place="chittor"
    city="tirupati"
sasidhar=car()
print(sasidhar.name,sasidhar.price,sasidhar.place,sasidhar.city)


class man:
    name="sasidhar"
    male="male"
    hegith="5.7"
    city="chittor"
    place="tirupati"
sasi=man()
print(sasi.name,sasi.male,sasi.hegith,sasi.city,sasi.place)

class kxn:
    name_of_employee="tsr"
    male_of_employee="male"
    hegith_of_employee="5.7"
    city_of_employee="TPT"
    place_of_employee="tirupati"
    def run(self):
        print("employee is runining............")
    def walk(self):
        print("employee is walk......")
sasidhart=kxn()
print(sasidhart.name_of_employee,sasidhart.male_of_employee,sasidhart.hegith_of_employee,sasidhart.city_of_employee,sasidhart.place_of_employee)
sasidhart.run()
sasidhart.walk()


class stdmarkes:
    def __init__(self,n,h,w,t,e,m,m1,s,a):
        self.stdname=n
        self.stdheghit=h
        self.stdweight=w
        self.stdtelugu=t
        self.stdenglish=e
        self.stdm1=m
        self.stdm2=m1
        self.stds=s
        self.stdaa=a
    def run(self, x):
        print(x+" "+"employee is runining............")

    def walk(self):
        print("employee is walk......")

tsr=stdmarkes("gowthami",5.2,50,90,50,60,70,56,99)
print(tsr.stdname,tsr.stdheghit,tsr.stdweight,tsr.stdtelugu,tsr.stdenglish,tsr.stdm1,tsr.stdm2,tsr.stds,tsr.stdaa)
ysr=stdmarkes("sagar",4.4,50,35,60,56,45,39,99)
print("name:-,",ysr.stdname,"heghit:-,",ysr.stdheghit,"weight:,",ysr.stdweight,"telugu:",ysr.stdtelugu,"English",ysr.stdenglish,"m1",ysr.stdm1,"m2",ysr.stdm2,"s",ysr.stds,"aa",ysr.stdaa)

tsr.run("stdmarkes")


def addition()#fucntion


                            #function

def std(**markes):
    print(markes)
std(X=200,y=300,z=100)

def tdd(**markes):
    return (markes)
print(tdd(a=200,b=600,c=800))

def tsr(*mark):
    print(mark)
tsr(99,98,78,98,67,56,)

def tsr1(*number):
    return(number)
print(tsr1(23,34,45,56))

def tsr2(*mumber):
    return sum(mumber)
print(tsr2(303,405,50,6006,4004,5005,60,5005,5006,60))

def tsr3(*kxn):
    return len(kxn)
print(tsr3(20,304,4,45,5,65,6,78,89,78))

def tsr4(*ysr):
    return min(ysr)
print(tsr3(20,304,4,45,5,65,6,78,89,78))

def tsr5(*kcr):
    return max(kcr)
print(tsr5(20,304,4,45,5,65,6,78,89,78))

def sur_name(my_name):
    return my_name+ " reddy "
print(sur_name(" sasidhar"))

def mid_name(frist_name,middle_name):
    return frist_name +middle_name+ "reddy"
print(mid_name("sasi"," dhar"))

def full_name(f_name,m_name,last_name):
    return f_name + m_name + last_name + " I am  kxn emplyee "
print(full_name("sasi","dhar","t"))

def add(a=300,b=400,c=500):
    print(a,b,c)
add()
add(c=600)
add(a=1000)
add(b=200000)
add()

def ktr_m(t,s,r):
    print(t,s,r)
ktr_m(500,600,700)

s=10
z=900
def aaa ():
    s=400
    print("local variable is",s)
    def bbb():
        print("enclosing is s",s)#enclosing LEGB
        def ccc():
            print("global value",z)
            def ddd():
                print("enclosing",s)
                def fff():
                    global s
                    print("global is",s)
                    print("type is",type(s))
                fff()
            ddd()
        ccc()
    bbb()
aaa()


def addition (a,b):
    print("type of a",type(a))
    print("type of b",type(b))
    if type(a)==int and type(b)==int:
        print("a value +b value",a+b)
    else:
        if type(a)!=int:
            print("a value is invalid Please enter the integer type only",a)
        if type(b)!=int:
            print("b value is invalid please enter the integer type only",b)
addition(1034343,3009989)



# single
"""
class Parent_rrr:
    last_name = "Reddy"
class Grandpa(Parent_rrr):
    full_name = "sasidhar reddy"
c1 = Grandpa()
print(c1.last_name)
print(c1.full_name)

#mulit level
class Grand_parent_TTT:
    last_name_t = "nara TTT"
class Parent(Grand_parent_TTT):
    fist_name_t = "Raja"
class Child_NNN(Parent):
    middle_name = "tsr"
tsr = Child_NNN()
print(tsr.last_name_t)
print(tsr.fist_name_t)
print(tsr.middle_name)

#mulitpule
class Dad:
    dad_name="raja reddy"
class Mom:
    mom_name="bhanumathi"
class son(Dad,Mom):
    son_name="sasidhar reddy"
tsr1=son()
print(tsr1.dad_name)
print(tsr1.son_name)
print(tsr1.mom_name)

#hierarchial
class Sasidhar:
    address="pantrampalli"
class c1(Sasidhar):
    address1="chittor"
class c2(Sasidhar):
    address2="tirupati"
class c3(Sasidhar):
    address3="blr"
class c4(Sasidhar):
    address4="hyd"
class c5(Sasidhar):
    address5="ysr"
sss=c5()
print(sss.address)
print(sss.address5)
sss=c4()
print(sss.address4)


class A:
    first_name="Gowthami"
    age="24 years"
class B:
    last_name="Reddy"
class C(B,A):
    pass
class D(C):
    pass
c=C()
print(c.last_name)

class Parent:
    first_name="Gowthami"
    age="24 years"
class Parent2:
    Last_name="Reddy"
class child(Parent2,Parent):
    middle_name="sasidhar"
class A(child):
    First_name="Gowthami"
class B(A,child):
    last_name="Reddy"
class d(B,A):
    Middle_name="sasidhar"

obj=d
print(obj.last_name,obj.Last_name,obj.middle_name,obj.Middle_name,obj.Last_name,obj.first_name,obj.First_name)
"""

# sigle inheritance with function

class Dad:
    full_name="Raja reddy T"
    def draja(self):
        print("pranent class")
class Child(Dad):
    full_name_child="sasidhar T"
    def csasi(self):
        print("child class")
obj_s=Child()
print(obj_s.full_name_child)
print(obj_s.full_name)
print(obj_s.draja())
print(obj_s.csasi())

class Grand_Parent:
    def gpdisplay(self):
        print("GRAND PARENT METHOD")
class Parent (Grand_Parent):
    def pdisplay(self):
        print("PARENT METHOD")
class Child (Parent):
    def cdisplay(self):
        print("CHILD DISPLAY")
c=Child()
print(c.pdisplay())
print(c.gpdisplay())
print(c.cdisplay())


x=5000
z=100000
def addition():
    x=4000
    print("local x is print",x)
    def sub_add():
        print("enclosing is ",x)
        def mul():
            global x
            print("global varibale is",x)
            def add():
                print("enclsoing of global varibale ",x)
                def tsr():
                    print("z is global variable is",(z))
                    def ysr():
                        print("endlsong of z varilable",z)
                        def rrr():
                            print("endlosing variable is x",x)
                            print("type of Z is",type(z))
                            def sss():
                                x=2343
                                print("Local varialbe is ",x)
                                def ttt():
                                    print("endlosing varibale is sss",x)
                                ttt()
                            sss()
                        rrr()

                    ysr()
                tsr()
            add()
        mul()
    sub_add()
addition()



class Company:
    def __init__(self,name,employeeid,pf,salary):
        self.name=name
        self.employeeid=employeeid
        self.pf=pf
        self.salary=salary
    def Address(self,a):
        return a
sasidhar_e=Company("sasidhar",111,12345,20000)
print(sasidhar_e.Address("chittoor"))
print(sasidhar_e.name,sasidhar_e.employeeid,sasidhar_e.pf,sasidhar_e.salary)
tsr=Company("Gowthami",222,5432,90000)
print(tsr.Address("tirupati"))
print(tsr.name,tsr.employeeid,tsr.pf,tsr.salary)

ysr=Company((input("Enter the Employee Full name:-")),
             int(input("Enter the Employee_ID:-")),
             int(input("Enter the Employee_PF:-")),
             int(input("Enter the employee_Salary:-")))
print(ysr.name,ysr.employeeid,ysr.pf,ysr.salary)
print(ysr.Address(input("Enter the Full Address:-")))

"""


class Company:
    def __init__(self,name,employeeid,pf,salary):
        self.name=name
        self.employeeid=employeeid
        self.pf=pf
        self.salary=salary
    def Address(self,a):
        return a
sasidhar_e=Company("sasidhar",111,12345,20000)
print(sasidhar_e.Address("chittoor"))
print(sasidhar_e.name,sasidhar_e.employeeid,sasidhar_e.pf,sasidhar_e.salary)


class Company:
    def __init__(self,name,employeeid,pf,salary):
        self.name=name
        self.employeeid=employeeid
        self.pf=pf
        self.salary=salary
    def Address(self,a):
        return a
sasidhar_e=Company("sasidhar",111,12345,20000)
print(sasidhar_e.Address("chittoor"))
print(sasidhar_e.name,sasidhar_e.employeeid,sasidhar_e.pf,sasidhar_e.salary)
tsr=Company("Gowthami",222,5432,90000)
print(tsr.Address("tirupati"))
print(tsr.name,tsr.employeeid,tsr.pf,tsr.salary)
Nanda=Company("Nadhaar_kishore",999,23,343434)
print(Nanda.name,Nanda.employeeid,Nanda.pf,Nanda.salary)

class Company:
    def __init__(self,name,employeeid,pf,salary):
        self.name=name
        self.employeeid=employeeid
        self.pf=pf
        self.salary=salary
    def Address(self,b):
        return b
ysr=Company((input("Enter the Employee Full name:-")),
             int(input("Enter the Employee_ID:-")),
             int(input("Enter the Employee_PF:-")),
             int(input("Enter the employee_Salary:-")))
print(ysr.name,ysr.employeeid,ysr.pf,ysr.salary)
print(ysr.Address(input("Enter the Full Address:-")))


class student:
    def __init__(self,name,age,studentaddress,telugum,english):
        self.name=name
        self.age=age
        self.studentaddress=studentaddress
        self.telugum=telugum
        self.english=english
    def FullName(self):
        print("std full name is {}".format(self.name))
    def StdAge(self):
        print("std age is {}".format(self.age))
    def StdAddress(self):
        print("std Address is {}".format(self.studentaddress))
    def StdTelugum(self):
        print("std telugemake is {}".format(self.telugum))
    def StdEndlish(self):
        print("std english marks is {}".format(self.english))
sasidhar=student("sasi",50,"CTR",90,80)
sasidhar.FullName()
sasidhar.StdAge()
sasidhar.StdAddress()
sasidhar.StdTelugum()
sasidhar.StdEndlish()


def tsr():
    print(10+10)
sss=tsr
sss()

def shout (text):
    return text.upper()
print(shout("welcome"))
k=shout
print(k("sasidhar"))

def ggg(amount):
    return amount.upper()
print(ggg("chittoor"))
ww=ggg
print(ww("tirupati"))

def ttt(text1):
    return text1.lower()
print(ttt("SASIDHAR"))
RRR=ttt
print(RRR("GOWTHAMI"))



import time
start_time=time.time()
def fun_exec_time_cal(sagar):
  def wrapper():
    start_time=time.time()
    sagar()
    end_time=time.time()
    print(end_time-start_time)
  return wrapper
@fun_exec_time_cal
def fun1():
    a=10
    b=34
    print("a is {}".format(a+b))
fun1()


def gowthami(sasi):
    def tsr():
        sasi()
        print("a is value")
    return tsr
@gowthami
def sss():
    t=10
    s=20
    print("t+s and add value",t+s)
sss()



def kxn_company(sasi):
    def tsr():
        ysr=230
        sasi()
        kcr=500
        print("ysr +kcr is sum",ysr+kcr)
    return tsr
@kxn_company
def  sasidhar():
    a=120
    print("a values is ",a)
sasidhar()



def kxn_company(sasi):
    def tsr():
        sasi()
        ysr=230
        kcr=500
        print("ysr +kcr is sum",ysr+kcr)
    return tsr
@kxn_company
def  sasidhar():
    a=120
    print("a values is ",a)
sasidhar()



import time
def sasidhar(tsr):
    print("{} being executed")
    def ggg ():
        start_time=time.time()
        tsr()
        end_time=time.time()
        print("{}took secs".format(end_time-start_time))
    return ggg
@sasidhar
def sss():
    time.sleep(0.5)
    a=10
    time.sleep(0.5)
    print("a is {}".format(a))
sss()

"""
"""

def fun_call(gowthami):
    print("gowthami is good")
    def tsr():
        a=23
        b=343
        gowthami()
        print("a+b is value{}".format(a+b))
    return tsr
@fun_call
def ggg():
    c=360
    d=200
    print("c-b is value{}".format(c-d))
ggg()

"""


def KXN_company(sasidhar_reddy):
    print("beging value {}".format(sasidhar_reddy.__name__))
    def sasidhar_t():
        a=2849
        b=3849
        sasidhar_reddy()
        print("a+b is value{}".format(a+b))
    return sasidhar_t
@KXN_company
def KXN_employee():
    c=898979
    d=988
    print("c-d is value{}".format(c-d))
KXN_employee()

@KXN_company
def sasi():
    f=9878
    e=345
    print("f*e is value", f*e)
sasi()

"""
my_list=range(200)
odd_list=[]

for item in my_list:
    if item%2 !=0:
        odd_list.append(item)
print(odd_list)


oddnum=[item for item in range(200) if item %2 !=0]
print(oddnum)



MyTsr=[item for item in range(50) if item %2!=0]
print(MyTsr)

MyKGR=[item for item in range(100) if item %5==0]
print(MyKGR)

mygowthmi=[item for item in range(100) if item %5==0]
print(mygowthmi)

tsr = [ sasi for sasi in range(20) if sasi % 2 == 0]
print(tsr)

stsr = [ysr for ysr in range(100) if ysr % 2 == 0 if ysr % 5 == 0]
print(stsr)

gowthami = [kxn for kxn in range(10) if kxn < 5]
print(gowthami)



tsr1=["welcome","chittor","tirupati"]
tsr = [sss.upper() for sss in tsr1]
print(tsr)

city= ["blr", "hyd", "tpt", "ctr"]
gkr = ["welcome to python programming" for ttt in city]
print(gkr)

raj = ["Even" if i %2==0 else "Odd" for i in range(10)]
print(raj)

tsr1=['WELCOME', 'CHITTOR', 'TIRUPATI']
tsr = [sss.lower() for sss in tsr1]
print(tsr)

#Nested Loops in List Comprehension
# kxn= [[1, 2], [3,4], [5,6], [7,8]]
# ctr = [[kkk[i] for kkk in kxn] for i in range(2)]
# print (ctr)

intlist=[item for item in [1,2,"india",[45]] if type (item)==int]
print(intlist)

welcome=[102,39494,5050,606]
intlist=[item for item in welcome if type (item)==int]
print(intlist)

kxn= [[1, 2], [3,4], [5,6], [7,8]]
ctr = [[kkk[i] for kkk in kxn] for i in range(2)]
print (ctr)


mydict={1:{2:{3:100}}}
print("mydict [1] is",mydict[1])
print("mydict is", mydict[1][2])
print(mydict[1][2][3])

tsrdict={"tsr":{"ysr":{"kcr":{"ctr":{"ktr":{"rrr":100}}}}}}
print("tsr[tsr]is",tsrdict["tsr"])
print("ysr[ysr] is",tsrdict["tsr"]["ysr"])
print("kcr[kcr]is",tsrdict["tsr"]["ysr"]["kcr"])
print("kcr[ctr]is",tsrdict["tsr"]["ysr"]["kcr"]["ctr"])
print("kcr[ktr]is",tsrdict["tsr"]["ysr"]["kcr"]["ctr"]["ktr"])
print("kcr[rrr]is",tsrdict["tsr"]["ysr"]["kcr"]["ctr"]["ktr"]["rrr"])


myfamily = {"child1": { "name" : "Emil", "year" : 2004 },"child2": {"name" : "Tobias", "year" : 2007}, "child3" : {"name" : "Linus","year" : 2011}}

print(myfamily["child1"]["year"])
print(myfamily["child3"]["year"])
print(myfamily["child2"]["name"])


welcome=[s for s in [1,2,"india",[45]] if type (s)==str]
print(welcome)

rr=[s for s in [1,2,"india",[45],(1,2,3)] if type (s)==tuple]
print(rr)

tt=[s for s in [1,2,"india",[45],(1,2,3), 10.323] if type (s)==int]
print(tt)

ss=[s for s in [1,2,"india",[45],(1,2,3), 10.323] if type (s)==float]
print(ss)

oo=[s for s in [1,2,"india",[45],(1,2,3), 10.323,{1,283,8484}] if type (s)==set]
print(oo)

dcit=[s for s in [1,2,"india",[45],(1,2,3), 10.323,{1,283,8484},{"key":2453636}] if type (s)==dict]
print(dcit)

"""

Adim=["tpt","sss","ttd"]
ccc= [aaa if aaa != "ttd" else "ctr" for aaa in Adim]
print(ccc)

for item in range(50):
    if item %2==0:
        print(item,end=" ")

prime_numeber=[item for item in range(50) if item %2==0]
print(prime_numeber)

g=(int(input("Enter the g value:-")))
t=0
#loop variable
while t<=g:
    print(t,end="   ")
    t=t+1

class human:#class cretion
    color="white"
    height=5.1
    def run(self):
        print("runingg......")
    def walk(self):
        print("walking......")

#object_name=Class_name()
sasidhar_name=human()
print(sasidhar_name.color,sasidhar_name.height)
sasidhar_name.run()
sasidhar_name.walk()

class school:
    def __init__(self,n,a,t,e,m):
        self.std_n=n
        self.std_a=a
        self.std_t=t
        self.std_e=e
        self.std_m=m
    def full_name(self):
        print("std full name is {}".format(self.std_n))
    def Address(self):
        print("std address is {}".format(self.std_a))
    def telegu_marks(self):
        print("std telegu is {}".format(self.std_t))
    def English_marks(self):
        print("english_marks is {}".format(self.std_t))
    def Math_Marks(self):
        print("math marks is {}".format(self.std_m))
    def Pes_address(self,a):
        return ("pes address is {}".format(a))
pes=school("sasidhr",35,23,345,45)
pes.full_name()
pes.Address()
pes.English_marks()
pes.Math_Marks()
print(pes.Pes_address("ctr"))

sasidhar=school("gowthami",29,30,56,78)
print(sasidhar.std_n,sasidhar.std_a,sasidhar.std_t,sasidhar.std_e,sasidhar.std_m)



class Ap:
   full_name="dad , mom"
class bc(Ap):
    last_name="chlid"
ob_t=bc()
print(ob_t.full_name)

class dad:
    f_name="trr"
class mom(dad):
    M_name="ddd"
class child(mom):
    c_name="ttd"
class child1(child):
    ch1_name="ttt"
class child2(child1):
    ch2_name="ggg"
object=child2()
print(object.ch2_name)
print(object.ch1_name)
print(object.f_name)
print(object.M_name)
print(object.c_name)

class ddad:
    ff_name="trr"
class mmom(ddad):
    mm_name="ddd"
class cchild(mmom,ddad):
    cc_name="ttd"
ob1=cchild()
print(ob1.mm_name)
print(ob1.ff_name)
print(ob1.mm_name)

class parent:
    full_middle_last_name="sasidhar reddy t"
class child(parent):
    f_name="t"
class child1(parent):
    l_name="l"
class child2(parent):
    m_name="m"
class child3(parent):
    w_name="w"
class child4(parent):
    t_name="s"

tsr=child4()
print(tsr.t_name)
print(tsr.full_middle_last_name)
ysr=child2()
print(ysr.full_middle_last_name)
print(ysr.m_name)


class ddad:
    ff_name="trr"
class mmom(ddad):
    mm_name="ddd"
class cchild(mmom,ddad):
    cc_name="ttd"
class d1(cchild):
    tt_name="kkk"
class m1(d1):
    dd_name="mmm"
class cc1(m1,d1):
    cc_name="ccc"
ob1=cc1()
print(ob1.mm_name)
print(ob1.ff_name)
print(ob1.mm_name)
print(ob1.cc_name)
print(ob1.tt_name)
print(ob1.dd_name)

s=10
z=900
def aaa ():
    s=400
    print("local variable is",s)
    def bbb():
        print("enclosing is s",s)#enclosing LEGB
        def ccc():
            print("global value",z)
            def ddd():
                print("enclosing",s)
                def fff():
                    global s
                    print("global is",s)
                    print("type is",type(s))
                fff()
            ddd()
        ccc()
    bbb()
aaa()

a=int(input("enter a:"))
b=int(input("enter b:"))
c=int(input("enter c:"))
if a>b:
    if a>c:
        print("a is big")
    else:
        print("c is Big")
else:
    if b>c:
        print("b is big")
    else:
        print("c is big")

s="Welcome to python programming"
print(s.endswith("ing"))
print(s.startswith("wel"))

mystr="aaaaaaaaaaaaawelcomeaaaaaaaaaaaaaaaaaaaa"
print(mystr.strip())
print(mystr.strip("a"))
print(mystr.rstrip("a"))
print(mystr.lstrip("a"))
print(max(mystr))
print(min(mystr))
print(mystr.split(" "))
print(mystr.replace("a","z"))

# jsonstring to python -List
import json

# MyJsonList="[1,2,3,4,5,7,8,9]"
# print("myjsonlist type is {}".format(type(MyJsonList)))
# print("oth index value in  myjsonlist[0]is {}".format(MyJsonList[0]))
# mylist=json.loads(MyJsonList)
# print(mylist)
#
# #python to json -List
# myl=[768687,29888,3876786,4997,58908,7767878,8797,999999]
# print("myl type is {}".format(type(myl)))
# print("myl index value [0]is {}".format(myl[0]))
# myl2=json.dumps(myl)
# print("myl type of is {}".format(type(myl2)))
# print("index value in myl2[1] is {}".format(myl2[1]))


# #json to python - tuple
# MyJsontuple="(1,2,3,4,5,7,8,9)"
# print("myjsontuple type is {}".format(type(MyJsontuple)))
# print("oth index value in  myjsontuplet[2]is {}".format(MyJsontuple[0]))
# mytuple=json.loads(MyJsontuple)
# print(mytuple)

# #python to json -tuple
# myt2=(76,29,66,46,55,79,8,99)
# print("myt2 type is {}".format(type(myt2)))
# print("myt2 index value [3]is {}".format(myt2[3]))
# print(myt2)
# myt3=json.dumps(myt2)
# print(myt3)
# print("myt3 type of is {}".format(type(myt3)))
# print("index value in myt3[5] is {}".format(myt3[5]))

#json to python -str
# myjstr="India"
# print("type myjstr is {}".format(type(myjstr)))
# print("myjstr is index value is [o] {}".format(myjstr[0]))
# print("myjstr is index value is [1] {}".format(myjstr[1]))
# mystr1=json.loads(myjstr)
# print(mystr1)
# print("type of mystr1 is {}".format(type(mystr1)))

#python to json -str
# mystr1="sasidhar"
# print("type mystr1 is {}".format(type(mystr1)))
# print("indexing is [4]  {}".format((mystr1[4])))
# myjstr=json.dumps(mystr1)
# print(myjstr)
# print("type myjstr is {}".format(type(myjstr)))
# print("indexing is [2] {}".format((myjstr[2])))
# print(myjstr)

# myjsondict='{"name":"sasi","age":28}'
# print(" myjsondict type is {}".format(type(myjsondict)))
# mydict=json.loads(myjsondict)
# print("mydict is {}".format(mydict))
# myd=json.dumps(mydict)
# print(myd)
#
# mydict1=[{"name":"sasidhar","age":23},{"keyvalue":555}]
# print("type mydict1 is {}".format(type(mydict1)))
# mydict1[1].update({"c":123})
# print(mydict1)
# mydict1[1].update({"d":2323})
# print(mydict1)
#
# myt=[{"name": "sasidhar", "age": {"today":"welcome"}}, {"keyvalue": 555, "c": 123, "d": 2323},{"place":"chittor","city":"tirupati"}]
# myt[0]["welcome"]="chittor"
# print(myt)

#
# myt=[{"name": "sasidhar", "age": {"today":"welcome"}}, {"keyvalue": 555, "c": 123, "d": 2323},{"place":"chittor","city":"tirupati"}]
# myt[1].update({"kwe":"wdijhd"})
# print(myt)
#
# mydict={"name":{"please":{"welcome":{"gowthami":23}}}}
# print(mydict["name"])
# print(mydict["name"]["please"]["welcome"]["gowthami"])

# mydict={"sasidhar":{"gowthami":{"welcome":300}}}
# print(mydict["sasidhar"])
# print(mydict["sasidhar"]["gowthami"])
# print(mydict["sasidhar"]["gowthami"]["welcome"])

# mydict={"name":"sasidhr","age":28,"mark_telugu":33,"english_marks":43}
# print(type(mydict))
# mydict["marks_math"]=75
# print(mydict)


# mydict1=[{"name":"sasidhr","age":28,"mark_telugu":33,"english_marks":43},{"city":"chittoor","town":"blr"}]
# print("mydict type is {}".format(type(mydict1)))
# mydict1[0].update({"mark_math2":45})
# print(mydict1)
# mydict1[1].update({"englis_marks":99})
# print(mydict1)
# mydict1.append({"welcome":"CTR"})
# print(mydict1)
# mydict1.extend([{"marks":"welcome"}, {"welcoe":"tirupati"}])
# print(mydict1)

# mydict2='[{"name":"sasidhr","age":28,"mark_telugu":33,"english_marks":43},{"city":"chittoor","town":"blr"}]'
# print("mydict type is {}".format(type(mydict2)))
# #json to python
# mydictj=json.loads(mydict2)
# print(mydictj)
# #python to json
# print("mydict type is {}".format(type(mydict2)))
# mydicts=json.dumps(mydictj)
# print(mydicts)
#
# mydict={"sasidhar":{"gowthami":{"welcome":300}}}
# print(mydict["sasidhar"])
# print(mydict["sasidhar"]["gowthami"])
# print(mydict["sasidhar"]["gowthami"]["welcome"])



# mydict={1:{2:{3:100}}}
# print("mydict [1] is",mydict[1])
# print("mydict is", mydict[1][2])
# print(mydict[1][2][3])
#
# tsrdict={"tsr":{"ysr":{"kcr":{"ctr":{"ktr":{"rrr":100}}}}}}
# print("tsr[tsr]is",tsrdict["tsr"])
# print("ysr[ysr] is",tsrdict["tsr"]["ysr"])
# print("kcr[kcr]is",tsrdict["tsr"]["ysr"]["kcr"])
# print("kcr[ctr]is",tsrdict["tsr"]["ysr"]["kcr"]["ctr"])
# print("kcr[ktr]is",tsrdict["tsr"]["ysr"]["kcr"]["ctr"]["ktr"])
# print("kcr[rrr]is",tsrdict["tsr"]["ysr"]["kcr"]["ctr"]["ktr"]["rrr"])
                    #postpgresql pg admin




























from flask import Flask,request
app=Flask (__name__)
# @app.route('/')
# def fun1():
#     return "welcome to python programming framework flask"
# @app.route('/get-tsr-mobile-number')
# def fun2():
#     return "79535317234567"
#
# mylist_json='[1,2,3,4,5,6,7]'
# @app.route('/welcome to python sample code json')
# def fun3():
#     return mylist_json
# @app.route('/add')
# def fun4():
#     a=request.args.get('a')
#     b=request.args.get('b')
#     return str(int(a)+int(b))
# @app.route('/multiplication')
# def tsr():
#     c=request.args.get('c')
#     d=request.args.get('d')
#     return str(int(c)*int(d))
#
# @app.route('/sub')
# def sasi():
#     ysr=request.args.get('ysr')
#     kcr=request.args.get('kcr')
#     return str(int(ysr)-int(kcr))
# app.run()



# @app.route('/divi')
# def tsr1():
#     ttt=request.args.get('ttt')
#     sss=request.args.get('sss')
#     return str(int(ttt)/int(sss))
#
# @app.route('/power')
# def tsr3():
#     ttt=request.args.get('ttt')
#     return str(int(ttt**2))
#
# @app.route('/power1')
# def tsr4():
#     gowthami=request.args.get('gowthami')
#     sasi=request.args.get('sasi')
#     return str(int(gowthami)*int(sasi))

# mylist1=[1,2,3,4,5]
# mylist2=[6,7,8,9,10]
# @app.route('/sasidharadd')
# def sasidharaddition():
#     return mylist1 + mylist2
# sasidharaddition()
# app.run()


# mylist_json='[1,2,3,4,5,6,7]'
# @app.route('/welcome to python sample code json')
# def fun3():
#     return mylist_json
# app.run()

mylist1=[1,2,3,4,5]
mylist2=[6,7,8,9,10]
# @app.route('/sasidharadd')
# def sasidharaddition():
#     return str(mylist1 + mylist2)
#
#
# tsr=100
# ysr=398
# @app.route('/tsr_function')
# def tsrfun():
#     return str(tsr+ysr)
#
#
# y=34678
# t=23443
# @app.route('/tsr multiplication')
# def tsrmultiplication():
#     return str(y+t)
#
# @app.route('/tsr sub')
# def tsrsub():
#     return str(y-t)
# @app.route('/tsr divin')
# def tsrdivin():
#     return str(y/t)
# @app.route('/sasi')
# def tttsss():
#     return str((y**5) +(t**5))
# @app.route('/welcome')
# def sst():
#     return str(y**)
# app.run()
#

from flask import Flask
app=Flask(__name__)
@app.route('/what is python')
def sasidhar_function():
    return "Python is a computer programming language" \
           " often used to build websites and software, automate tasks, and conduct data analysis. " \
           "Python is a general-purpose language, " \
           "meaning it can be used to create a variety of different programs " \
           "and isn't specialized for any specific problems"

@app.route('/python language')
def python ():
    return "Python is an interpreted, interactive, object-oriented programming language. " \
           "It incorporates modules, exceptions, dynamic typing," \
           " very high level dynamic data types, and classes. " \
           "It supports multiple programming paradigms beyond object-oriented programming," \
           " such as procedural and functional programming"

app.run()