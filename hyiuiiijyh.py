from flask import Flask
app=Flask(__name__)
@app.route('/what is python')
def sasidhar_function():
    return "Python is a computer programming language often used to build websites and software, automate tasks, and conduct data analysis. " \
           "Python is a general-purpose language, " \
           "meaning it can be used to create a variety of different programs and isn't specialized for any specific problems"

@app.route('/python language')
def python ():
    return "Python is an interpreted, interactive, object-oriented programming language. " \
           "It incorporates modules, exceptions, dynamic typing, very high level dynamic data types, and classes. " \
           "It supports multiple programming paradigms beyond object-oriented programming, such as procedural and functional programming"

app.run()