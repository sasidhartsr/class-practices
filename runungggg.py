                       #today practices
"""
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


"""
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

tsrstr9="ysr"
s=" welcome to python programming ".join(tsrstr9)
print(s)
tsrtsr10="ttd"
td="  tirumala tirupati devasthanma  ".join(tsrtsr10)
print(td)

tsrs1="CHITTOOR"
print(tsrs1.lower())

tsrs2=" WLCOME TO PYTHON PROGRAMMING"
print(tsrs2.lower())

tsrs3="sasidhar"
print(tsrs3.lower())

tsrs44="sasdhart"
print(tsrs44.upper())

tsr55=" s.r.puram "
print(tsr55.upper())

tsr66="welcome to python programming"
print(tsr66.upper())



tss="welcome to python"
print(tss.endswith("hon"))
print(tss.endswith("ton"))
print(ts)


