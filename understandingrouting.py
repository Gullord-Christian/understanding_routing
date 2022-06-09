from flask import Flask

app = Flask(__name__)

@app.route("/hello")
def hello():
    return("Hello World!")

@app.route("/dojo")
def dojo():
    return("Dojo!")
    
@app.route("/greeting/<name>") # for a route '/hello/____' anything after '/hello/' gets passed as a variable 'name'
def greeting(name):
    print(name)
    return "Hi, " + (f"{name}")

@app.route("/repeat/35/hello")
def repeat():
        return ("Hello" * 35)

@app.route("/repeat/85/bye")
def bye():
        return ("bye" * 85)

@app.route("/repeat/99/dog")
def dog():
        return ("dog" * 99)

if __name__ == "__main__":
    app.run(debug = True)