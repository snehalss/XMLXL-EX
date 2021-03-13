from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField
from wtforms.validators import DataRequired, InputRequired, Email, Length, EqualTo, ValidationError


class RegistrationForm(FlaskForm):
    first_name = StringField(validators=[InputRequired(), Length(min=1, max=40)])
    last_name = StringField(validators=[InputRequired(), Length(min=1, max=40)])
    email = StringField(validators=[InputRequired(),Email(), Length(max=60)])
    password = PasswordField(validators=[InputRequired(),Length(min=8)])
    confirm_password = PasswordField(validators=[InputRequired(), EqualTo('password')])
    company = StringField(validators=[Length(max=60)])
    subscription_plans = SelectField(choices=[
        ('', 'Select a plan...'),
        ('P0000', 'Register for Free - Get 10 Records'), 
        ('P0100', 'Plan 100'), 
        ('P0500', 'Plan 500'),
        ('P1000', 'Plan 1000'),
        ('P2000', 'Plan 2000'),
        ('P5000', 'Plan 5000')])
    submit = SubmitField('Register')
    
    def validate_subscription_plans(self, subscription_plans):
        if subscription_plans.data == '':
            print("Validation error: " + subscription_plans.data)
            raise ValidationError('Must select a plan')


