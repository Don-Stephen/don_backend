#don_backend
[![Build Status](https://travis-ci.org/Don-Stephen/don_backend.svg?branch=master)](https://travis-ci.org/Don-Stephen/don_backend)

An app for gathering requirements and converting them to tests.. Check out the project's [documentation](http://Don-Stephen.github.io/don_backend/).

# Prerequisites 
- [virtualenv](https://virtualenv.pypa.io/en/latest/)
- [mysql](mysql server)

# Initialize the project
Create and activate a virtualenv:

```bash
apt-get install -y python3.4-dev gcc libmysqlclient-dev mysql-server virtualenvwrapper
```

```bash
mkvirtualenv -p `which python3.4` don_backend
```
Install dependencies:

```bash
pip install -r requirements/local.txt
```
Create the database:

in the mysql cli

```mysql
create database don_stephen;
```

Migrate, create a superuser, and run the server:
```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
