                                   # practice all
"""
a=10
b=10
if a>b:
    print("a is big")
elif b>a:
    print("b is big")
else:
    print("both are equal")


t=12
s=12
if t>s:
    print("t is big")
elif s>t:
    print("s is big")
elif t==s:
    print("both are equal")
else:
    print("all false")

a=int(input("Enter the a value:"))
b=int(input("enter the b value:"))
c=int(input("Enter the c value:"))
if a>b:
    if a>c:
        print("a is big")
    else:
        Print("c is big")
else:
    if b>c:
        print("b is big")
    else:
        print("c is big")
    
    
"""
"""
a=int(input("Enter the a value:"))
b=int(input("enter the b value:"))
c=int(input("Enter the c value:"))
if a>b:
    if a>c:
        print("a is big")
    elif a==c:
        print("a and c both are equla")
    else:
        Print("c is big")
elif
    if b>c:
        print("b is big")
    else:
        print("c is big")
else:
    print("a,b,c all are equal")

"""
"""
tsrlist=range(20)
for item in tsrlist:
    if item %2==0:
        print(item)
"""
"""
tsrlist1=range(30)
for item in tsrlist1:
    if item %2==0 and item %1==0:
      print("Even number")
    else:
      print("odd number")
"""
"""
#function definitions:
def function_name(a,b):
    print(a,b)
function_name(10,30)
#function call
"""


"""
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

print(sasidhar)

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
s19={1,2,3,4,5,6}
#buil in methods
s19.add(10)
print(s19)
s19.remove(2)
print(s19)
s