from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import *
from .models import User

class LoginForm(FlaskForm):
	email = StringField('Email', validators=[InputRequired(), Email(), Length(max=120)], render_kw={"class": "form-control"})
	password = PasswordField('Password', validators=[InputRequired(), Length(min=8, max=80)], render_kw={"class": "form-control"})
	remember_me = BooleanField('Remember Me', default=False, render_kw={"class": "form-check-input"})
	
	submitLogin = SubmitField('Login', render_kw={"class": "btn btn-primary"})

class RegistrationForm(FlaskForm):
	username = StringField('Username', validators=[InputRequired(), Length(min=4, max=64)], render_kw={"class": "form-control", "placeholder": "foodlover"})
	email = StringField('Email', validators=[InputRequired(), Email(), Length(max=120)], render_kw={"class": "form-control", "placeholder": "foodlover@email.com"})
	password = PasswordField('Password', validators=[InputRequired(), Length(min=8, max=80)], render_kw={"class": "form-control"})
	confirm_password = PasswordField('Confirm Password', validators=[InputRequired(), EqualTo('password')], render_kw={"class": "form-control"})
	
	submitRegistration = SubmitField('Sign Up', render_kw={"class": "btn btn-primary"})
	
	def validate_email(self, email):
		user = User.query.filter_by(email=email.data).first()
		if user:
			raise ValidationError('Email is already taken.')
		
class EventCreationForm(FlaskForm):
	title = StringField('Event Name', validators=[InputRequired(), Length(min=4, max=64)], render_kw={"class": "form-control"})
	description = TextAreaField('Event Description', validators=[InputRequired(), Length(min=50, max=500)], render_kw={"class": "form-control"})
	image = FileField('Event Image', validators=[DataRequired()], render_kw={"class": "form-control-file", "type": "file"})
	dateTime = DateTimeLocalField('Event Date & Start Time', format='%Y-%m-%dT%H:%M', validators=[InputRequired()], render_kw={"class": "form-control", "type": "datetime-local"})
	price = DecimalField('Event Price', validators=[InputRequired()], render_kw={"class": "form-control"})
	ticketsAvailable = IntegerField('Tickets Available', validators=[InputRequired()], render_kw={"class": "form-control"})
	locationName = StringField('Event Location', validators=[InputRequired(), Length(min=4, max=64)], render_kw={"class": "form-control"})
	category = SelectField('Select Category', validators=[InputRequired()], choices=[
		('Market', 'Market'),
		('Festival', 'Festival'),
		('Asian', 'Asian'),
		('Western', 'Western'),
		('Seafood', 'Seafood'),
		('Dessert', 'Dessert'),
		('Wine', 'Wine'),
		('Beer', 'Beer'),
		('Spirits', 'Spirits'),
		('Other', 'Other')
		])

	submit = SubmitField('Publish...', render_kw={"class": "btn btn-primary"})

class CommentForm(FlaskForm):
	content = TextAreaField('Add a comment...', [InputRequired()])

	submit = SubmitField('Post')

class BookingForm(FlaskForm):
	tickets = IntegerField('Enter no. of tickets...', [InputRequired()], render_kw={"min": "0", "step": "1"})

	submit = SubmitField('Buy Tickets')