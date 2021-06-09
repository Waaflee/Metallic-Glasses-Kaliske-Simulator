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
    # print(request)
    time = request.args["time"]
    deformation = request.args["deformation"]
    print(time)
    print(deformation)
    M = Maxwell(time, deformation)
    # return jsonify({'hello': 'world!'})
    s, d, t = M.run()
    return jsonify({
        'sigma': s.tolist(),
        'deformation': d.tolist(),
        'time': t.tolist(),
    })


# Run App on default port (5000)
app.run()
