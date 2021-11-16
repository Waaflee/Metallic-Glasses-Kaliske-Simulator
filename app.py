#!/usr/bin/env python
# encoding: utf-8

from flask import Flask, jsonify, request
from flask_cors import CORS

from models.maxwell.Maxwell import Maxwell

app: Flask = Flask(__name__)
# Enable CORS so we can use the API
CORS(app)


@app.route('/', methods=['GET'])
def get_root():
    time = request.args["time"]
    deformation = request.args["deformation"]
    model = request.args["model"]
    try:
        M: Maxwell = Maxwell(time, deformation, model)
        s, d, t = M.run()
    except ValueError as e:
        return e.__str__(), 400
    return jsonify({
        'sigma': s.tolist(),
        'deformation': d.tolist(),
        'time': t.tolist(),
    })


# Run App on default port (5000)
app.run()
