from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/beans")
def beans():
    return "<h1>B E A N S</h1>"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=9000, debug=False)
