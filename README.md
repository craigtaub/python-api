# REST API

Example REST API in Python with flask.

## Run dev mode

        FLASK_DEBUG=1 FLASK_APP=src/app.py flask run

## Run unit tests
Add test + src to system path.

        export PYTHONPATH=/Users/craig/Documents/python/api/src:/Users/craig/Documents/python/api/test
    
Run tests:

        python test/test_mapped.py -v

## Setup
        sudo easy_install pip
        sudo pip install -r requirements.txt

## Tools
- Flask - http://flask.pocoo.org/