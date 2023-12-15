from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)


@app.route('/hello/<user>')
def hello(user):
    return render_template('hello.html', name = user)

@app.route('/result/<int:score>')


def result(score):
    if score > 50:
        return render_template('pass.html', marks = score)
    else:
        return render_template('fail.html', marks = score)
    
if __name__=='__main__':
    app.run(debug=True)