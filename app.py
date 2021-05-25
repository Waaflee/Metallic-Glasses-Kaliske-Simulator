#!/usr/bin/env python
# encoding: utf-8

from flask import Flask, jsonify
from flask_cors import CORS

app: Flask = Flask(__name__)
# Enable CORS so we can use the API
CORS(app)


@app.route('/', methods=['GET'])
def get_root():
    return jsonify({
        'Hello': 'World!',
    })


# Run App on default port (5000)
app.run()
