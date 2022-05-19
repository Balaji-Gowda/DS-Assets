from flask import Flask
# WSGI app
app = Flask(__name__)

# decorator


@app.route('/')
def welcome():
    return "Hello Flask FrameWork!!!!!  inside home page..........."


@app.route('/hello')
def welcome2():
    return "Hello Flask FrameWork!!!!!  inside /hello path.........."


if __name__ == '__main__':
    app.run(debug=True)
