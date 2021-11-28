from flask import Flask


app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/hi')
def hello():
    return 'Hi , World'


if __name__=='__main__':
    app.run()