"""
Flask app
"""
import os, redis, datetime
from flask import (Flask, g, request, session, redirect,
                   url_for, render_template, jsonify)
from flask_script import Manager
from sentiment_icebreaker.twitter_ import config as config_file

app = Flask(__name__)
app.config.from_object(config_file)

def get_redis():
    if not hasattr(g, 'redis'):
        g.redis = redis.StrictRedis(**app.config['REDIS'])
    return g.redis


@app.route('/')
def home():
    '''
    index.html
    '''
    args = request.args.copy()
    #redis_client = get_redis()

    return render_template("index.html")


@app.route('/messages')
def tracked_users():
    '''
    return messages
    '''
    messages = ["dummy one", "dummy two"]
    return jsonify(messages)


manager = Manager(app)

if __name__ == "__main__":
    manager.run()
