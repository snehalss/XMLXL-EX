from datetime import datetime
from xmlxl import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(60), index=True, unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    verified = db.Column(db.Boolean(), nullable=False)
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

