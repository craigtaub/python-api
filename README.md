# REST API

Example REST API in Python.

## Run dev mode

        python3 src/app.py

## Run unit tests
Add test + src to system path.

        export PYTHONPATH=/Users/craig/Documents/python/api/src:/Users/craig/Documents/python/api/test

        export PYTHONPATH=/Users/craigtaub/Documents/python/python-api/src:/Users/craigtaub/Documents/python/python-api/test
    
Run tests:

        python test/test_mapped.py -v

## Setup
        sudo easy_install pip
        sudo pip3 install -r requirements.txt

## Issues
Mock install issue.

        sudo -H pip install --ignore-installed mock==1.0.1