from flask import Flask

app = Flask(__name__)

# @app.route('/')

def gfg():
   return 'geeksforgeeks'
app.add_url_rule('/', 'g2g', gfg)


if __name__ == "__main__":
    # app.debug = True
    # app.run()
    app.run(debug=True)