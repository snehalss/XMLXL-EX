from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField, IntegerField
from wtforms.validators import DataRequired, InputRequired, Email, Length, EqualTo, ValidationError, NumberRange


class RegistrationForm(FlaskForm):
    first_name = StringField(validators=[InputRequired(), Length(min=1, max=40)])
    last_name = StringField(validators=[InputRequired(), Length(min=1, max=40)])
    email = StringField(validators=[InputRequired(),Email(), Length(max=60)])
    password = PasswordField(validators=[InputRequired(),Length(min=8)])
    confirm_password = PasswordField(validators=[InputRequired(), EqualTo('password')])
    company = StringField(validators=[Length(max=60)])
    order_qty = IntegerField('No. of Records', validators=[
        InputRequired(),
        NumberRange(min=10, max=10000, message="You can buy any quantity between 10 and 10,000")
        ])
    amt = IntegerField()

    # subscription_plans = SelectField(choices=[
    #     ('', 'Select a plan...'),
    #     ('P0000', 'Register for Free - Get 10 Records'), 
    #     ('P0100', 'Plan 100'), 
    #     ('P0500', 'Plan 500'),
    #     ('P1000', 'Plan 1000'),
    #     ('P2000', 'Plan 2000'),
    #     ('P5000', 'Plan 5000')])

    i_agree = BooleanField('I agree to the')
    submit = SubmitField('Register')

    # xmlxl_ns.price_info = 
    # [[0,10,0],[10,100,20],[100,250,16],[250,500,12],[500,1000,9],[1000,2000,7],[2000,5000,5],[5000,10000,4]];
    # Price
    price_table_dict = [
        {'from': 0, 'to': 10, 'rate': 0},
        {'from': 10, 'to': 100, 'rate': 20},
        {'from': 100, 'to': 250, 'rate': 16},
        {'from': 250, 'to': 500, 'rate': 12},
        {'from': 500, 'to': 1000, 'rate': 9},
        {'from': 1000, 'to': 2000, 'rate': 7},
        {'from': 2000, 'to': 5000, 'rate': 5},
        {'from': 5000, 'to': 10000, 'rate': 4},
    ]



    # def validate_subscription_plans(self, subscription_plans):
    #     if subscription_plans.data == '':
    #         print("Validation error: " + subscription_plans.data)
    #         raise ValidationError('Must select a plan')


