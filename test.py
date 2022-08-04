
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


