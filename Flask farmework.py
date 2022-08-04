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

