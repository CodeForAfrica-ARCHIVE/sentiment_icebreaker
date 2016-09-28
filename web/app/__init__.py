"""
Flask app
"""
import os, datetime
from flask import (Flask, g, request, session, redirect,
                   url_for, render_template, jsonify)
from flask_script import Manager
from sentiment_icebreaker.twitter_ import config as config_file

app = Flask(__name__)
app.config.from_object(config_file)


@app.route('/')
def home():
    '''
    index.html
    '''
    args = request.args.copy()
    return render_template("index.html")


@app.route('/messages')
def tracked_users():
    '''
    return messages
    '''
    #messages = ["dummy one", "dummy two"]
    with open(app.config["MESSAGESTORE"], "r") as archivefile:
        msgs = archivefile.read()
    return jsonify(msgs)


manager = Manager(app)

if __name__ == "__main__":
    manager.run()
