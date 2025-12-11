from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, SubmitField
from wtforms.validators import InputRequired, Length

class SignupForm(FlaskForm):
    username = StringField("Username", validators=[InputRequired(), Length(min=3)])
    password = PasswordField("Password", validators=[InputRequired(), Length(min=6)])
    submit = SubmitField("Sign Up")

class LoginForm(FlaskForm):
    username = StringField("Username", validators=[InputRequired(), Length(min=3)])
    password = PasswordField("Password", validators=[InputRequired(), Length(min=6)])
    submit = SubmitField("Log In")

class AdminSignupForm(FlaskForm):
    username = StringField("Username", validators=[InputRequired(), Length(min=5)])
    password = PasswordField("Password", validators=[InputRequired(), Length(min=8)])
    submit = SubmitField("Create Admin")

class AdminLoginForm(FlaskForm):
    username = StringField("Username", validators=[InputRequired(), Length(min=5)])
    password = PasswordField("Password", validators=[InputRequired(), Length(min=8)])
    submit = SubmitField("Admin Login")

class HomeContentForm(FlaskForm):
    general_objective = TextAreaField('General Objective', validators=[InputRequired()])
    background_info = TextAreaField('Background Information', validators=[InputRequired()])
    submit = SubmitField('Update Content')

class FeedbackForm(FlaskForm):
    name = StringField("Name (optional)")
    message = TextAreaField("Message", validators=[InputRequired(), Length(min=3)])
    submit = SubmitField("Send Feedback")
