# integrate HTML with flask
# HTTP verb GEt ND pOST

from types import MethodType
from flask import Flask, redirect, request, url_for, render_template
# from flask import render_template, request;
urls = Flask(__name__)

# integrate HTML with flask


@urls.route('/')
def index():
    return render_template('index.html')


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


# HTTP verb GEt ND pOST
# result checker html page
@urls.route('/submit', methods=['POST', 'GET'])
def gfg():
    python = 0
    if request.method == "POST":
        python = request.form['python']
        # html = float(request.form['HTML'])
        # sql = float(request.form['SQL'])
        # ml = float(request.form['ML'])
        # scre = ((python+html+sql+ml)/4)

    return render_template("index.html", res=python)


if __name__ == '__main__':
    urls.run(debug=True)
