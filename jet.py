#!/bin/python
# import flask server dependecies & ML models
from flask import Flask, render_template, jsonify, url_for 
from script import imagenet, depthnet, detectnet, segnet, posenet, stopMLs

app = Flask(__name__)

# access the webpage via server
@app.route('/')
def index():
    return render_template('index.html')

#1 access the ML imagenet script
@app.route('/execute-imagenet')
def execute_script():
    try:
        imagenet()
        return jsonify({"success": True})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)})

#2 access the ML detectnet script 
@app.route('/execute-detect')
def execute_detect():
    try:
        detectnet()
        return jsonify({"success": True})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)})

#3 access the ML segnet script 
@app.route('/execute-segnet')
def execute_segnet():
    try:
        segnet()
        return jsonify({"success": True})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)})

#3 access the ML posenet script 
@app.route('/execute-posenet')
def execute_posenet():
    try:
        posenet()
        return jsonify({"success": True})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)})

#7 access the ML depthnet script
@app.route('/execute-depth')
def execute_depth():
    try:
        depthnet()
        return jsonify({"success": True})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)})

#1 access the ML imagenet script
@app.route('/execute-stopmls')
def execute_stopmls():
    try:
        stopMLs()
        return jsonify({"success": True})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)})

# set the ip + port for access
app.run(host="192.168.0.235", port=8555)

if __name__ == '__main__':
    app.run(debug=False)

