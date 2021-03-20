from xmlxl import app, db
from xmlxl.models import User, Transaction


# The app.shell_context_processor decorator 
# registers the function as a shell context function. 
# When the flask shell command runs, it will
# invoke this function and register the 
# items returned by it in the shell session.
# The reason the function returns a dictionary
# and not a list is that for each item you have to
# also provide a name under which it will be referenced
# in the shell, which is given by the dictionary keys.
# After you add the shell context processor function 
# you can work with database entities without 
# having to import them.
@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Transaction': Transaction}