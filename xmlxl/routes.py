# The routes are the different URLs that the application implements. 
# In Flask, handlers for the application routes are written as Python functions, called view functions. 
# View functions are mapped to one or more route URLs.
# This basically tells Flask what logic to execute when a client requests a given URL.

from xmlxl import app
from flask import request, render_template, redirect, flash
from xmlxl.forms import RegistrationForm

# The term "app.route" is a decorator
# The function 'index()' is called a 'view function' in MVC terminology.
@app.route('/')
@app.route('/index')
def index():
    # Creating a mock dictionary object for testing
    user = {'username': 'snehal'}
    # File index.html created in the 'templates' directory in main app folder i.e. "xmlxl"
    # In below statement the terms 'title' and 'user' are names of variables used in the template.
    return render_template('index.html', title='Home', user=user)
    

# Example of a route with dynamic component
@app.route('/user/<name>')
def user(name):
    return "<h1>Hello, {}!</h1>".format(name)

# Request-Response Cycle in Flask:
#
# When Flask receives a request from a client, 
# it needs to make a few objects available to 
# the view function that will handle it.
#
# To avoid cluttering view functions 
# with lots of arguments that may not always be needed, 
# Flask uses "contexts" to temporarily make
# certain objects globally accessible.

# Example
# Requires "from flask import request"
# 
# In 'my_browser' function given below,
# the 'request' object is used as if 
# it were a global object, but it is not.
# 
# In reality, request cannot be a global variable. 
# In a multithreaded server several threads can be working
# on different requests from different clients all at the same time, 
# so each thread needs to see a different object in request. 
# 
# Contexts enable Flask to make certain variables 
# globally accessible to a thread without 
# interfering with the other threads.

@app.route('/my-browser')
def my_browser():
    user_agent = request.headers.get('User-Agent')
    return '<p>Your browser is {}</p>'.format(user_agent)


# The 'register()' view function: 
#   1. Loads the 'RegistrationForm()' from forms.py (see import directive at top of this file)
#   2. Uses name.html template to render the form on given route (i.e. URI)
@app.route('/register/', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    
    if form.validate_on_submit():
        flash(f'This is flash testing', 'info')
        return redirect('/')
    else: 
        flash(f'This is flash error', 'danger')
    return render_template('registration.html', title="Registration", form=form)

