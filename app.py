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
    a = Maxwell(time, deformation)
    return jsonify({
        'Hello': 'World!',
    })


# Run App on default port (5000)
app.run()
