#------------------------------Flask Basic Routes
from flask import Flask
app = Flask(__name__)

@app.route('/')
def Page1():
    return '<h1>Introduction Page1</h1>'
@app.route('/about')
def Page2():
    return '<h1>About Page2</h1>'
if __name__ == '__main__':
    app.run()

