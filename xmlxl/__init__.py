# The __init__.py file is considered a package.
# It can be imported by other Python programs (or modules).
# When a program imports the package, the "__init__.py" file is executed first.
# When executed, it defines the symbols that the package exposes to the outside world.

from flask import Flask
from xmlxl.config import Config   # Importing Config class from config.py
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


# This creates an application object that is an instance of the class Flask
# The "__name__" variable passed to Flask class is a Python predefiend variable. 
# The value of "__name__" is set to the name of the module (i.e. a Python program) in which it is used.
app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Importhing the "routes" module 
# The "routes" module is imported after declaring the 'app' variable above.
# This is peculiar because it is a workaround to avoid circular imports.
# Circular imports are a common problem in Flask applications.
# The "routes" module needs the "app" variable defined above.
# And the "xmlxl" moodule needs to import the "routes" module. 
# So putting one of the reciprocal imports at the bottom avoids the circular reference error.
# Such error results from mutual references between these two files.
from xmlxl import routes, models
