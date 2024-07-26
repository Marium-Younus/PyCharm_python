#----------------------------- Flask Dynamic Routes
from flask import Flask
app = Flask(__name__)
@app.route('/')
def Page1():
    return '<h1>Introduction Page1</h1>'

@app.route('/about')
def Page2():
    return '<h1>About Page2</h1>'

@app.route('/country/<name>')
def Page3(name):
    return '<h1>country is {} </h1>'.format(name)

if __name__ == '__main__':
    app.run()
