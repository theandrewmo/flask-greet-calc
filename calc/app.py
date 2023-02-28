# Put your app in here.

from flask import Flask, request
import operations 


app = Flask(__name__)

@app.route('/add')
def add():
    a = request.args.get('a', type=int)
    b = request.args.get('b', type=int)
    return f"<p>{operations.add(a,b)}</p>"

@app.route('/sub')
def sub():
    a = request.args.get('a', type=int)
    b = request.args.get('b', type=int)
    return f"<p>{operations.sub(a,b)}</p>"

@app.route('/mult')
def mult():
    a = request.args.get('a', type=int)
    b = request.args.get('b', type=int)
    return f"<p>{operations.mult(a,b)}</p>"

@app.route('/div')
def div():
    a = request.args.get('a', type=int)
    b = request.args.get('b', type=int)
    return f"<p>{operations.div(a,b)}</p>"

funcs = {
    'add': operations.add,
    'sub': operations.sub,
    'mult': operations.mult,
    'div': operations.div
}

@app.route('/math/<op>')
def all(op):
    a = request.args.get('a', type=int)
    b = request.args.get('b', type=int)
    return f"{funcs[op](a,b)}"
