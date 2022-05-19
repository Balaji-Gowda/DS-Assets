# building urls dynamically
# variables rules

from flask import Flask, redirect, url_for
urls = Flask(__name__)


@urls.route('/')
def index():
    return "<html><div style='text-align:center;color:blue'><h1>Welcome To Flask FrameWork</h1></div></html>"


@urls.route('/<int:intval>')
def value(intval):
    return "value is "+str(intval)


@urls.route('/pass/<score>')
def passs(score):
    return "student passed with score"+score


@urls.route('/fail/<score>')
def fail(score):
    return "student failed with score"+score


@urls.route('/results/<int:score>')
def results(score):
    if score < 35:
        res = "fail"
    else:
        res = "passs"
    return redirect(url_for(res, score=score))


if __name__ == '__main__':
    urls.run(debug=True)
