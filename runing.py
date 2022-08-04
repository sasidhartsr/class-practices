
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

