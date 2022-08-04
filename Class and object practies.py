                        #class and object function
"""
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

                               # Constructor


class human:#class cretion
    def __init__(self):
        print("constructor")
#object_name=Class_name()
sasidhar_name=human()

class human:
    def __init__(self,c,h):
        self.color=c
        self.height=h
    def run(slef):
        print("running....")
    def walk(self):
        print("walking")
sasidhar=human("white",5.11)
print(sasidhar.color,sasidhar.height)


class employee:
    employee_name="raju"
    def fetch_employee_details(self):
        return {"name":"raju","age":78}
raju_obj=employee()
print(employee)
print(raju_obj)
print(raju_obj.employee_name)
print(raju_obj.fetch_employee_details())

class student:
    name ="sasidhar"
    age=23
    gendr="male"
    telugu=89
    english=90
    def student_address(self):
        return "pantrampali,chittoor"
sasidhar=student()
print(sasidhar.name,sasidhar.age,sasidhar.gendr,sasidhar.telugu,sasidhar.english)
print(sasidhar.student_address())
"""

class student:
    name ="sasidhar"
    age=23
    gendr="male"
    telugu=89
    english=90
    def student_address(self):
        return "1-1200/1,Pantrampali,Chittoor, Pin:517 125"
sasidhar=student()
print("student name:-",sasidhar.name,"student age:-",sasidhar.age,"student gendr:-",sasidhar.gendr,"student telugu:-",sasidhar.telugu,"student english:-", sasidhar.english)
print(sasidhar.student_address())
tsr=student()
print("student name:-",tsr.name,"student age:-",tsr.age,"student gendr:-",tsr.gendr,"student telugu:-",tsr.telugu,"student english:-", tsr.english)
print(tsr.student_address())
ysr=student()
print("student name:-",ysr.name,"student age:-",ysr.age,"student gendr:-",ysr.gendr,"student telugu:-",ysr.telugu,"student english:-", ysr.english)
print(ysr.student_address())
