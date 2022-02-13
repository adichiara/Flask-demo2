from flask import Flask

app = Flask(__name__)

@app.route("/")
# @app.route("/hello/")
# @app.route("/hello/<name>")
def hello(name=''):

    return "Hello there: " + name

# @app.route("/goodbye/<name>")
# def goodbye(name=''):

#     return "see ya: " + name


if __name__ == '__main__':
  
    # run() method of Flask class runs the application 
    # on the local development server.
    app.run()