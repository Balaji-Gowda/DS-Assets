from flask import Flask, redirect, request, url_for, render_template

spam = Flask(__name__)


@spam.route('/', methods=['POST'])
def index():
    if request.method == 'post':
        text = request.form['text']


if __name__ == "__main__":
    spam.run(debug=True)
