**Instagram**

**Description**
This is a clone of the image sharing network, Instagram. Users can sign up login, view and post photos and follow other users.

**Author**
Joe Muriithi
**Setup and installation**

Clone the Repo

git clone https://github.com/Muriithijoe/Instagram-project.git

cd instagram

*Activate virtual environment*
create and acvite a virtual environment python3.6 -m venv virtual && source virtual/bin/activate

*Install dependancies*
Install dependancies that will create an environment for the app to run pip install -r requirements.txt

*Create the Database*
- psql
- CREATE DATABASE instaclone;
.env file
Create .env file and paste paste the following filling where appropriate:

SECRET_KEY = '<Secret_key>'
DBNAME = 'database name'
USER = '<Username>'
PASSWORD = '<password>'
DEBUG = True
Run initial Migration
python3.6 manage.py makemigrations instaclone
python3.6 manage.py migrate
Run the app
python3.6 manage.py runserver
**Technologies Used**
Python 3.6 and The Django framework
HTML, CSS and Bootstrap
JavaScript
Heroku
**License**
This project is licensed under the MIT License - see the LICENSE file for details
