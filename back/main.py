from flask import Flask, request, abort
from flask_cors import CORS
import algorithms.python as pal

app = Flask(__name__)
CORS(app)

@app.route("/")
def hello_world():
    return "<h1> Division Site 😎 </h1>"

@app.route("/python")
def python_divide():
    raw_num = request.args.get('num')
    raw_den = request.args.get('den')
    if (raw_num == None or raw_den == None):
        abort(400)

    num = 0
    den = 0
    try:
        num = int(raw_num)
        den = int(raw_den)
    except ValueError:
        abort(400)
    except:
        abort(500)
    
    res = pal.divide(num,den)
    return list(res)


@app.route("/python/withdecimals", methods=["GET"])
def python_divide_with_decimals():
    raw_num = request.args.get('num')
    raw_den = request.args.get('den')
    raw_steps = request.args.get('steps')
    if (raw_num == None or raw_den == None or raw_steps == None):
        abort(400)
    
    num = 0
    den = 0
    steps = 0
    try:
        num = int(raw_num)
        den = int(raw_den)
        steps = int(raw_steps)
    except ValueError:
        abort(400)
    except:
        abort(500)

    res = pal.divide_with_decimals(num, den, steps)

    return res