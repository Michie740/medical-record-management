# medical-record-management

**Instructions**
1. To run this project locally, fork and clone the repo (ideally in a virtual environment)
1. Navigate into medical_record_management 
1. Run `make setup_dev` to setup dependencies and build DBs
1. Run `make lint` to use flake8 linter on all .py files
1. Run `python manage.py runserver` to run locally
1. Navigate to `127.0.0.1:8000/` on browser for home page
1. To view admin style, create superuser using `python manage.py createsuperuser` and then navigate to `127.0.0.1:8000/admin`
1. For testing: run `make tests` or `make coverage` depending on if you just want to run tests or if you want a full coverage report


**Email Authentication**
1. As of 11/18/21, email authentication for new accounts has been added.
1. For testing purposes, this can easily be switched off by setting `ACCOUNT_EMAIL_VERIFICATION = False` in settings.py
1. When running locally, emails are sent to the medical_record_management_project/emails directory. Follow the link to verify email accounts for a user. Do so quickly before link expires or resend link if necessary.


**Basic Concept:**\
A medical record management system designed for the hospital setting. It will allow doctors to document patient information, provide updates, and keep track of medical/family history.


**Database Design**
[Medical Record Management Database Design.pdf](https://github.com/Michie740/medical-record-management/files/7165864/Medical.Record.Management.Database.Design.pdf)


**Technical Stack:** \
Python\
Django\
PostgreSQL\
Docker (?)\
HTML/CSS/JS/etc.

**Functional Requirements:**\ 
Log in view\
Sign up view\
Patient profile view\
Add patient view\
Edit patient view\
Patient roster view (to see all the patients in the system)\

**Project Plan:**\
Create database design\
Implement encryption that abides by HIPAA requirements\
Begin with basic web application functionality (log-in/sign-up, create patient, update patient record)\
Add MFA and further security measures\
Add additional functionality (details regarding patients, linking patients based on family connections, etc.)

**Stretch Goals:**\
User friendly design\
Create a place to upload images/documents such as X-Rays, ultrasound images, etc.\
Create a place for prescriptions to be uploaded/tracked, etc.\
Link to patient’s insurance plan using API (?)\
Create a patient view to add updates, fill out forms, etc.\
Create patient roster for individual doctors (based on rounds)\
Ease of deployment and migration
HIPAA compliance
Import records from other software\
Export records to a common format\
