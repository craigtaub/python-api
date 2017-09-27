# pylint: disable=C0111

from flask import Flask, render_template
APP = Flask(__name__)

@APP.route("/")
def hello():
    return "Hello World!"

@APP.route("/route1")
def route1():
    return render_template('hello.html', name="Craig")

@APP.route('/post/<int:post_id>')
def show_post(post_id): # integer
    return 'Post %d' % post_id
