# mongologin
A guestbook like app that has <b>MongoDB</b> and <b>django</b>(mongoengine + pymongo) for backend with some polymer front end and most importantly, creating a REST API with django's rest framework 


# Mongologin API Documentation
- starts at homes/usrs/
## returns the following fields into json format
    name = StringField(max_length=50)
    email = StringField(max_length=50)
    usrnm = StringField(max_length=50)
    pss = StringField(max_length=50)
    githuburl = StringField(max_length=50)
    bio = StringField(max_length=50)
    
    sample url: GET "https://localhost:8000/homes/usrs/{username}"
## commands    
POST DATA to create usrs
GET DATA to retrieve all usrs
   - GET SPECIFIC to retrieve specific user
PUT, PATCH , DELETE ETC.
