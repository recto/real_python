"""
Task Form module
"""
from flask_wtf import FlaskForm, Form
from wtforms import StringField, DateField, IntegerField, \
        SelectField, PasswordField
from wtforms.validators import DataRequired, Length, EqualTo

class AddTaskForm(FlaskForm):
    """
    Add task form.
    """
    task_id = IntegerField()
    name = StringField('Task Name', validators=[DataRequired()])
    due_date = DateField(
        'Date Due (mm/dd/yyyy)',
        validators=[DataRequired()], format='%m/%d/%Y'
    )
    priority = SelectField(
        'Priority',
        validators=[DataRequired()],
        choices=[
            ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'),
            ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'),
            ('9', '9'), ('10', '10')
        ]
    )
    status = IntegerField('Status')

class RegisterForm(Form):
    """
    Registration Form
    """
    name = StringField(
        'Username',
        validators=[DataRequired(), Length(min=6, max=25)]
    )
    email = StringField(
        'Email',
        validators=[DataRequired(), Length(min=6, max=40)]
    )
    password = PasswordField(
        'Password',
        validators=[DataRequired(), Length(min=6, max=40)]
    )
    confirm = PasswordField(
        'Repeat Password',
        validators=[DataRequired(),
                    EqualTo('password', message='Passwords must match')]
    )

class LoginForm(Form):
    """
    Login Form
    """
    name = StringField(
        'Username',
        validators=[DataRequired(), Length(min=6, max=25)]
    )
    password = PasswordField(
        'Password',
        validators=[DataRequired()]
    )
