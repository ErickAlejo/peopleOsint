from flask import Flask, request, render_template, jsonify
import sys
import os
path = os.path.abspath("./config")
sys.path.append(path)
import config.getjson as getj

app = Flask(__name__)

@app.route("/", methods=['GET'])
def home():
    return render_template('home.html')

@app.route("/person", methods=['GET','POST'])
def person():
    if request.method == 'GET':
        return render_template('person.html', data='Not Found')
    else:
        person = request.form.get("name")
        person = getj.getjson(person)
        return jsonify(person)
        #return render_template('person.html', data=person)

@app.errorhandler(500)
def internal_server_error(e):
    # note that we set the 500 status explicitly
    return render_template('500-error.html')


@app.errorhandler(404)
def internal_server_error(e):
    # note that we set the 500 status explicitly
    return render_template('404-error.html')