# medical-record-management

**Basic Concept:**\
A medical record management system designed for the hospital setting. It will allow doctors to document patient information, provide updates, and keep track of medical/family history.

**Technical Stack:** \
Python\
Flask/SQLAlchemy - makes the product easier to deploy with the availability of database templates\
PostgreSQL (?)\
Docker (?)\
HTML/CSS/JS/etc.

**Functional Requirements:**\ 
Log in view\
Sign up view\
Patient profile view\
Add patient view\
Edit patient view\
Patient roster view (to see all the patients in the system)\
Import records from other software\
Export records to a common format\
HIPAA compliance

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
