from flask import Blueprint

bp = Blueprint('quote', __name__)

#from app.qoute import routes
from flask import render_template, redirect, url_for, flash, request
from werkzeug.urls import url_parse
from flask_login import login_user, logout_user, current_user
from flask_babel import _
from app import db
from app.quote import bp
from app.quote.forms import LandingForm, PersonalInfoForm,VehicleInfoForm
from app.models import User,Lead
from app.quote.email import send_password_reset_email
#twilio call import

@bp.route('/get-quote', methods=['GET', 'POST'])
def getQuote():
    landingform = LandingForm()
    personalInfoForm=PersonalInfoForm()
    vehicleInfoForm = VehicleInfoForm()
    if current_user.is_authenticated:
        print(current_user.email)
        lead = Lead.query.filter_by(email=current_user.email).first()
        #return redirect(url_for('quote.my-data'),PersonalInfoForm=personalInfoForm, lead=lead)
        return render_template('quote/my-data.html', title=_('My Data'), lead=lead, PersonalInfoForm=personalInfoForm)
        return redirect(url_for('quote.my-data', title=_('My Data'),PersonalInfoForm=personalInfoForm, lead=lead))
        #return render_template('quote/my-data.html', title=_('My Data'), lead=lead, PersonalInfoForm=personalInfoForm)

    if request.method == 'POST':
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
        print(lead_errors)
        #add email to session and store lead in database
        db.session.add(lead)
        db.session.commit()
        #flash(_('Congratulations, you are on your way to savings!'))

        lead = Lead.query.filter_by(email=personalInfoForm.email.data).first()
        #return redirect(url_for('quote.myData', title=_('My Data'),PersonalInfoForm=personalInfoForm, lead=lead))
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
    return render_template('quote/landing.html', title=_('Get Quote'), form=landingform, PersonalInfoForm=personalInfoForm, VehicleInfoForm=vehicleInfoForm)

@bp.route('/my-data', methods=['GET', 'POST'])
def success():
    #landingform = LandingForm()
    personalInfoForm=PersonalInfoForm()
    if current_user.is_authenticated:
        print(current_user.email)
        lead = Lead.query.filter_by(email=current_user.email).first()
        #return redirect(url_for('quote.my-data'),PersonalInfoForm=personalInfoForm, lead=lead)
        return render_template('quote/my-data.html', title=_('My Data'), lead=lead, PersonalInfoForm=personalInfoForm)
    else:
    	pass
    	return render_template()# get user to make account to manage data/ads

    personalInfoForm=PersonalInfoForm()
    landingform = LandingForm()
    return render_template('quote/landing.html', title=_('Get Quote'), form=landingform, PersonalInfoForm=personalInfoForm)

@bp.route('/personal-info-form', methods=['GET', 'POST'])
def testForm():
    personalInfoForm=PersonalInfoForm()
    if request.method == 'POST':
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
        print(lead_errors)
        #add email to session and store lead in database
        db.session.add(lead)
        db.session.commit()
        #flash(_('Congratulations, you are on your way to savings!'))

        lead = Lead.query.filter_by(email=personalInfoForm.email.data).first()
    return render_template('quote/personal-form.html', title=_('Personal Info Form'), PersonalInfoForm=personalInfoForm)
