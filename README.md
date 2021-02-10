### NHSEE Scoring Web Application

This application was made for NHSEE for the purpose of gathering scores for the students projects, and calculating the average score of 5 judges given to 1 project and store it in the app.

 *     Rank is based on the average score of the project.

 *     Z-score = (raw score for that project – that judge’s average score for all projects) / (the standard deviation       of that judge’s scores for all projects).

 *     Scaled “score”, “z” and “rank” is the normalization of these entities to be in the range of 25 and 50.


Deployment

URL:https://nhseeapp.herokuapp.com/

* Models
* views
* Templates
* Calculations
* Heroku Deployment
* Pycode style
* Testing

App Usage




### Requirements

* python 3.7

* pipenv

* Django 2.1.15

* django-import-export 1.2.0


### Developers of this NHSEE Application

Snehal Jadhav --(https://www.linkedin.com/in/snehal-jadhav-2a92273b/)


### Installation Guide


*     Install python virtual environment with Django 
      pipenv install django --python=3.7

*     Start virtual environment
      pipenv shell

*     Migrate the database
      python manage.py migrate nhsee

*     Run the server
      python manage.py runserver


