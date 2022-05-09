from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo,Email, DataRequired, ValidationError
from market.models import User

class RegisterForm(FlaskForm):
    def validate_username(self, username_to_check):
        user = User.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError('Username already Exists!, Please try a different username')
    def validate_email_address(self,email_address_to_check):
        email_address = User.query.filter_by(email_address=email_address_to_check.data).first()
        if email_address:
            raise ValidationError("Email address already exists!, Please try a different email address.")


    username = StringField('User Name:', validators=[Length(min=2, max=30),DataRequired()])
    email_address = StringField('Email Address:',validators=[Email(),DataRequired()])
    password1 = PasswordField('Password:', validators=[Length(min=6),DataRequired()])
    password2 = PasswordField('Confirm Password:', validators=[EqualTo('password1'),DataRequired()])
    submit = SubmitField('Create Account')

