# pylint: disable=C0111

from flask import Flask, render_template, jsonify
from mapped import process
import logging

APP = Flask(__name__)


# Hello
@APP.route("/")
def hello():
    return "Hello World!"


# Basic template + variable
@APP.route("/route1")
def route1():
    return render_template('hello.html', name="Craig")


# Process url param and return
@APP.route('/post/<int:post_id>') # integer
def show_post(post_id):
    mapped_it = process(post_id)
    return 'Post %d' % mapped_it

# Process url param, log, JSON return it
@APP.route('/api/<int:post_id>')
def api(post_id):
    
    mapped_it = process(post_id)
    logging.warning('Log to terminal post_id %d', post_id) # log it

    return jsonify(
        id=mapped_it,
        key="value"
    )