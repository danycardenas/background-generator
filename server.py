from flask import Flask, render_template, url_for   # flask converts text like Hello Peeps into html for you
# render_template function allows to send the html file
app = Flask(__name__)     # app is an instance of Flask is the main file.

# app is the instance of this class. route() is a decorator to tell Flask what URL should trigger our function
@app.route('/')
def hello_world():
    # print('Hello World!')
    return render_template('index.html')     # need a folder named 'templates and put html file in there

@app.route('/favicon.ico')     # in html file, add another link to favicon.ico
def blog():
    return 'This is my blog'

@app.route('/about.html')
def about():
    return render_template('index.html')

@app.route('/careers')
def careers():
    return 'CAREERS Directory'

@app.route('/users/<username>/<int:post_id>')
def user(username=None, post_id=None):
    return render_template('index.html', name=username, post_id=post_id)

@app.route('/users/<username>/favicon2.ico')     # in html file, add another link to favicon.ico
def icon():
    return 'This is my blog'
# On terminal need to do the following
# set FLASK_APP=server.py   <---- server.py is python file
# set FLASK_DEBUG=1    <----- turns on debug mode to change it right away
# flask run  , on browser enter: http://127.0.0.1:5000/



