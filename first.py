from flask import Flask

app = Flask(__name__)

@app.route('/')

def hello():
    return "hello this is the first flask app"

@app.route('/greet')
def greet():
    return 'welcome to the greet url'



def hosting():
   return "hello this is your host! how can i help you"
app.add_url_rule('/', 'hostilng', hosting )


def gfg():
   return 'geeksforgeeks'
app.add_url_rule('/', 'g2g', gfg)


if __name__ == "__main__":
    # app.debug = True
    # app.run()
    app.run(debug=True)