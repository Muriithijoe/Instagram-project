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
MIT License

Copyright (c) [2018] [Joe Muriithi Wambugu]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
