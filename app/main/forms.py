from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, PasswordField
from wtforms.validators import DataRequired, EqualTo, Email, ValidationError

from app.models import User


class SignupForm(FlaskForm):
    username = StringField('User Name', validators=[DataRequired()])
    email = StringField('Email address', validators=[DataRequired(), Email(message='Valid email address required')])
    submit = SubmitField('Sign Up')

    def validate_email(self, email):
        email = User.query.filter_by(email=email.data).first()
        if email is not None:
            raise ValidationError(
                'An account is already registered for that email. Please use a different email.')