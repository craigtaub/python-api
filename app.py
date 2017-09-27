# pylint: disable=C0111

from flask import Flask, render_template
from mapped import process

APP = Flask(__name__)

@APP.route("/")
def hello():
    return "Hello World!"

@APP.route("/route1")
def route1():
    return render_template('hello.html', name="Craig")

@APP.route('/post/<int:post_id>')
def show_post(post_id): # integer
    mapped_it = process(post_id)
    return 'Post %d' % mapped_it
