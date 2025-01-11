from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField, SubmitField, SelectField
from wtforms.validators import DataRequired, EqualTo

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

class AddPatientForm(FlaskForm):
    name = StringField('Patient Name', validators=[DataRequired()])
    gender = SelectField('Gender', choices=[('male', 'Male'),('female', 'Female')], validators=[DataRequired()])
    blood_type = SelectField('Blood Type', choices=[
        ('a-positive', 'A+'),
        ('a-negative', 'A-'),
        ('b-positive', 'B+'),
        ('b-negative', 'B-'),
        ('ab-positive', 'AB+'),
        ('ab-negative', 'AB-'),
        ('o-positive', 'O+'),
        ('o-negative', 'O-')
    ], validators=[DataRequired()])
    submit = SubmitField('Add Patient')


class DeletePatientForm(FlaskForm):
    id = IntegerField('Patient ID to Remove', validators=[DataRequired()])
    submit = SubmitField('Delete Patient')

class AddMedicalRecordForm(FlaskForm):
    details = StringField('Record Details', validators=[DataRequired()])
    submit = SubmitField('Add Record')
