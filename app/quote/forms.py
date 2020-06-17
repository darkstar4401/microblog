from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField,  SelectField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from flask_babel import _, lazy_gettext as _l
from app.models import User, Lead
from wtforms.fields.html5 import DateField
\
class LandingForm(FlaskForm):
    zipcode = StringField(_l('Zip Code:'), validators=[DataRequired()]) #validators=[]
    insStatus = SelectField(_l('Currently insured?'), choices=[('yes',"Yes, I'm looking for savings."),('no',"No, I need coverage.")])
    submit = SubmitField(_l('Get Quote'))
class PersonalInfoForm(FlaskForm):
    zipcode = StringField(_l('Zip Code:'), validators=[DataRequired()])
    fname = StringField(_l('First Name:'), validators=[DataRequired()])
    lname = StringField(_l('Last Name:'), validators=[DataRequired()])
    insStatus = SelectField(_l('Currently insured?'), choices=[('yes',"Yes, I'm looking for savings."),('no',"No, I need coverage.")])
    email = StringField(_l('Email:'), validators=[DataRequired()])
    zipcode = StringField(_l('Zip Code:'), validators=[DataRequired()])
    gender = SelectField(_l('Gender'),choices=[("Male",'Male'),("Female",'Female')])
    birthDate = StringField(_l('Birthdate:'),default="mmddyyyy", validators=[DataRequired()])
    martial = SelectField(_l('Marital Status'), choices=[('single',"Single"),('married',"Married")])
    military = SelectField(_l('Military Status'), choices=[('yes',"Active duty/Veteran"),('no',"No Military history")])
    homeOwner = SelectField(_l('Home Owner Status'), choices=[('rent',"Renting"),('owned',"Home Owned"),('mortgage',"Home financed")])
    education = SelectField(_l('Education'), choices=[('Phd',"Phd.",),('Ma',"Masters"),('Ba',"Bachelors"),('College',"Some College"),('Hs',"Diploma/GED")])
    occupation = SelectField(_l('Occupation'), choices=[('tech',"Tech./IT"),('health',"Heathcare"),('finance',"Finance"),("Manufacturing",'Manufacturing'),("Construction",'Construction'),('trade',"Skilled Trade")])
    credit = SelectField(_l('Credit Score'), choices=[('none',"No credit history."),('Fair',"Fair 580-669"),('Good',"Good 670-739"),("Very Good",'Very Good 740-799'),("Exceptional",'Exceptional 800-850')])
    accidents = SelectField(_l('Accidents in past 3 years:'), choices=[('0',"0"),('1',"1"),('2',"2"),('3',"3"),('4',"4+")])
    duis = SelectField(_l('DUIs in past 3 years:'), choices=[('0',"0"),('1',"1"),('2',"2"),('3',"3"),('4',"4+")])
    suspensions = SelectField(_l('Suspensions in past 3 years:'), choices=[('0',"0"),('1',"1"),('2',"2"),('3',"3"),('4',"4+")])
    parentId = StringField(_l('Accidents in past 3 years:'), validators=[DataRequired()])
    phone = StringField(_l('Phone:'), validators=[DataRequired()])
    phoneVerified = StringField(_l('Is phone verified:'), validators=[DataRequired()])
    submit = SubmitField(_l('Submit'))
class VehicleInfoForm(FlaskForm):
    make = SelectField(_l('Make:'), choices=[('tech',"Tech./IT"),('health',"Heathcare"),('finance',"Finance"),("Manufacturing",'Manufacturing'),("Construction",'Construction'),('trade',"Skilled Trade")])
    model = SelectField(_l('Model:'), choices=[('tech',"Tech./IT"),('health',"Heathcare"),('finance',"Finance"),("Manufacturing",'Manufacturing'),("Construction",'Construction'),('trade',"Skilled Trade")])
    trim = SelectField(_l('Trim:'), choices=[('sedan4d',"4 Door Sedan"),('coupe',"2 Door Coupe"),('convert',"Convertable")])
    year = SelectField(_l('Year'), choices=[(str(year),str(year)) for year in range(1980,2021)])
    submit = SubmitField(_l('Submit'))

class HomeInfoForm(FlaskForm):
    pass


class LoginForm(FlaskForm):
    username = StringField(_l('Username'), validators=[DataRequired()])
    password = PasswordField(_l('Password'), validators=[DataRequired()])
    remember_me = BooleanField(_l('Remember Me'))
    submit = SubmitField(_l('Sign In'))


class RegistrationForm(FlaskForm):
    username = StringField(_l('Username'), validators=[DataRequired()])
    email = StringField(_l('Email'), validators=[DataRequired(), Email()])
    password = PasswordField(_l('Password'), validators=[DataRequired()])
    password2 = PasswordField(
        _l('Repeat Password'), validators=[DataRequired(),
                                           EqualTo('password')])
    submit = SubmitField(_l('Register'))

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError(_('Please use a different username.'))

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError(_('Please use a different email address.'))


class ResetPasswordRequestForm(FlaskForm):
    email = StringField(_l('Email'), validators=[DataRequired(), Email()])
    submit = SubmitField(_l('Request Password Reset'))


class ResetPasswordForm(FlaskForm):
    password = PasswordField(_l('Password'), validators=[DataRequired()])
    password2 = PasswordField(
        _l('Repeat Password'), validators=[DataRequired(),
                                           EqualTo('password')])
    submit = SubmitField(_l('Request Password Reset'))

class TestForm(FlaskForm):
    email = StringField(_l('Email'), validators=[DataRequired(), Email()])
    submit = SubmitField(_l('test submit'))

