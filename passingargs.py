from flask import Flask

app = Flask(__name__)


@app.route('/hello/<name>')

def hello(name):
    return f"hello ! {name}"


@app.route('/numerical/<int:n>')
def number(n):
    return f"value you have entered : {n}"


@app.route('/float/<float:f>')
def floating(f):
    return f"you have entered float number is : {f}"

@app.route('/python/')  #canonical url
def hello_python():
   return 'Hello Python'


if __name__=='__main__':
    app.debug = True
    app.run()
