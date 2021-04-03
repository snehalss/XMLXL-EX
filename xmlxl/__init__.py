# The __init__.py file is considered a package.
# It can be imported by other Python programs (or modules).
# When a program imports the package, the "__init__.py" file is executed first.
# When executed, it defines the symbols that the package exposes to the outside world.

from flask import Flask
from xmlxl.config import Config   # Importing Config class from config.py
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from celery import Celery


# This creates an application object that is an instance of the class Flask
# The "__name__" variable passed to Flask class is a Python predefiend variable. 
# The value of "__name__" is set to the name of the module (i.e. a Python program) in which it is used.
app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

# Celery 
celery = Celery(app.name, backend=app.config['CELERY_RESULT_BACKEND'], broker=app.config['CELERY_BROKER_URL'])
# celery.conf.update(app.config)

PRICE_TABLE = [
    [10,10,25,250, "First 10 at Rs. 25 each (10 x 25 = Rs. 250)"],
    [10,100,20,2050, "Next 90 at Rs. 20 each (90 x 20 = Rs. 1,800)"],
    [100,250,16,4450, "Next 150 at Rs. 16 each (150 x 16 = Rs. 2,400)"],
    [250,500,12,7450, "Next 250 at Rs. 12 each (250 x 12 = Rs. 3,000)"],
    [500,1000,9,11950, "Next 500 at Rs. 9 each (500 x 9 = Rs. 4,500)"],
    [1000,2000,7,18950 ,"Next 1000 at Rs. 7 each (1000 x 7 = Rs. 7,000)"],
    [2000,5000,5,33950, "Next 3000 at Rs. 5 each (3000 x 5 = Rs. 15,00)"],
    [5000,10000,4,53950, "Next 5000 at Rs. 4 each (5000 x 4 = Rs. 20,000)"],
]

# Importhing the "routes" module 
# The "routes" module is imported after declaring the 'app' variable above.
# This is peculiar because it is a workaround to avoid circular imports.
# Circular imports are a common problem in Flask applications.
# The "routes" module needs the "app" variable defined above.
# And the "xmlxl" moodule needs to import the "routes" module. 
# So putting one of the reciprocal imports at the bottom avoids the circular reference error.
# Such error results from mutual references between these two files.
from xmlxl import routes, models
