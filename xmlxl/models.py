from datetime import datetime
from xmlxl import db, login_manager
from flask_login import UserMixin

# Because Flask-Login knows nothing about databases, 
# it needs the application's help in loading a user. 
# For that reason, the extension expects that the 
# application will configure a user loader function, 
# that can be called to load a user given the ID.
# The user loader is registered with Flask-Login with
# the "@login_manager.user_loader" decorator. 
# The id that Flask-Login passes to the function 
# as an argument is going to be a string, 
# so databases that use numeric IDs need to
# convert the string to integer.

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(60), index=True, unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    verified = db.Column(db.Boolean(), nullable=False, default=False)
    first_name = db.Column(db.String(40), nullable=False)
    last_name = db.Column(db.String(40), nullable=False)
    date_register = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    ip_register = db.Column(db.String(45), nullable=False)
    company = db.Column(db.String(60))
    balance_qty = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return (
            f"User('{self.email}', "
            f"'{self.first_name}', " 
            f"'{self.last_name}', "
            f"'{self.company}', " 
            f"'{self.balance_qty}')" 
        )

class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ref_transact = db.Column(db.String(40), nullable=False, default="TEST TRANSACTION")
    transaction_status = db.Column(db.String(40), nullable=False)
    date_transact = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    ip_transact = db.Column(db.String(45), nullable=False)
    purchase_qty = db.Column(db.Integer, nullable=False)
    amt = db.Column(db.Numeric(10,2), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return (
            f"Transaction('{self.ref_transact}', "
            f"'{self.date_transact}', " 
            f"'{self.purchase_qty}', "
            f"'{self.amt}')" 
        )

class ExcelFile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    upload_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    file_upload_name = db.Column(db.String(60), nullable=False)
    file_name = db.Column(db.String(30), unique=True, nullable=False)
    validation_status = db.Column(db.String(20), nullable=False)
    is_valid = db.Column(db.Boolean(), nullable=False)
    validation_report = db.Column(db.Text, nullable=False)
    processing_status = db.Column(db.String(20), nullable=False)
    is_processed = db.Column(db.Boolean(), nullable=False)
    no_of_records = db.Column(db.Integer(), nullable=False, default=0)

    def __repr__(self):
        return (
            f"File('{self.user_id}', "
            f"'{self.upload_date}', " 
            f"'{self.validation_status}', "
            f"'{self.processing_status}')" 
        )