# from flask import Flask, redirect, url_for

# app = Flask(__name__)
# admin = 'abc'

# @app.route('/admin')

# def admin():
#     # adm = 'abc'
#     return f"hello {admin}"

# @app.route('/guest/<guest>')
# def guest(guest):
#     return f"hello {guest} you are our guest"

# @app.route('/user/<name>')

# def user(name):
#     if name == 'abc':

#         return redirect(url_for('admin'))
#     else:
#         return redirect(url_for('guest', guest=name))
    
# # @app.route('/user/<name>')
# # def hello_user(name):
# #    if name =='admin':
# #       return redirect(url_for('admin'))
# #    else:
# #       return redirect(url_for('guest',guest = name))

# if __name__ == '__main__':
#    app.run(debug = True)




from flask import Flask, redirect, url_for

app = Flask(__name__)
admin_username = 'abc'

@app.route('/admin')
def admin():
    return f"hello {admin_username}"

@app.route('/guest/<guest>')
def guest(guest):
    return f"hello {guest} you are our guest"

@app.route('/user/<name>')
def user(name):
    if name == 'abc':
        return redirect(url_for('admin'))
    else:
        return redirect(url_for('guest', guest=name))

if __name__ == '__main__':
    app.run(debug=True)
