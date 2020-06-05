from flask import Blueprint

bp = Blueprint('quote', __name__)

#from app.qoute import routes
from flask import render_template, redirect, url_for, flash, request
from werkzeug.urls import url_parse
from flask_login import login_user, logout_user, current_user
from flask_babel import _
from app import db
from app.quote import bp
from app.quote.forms import LandingForm, PersonalInfoForm
from app.models import User,Lead
from app.quote.email import send_password_reset_email
#twilio call import


@bp.route('/get-quote', methods=['GET', 'POST'])
def getQuote():
    if current_user.is_authenticated:
        #TODO: redirect to profile
        return redirect(url_for('main.index'))
    #else get user zipcode and insurance status stpre in session
    landingform = LandingForm()
    personalInfoForm=PersonalInfoForm()
    if landingform.zipcode.data is not None:
        print(landingform.zipcode.data)
        personalInfoForm.zipcode.data = landingform.zipcode.data

    if request.method == 'POST':
        #return render_template('quote/my-data.html',PersonalInfoForm=personalInfoForm)
        #write zip and status tp session

        lead = Lead(
        	fname=personalInfoForm.fname.data,
			lname=personalInfoForm.lname.data,
			email=personalInfoForm.email.data,
			zipcode=personalInfoForm.zipcode.data,
			insured=personalInfoForm.insStatus.data,
			gender=personalInfoForm.gender.data,
			birthDate=personalInfoForm.birthDate.data,
			martial=personalInfoForm.martial.data,
			military=personalInfoForm.military.data,
			homeOwner=personalInfoForm.homeOwner.data,
			education=personalInfoForm.education.data,
			occupation=personalInfoForm.occupation.data,
			credit=personalInfoForm.credit.data,
			accidents=personalInfoForm.accidents.data,
			suspensions=personalInfoForm.suspensions.data,
			phone=personalInfoForm.phone.data,
			phoneVerified="False",
			parentId="None"
			)
        #add email to session and store lead in database
        db.session.add(lead)
        db.session.commit()
        flash(_('Congratulations, you are on your way to savings!'))

        lead = Lead.query.filter_by(email=personalInfoForm.email.data).first()
        #return redirect(url_for('quote.my-data'),PersonalInfoForm=personalInfoForm, lead=lead)
        return render_template('quote/my-data.html', title=_('My Data'), lead=lead, PersonalInfoForm=personalInfoForm)

    if not personalInfoForm.validate_on_submit() and request.method == 'POST':
        print("post")
        lead_data = {
        	"fname":personalInfoForm.fname.data,
			"lname":personalInfoForm.lname.data,
			"email":personalInfoForm.email.data,
			"zipcode":personalInfoForm.zipcode.data,
			"insured":personalInfoForm.insStatus.data,
			"gender":personalInfoForm.gender.data,
			"birthDate":personalInfoForm.birthDate.data,
			"martial":personalInfoForm.martial.data,
			"military":personalInfoForm.military.data,
			"homeOwner":personalInfoForm.homeOwner.data,
			"education":personalInfoForm.education.data,
			"occupation":personalInfoForm.occupation.data,
			"credit":personalInfoForm.credit.data,
			"accidents":personalInfoForm.accidents.data,
			"suspensions":personalInfoForm.suspensions.data,
			"phone":personalInfoForm.phone.data,
			"phoneVerified":"False",
			"parentId":"None"}
        lead_errors = {
        	"fname":personalInfoForm.fname.errors,
			"lname":personalInfoForm.lname.errors,
			"email":personalInfoForm.email.errors,
			"zipcode":personalInfoForm.zipcode.errors,
			"insured":personalInfoForm.insStatus.errors,
			"gender":personalInfoForm.gender.errors,
			"birthDate":personalInfoForm.birthDate.errors,
			"martial":personalInfoForm.martial.errors,
			"military":personalInfoForm.military.errors,
			"homeOwner":personalInfoForm.homeOwner.errors,
			"education":personalInfoForm.education.errors,
			"occupation":personalInfoForm.occupation.errors,
			"credit":personalInfoForm.credit.errors,
			"accidents":personalInfoForm.accidents.errors,
			"suspensions":personalInfoForm.suspensions.errors,
			"phone":personalInfoForm.phone.errors
			}
        print(lead_data)
        print(lead_errors)
        #return render_template('quote/my-data.html', title=_('My Data'), PersonalInfoForm=personalInfoForm)
    return render_template('quote/landing.html', title=_('Get Quote'), form=landingform, PersonalInfoForm=personalInfoForm)

@bp.route('/my-data', methods=['GET', 'POST'])
def success():
    if current_user.is_authenticated:
        #TODO: redirect to profile
        return redirect(url_for('main.index'))
    lead = Lead.query.filter_by(email="datatradr96@gmail.com").first()#form.email.data
    print(lead.email)
    if lead.email is not None:
    	print(lead)
    	return render_template('quote/my-data.html',lead=lead, title=_('My Data'), PersonalInfoForm=lead)


    personalInfoForm=PersonalInfoForm()
    landingform = LandingForm()
    return render_template('quote/landing.html', title=_('Get Quote'), form=landingform, PersonalInfoForm=personalInfoForm)

