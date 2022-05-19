# integrate HTML with flask
# HTTP verb GEt ND pOST
# if elif else injinja2
# tables ,borders

# main.py,index.html,results.html

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


# tables
@urls.route('/pass/<score>')
def passs(score):
    status = "pass"
    dct = {"name": "BAlaji", "Age": 23, "Location": "Kuppam"}
    return render_template('results.html', score=int(score), status=status, dct=dct)


@urls.route('/fail/<score>')
def fail(score):
    status = "fail"
    return render_template('results.html', score=int(score), status=status)


@urls.route('/results/<int:score>')
def results(score):
    if score < 35:
        res = "fail"
    else:
        res = "passs"
    return redirect(url_for(res, score=score))


# HTTP verb GEt ND pOST
# result checker html page
@urls.route('/st', methods=['POST', 'GET'])
def gfg():
    scre = 0
    if request.method == "POST":
        python = float(request.form['python'])
        ml = float(request.form['ML'])
        nlp = float(request.form['NLP'])
        # ml = float(request.form['ML'])
        scre = int((python+ml+nlp)/3)

    return redirect(url_for("results", score=scre))


if __name__ == '__main__':
    urls.run(debug=True)
