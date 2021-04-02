from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField, IntegerField
from wtforms.validators import DataRequired, InputRequired, Email, Length, EqualTo, ValidationError, NumberRange
from xmlxl.models import User
from flask_wtf.file import FileField, FileAllowed

class RegistrationForm(FlaskForm):
    first_name = StringField(validators=[InputRequired(), Length(min=1, max=40)])
    last_name = StringField(validators=[InputRequired(), Length(min=1, max=40)])
    email = StringField(validators=[InputRequired(),Email(), Length(max=60)])
    password = PasswordField(validators=[InputRequired(),Length(min=6)])
    confirm_password = PasswordField(validators=[InputRequired(), EqualTo('password')])
    company = StringField(validators=[Length(max=60)])
    order_qty = IntegerField('No. of Records', default=10, validators=[
        InputRequired(),
        NumberRange(min=10, max=10000, message="You can buy any quantity between 10 and 10,000.")
        ])
    amt = IntegerField()

    i_agree = BooleanField()
    submit = SubmitField('Register')

    # def validate_subscription_plans(self, subscription_plans):
    #     if subscription_plans.data == '':
    #         print("Validation error: " + subscription_plans.data)
    #         raise ValidationError('Must select a plan')


    def validate_i_agree(self, i_agree):
        if i_agree.data == False:
            print(i_agree.data)
            raise ValidationError('You must agree to the terms and conditions and our privacy policy before registering.')

class LoginForm(FlaskForm):
    email = StringField(validators=[InputRequired(),Email()])
    password = PasswordField(validators=[InputRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Log In')

class UploadForm(FlaskForm):
    xl_file = FileField('Upload Excel File', validators=[FileAllowed(['xls', 'xlsx', 'xlsm'])])
    submit = SubmitField('Upload')