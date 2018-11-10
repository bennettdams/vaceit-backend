
import os
from flask import Flask, url_for, json, jsonify
app = Flask(__name__)


@app.route('/')
def hello():
    return "VACEIT BACKEND | https://github.com/bennettdams/vaceit"

@app.route('/bans')
def showjson():
    json_url = os.path.join(app.root_path, "static", "bans.json")
    data = json.load(open(json_url))
    return jsonify(data)

@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)

if __name__ == '__main__':
    app.run()

