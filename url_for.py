from flask import Flask, redirect, url_for

app = Flask(__name__)
admin = 'nitin'

@app.route('/admin')
def admin():
    return "hello admin"

@app.route('/guest/<guest>')
def guest(guest):
    return f"hello {guest} you are our guest"

@app.route('/user/<name>')

def user(name):
    if name == 'admin':

        return redirect(url_for('admin'))
    else:
        return redirect(url_for('guest', guest=name))
    
# @app.route('/user/<name>')
# def hello_user(name):
#    if name =='admin':
#       return redirect(url_for('hello_admin'))
#    else:
#       return redirect(url_for('hello_guest',guest = name))

if __name__ == '__main__':
   app.run(debug = True)