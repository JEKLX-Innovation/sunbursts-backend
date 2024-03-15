# Sunbursts

## Group Members

Johnny Backus, Kaitlin Davis, Xin Deng, Errol Vidad, Lana Zumbrunn

### Summary of project:

This project will allow an admin to collect data from participants in a way that doesn’t require participants to use a spreadsheet which is prone to errors when formulas get messed up.

It will make analyzing the data easier for the admin. Right now, pulling together the data from all the participants is labor intensive.

It will allow for data visualization that is beautiful and easily digestible.


### Overview - Django Permissions & Postgresql

Complete at end of week. This project uses Django and Django Rest Framework together. It builds out a Restful API as well as a user facing site and data in a remote database.

#### Version 1.0

Build 1.0 Feature Tasks

1. Use API quick start [template](https://github.com/codefellows/python-401-api-quickstart)
2. Install from requirements.txt
3. Update templates to match cookie stand model
4. Host database at elephantSQL

### How to Initialize/Run Application

- `python manage.py runserver`

## Customization Steps

- DO NOT migrate yet
- add additional dependencies as needed
  - Re-export requirements.txt as needed
- change `things` folder to the app name of your choice
- Search through entire code base for `Thing`,`Things` and `things` to modify code to use your resource
  - `project/settings.py`
  - `project/urls.py`
  - App's files
    - `views.py`
    - `urls.py`
    - `admin.py`
    - `serializers.py`
    - `permissions.py`
  - "Front" files
    - if including a customer facing portion of the site then update/recreate:
      - `urls_front.py`
      - `views_front.py`
      - template files
      - Make sure to update project `urls.py` to add routes to the "front".
- Update ThingModel with fields you need
  - Make sure to update other modules that would be affected by Model customizations. E.g. serializers, tests, etc.
- Rename `project/.env.sample` to `.env` and update as needed
  - To generate secret key use `python3 -c "import secrets; print(secrets.token_urlsafe())"`
- Run makemigrations and migrate commands when ready.
- Run `python manage.py collectstatic`
  - This repository includes static assets in repository. If you are using a Content Delivery Network then remove `staticfiles` from repository.
- Optional: Update `api_tester.py`

## Database

**NOTE:** If you are using Postgres instead of SQLite then make sure to install `psycopg2-binary` and include in `requirements.txt`


### Deployed Link



#### For Lana list of possible commands for monica to know

`python manage.py runserver
source .venv/bin/activate
python manage.py migrate  
python manage.py makemigrations sunbursts
pip install -r requirements.txt
python3 -c "import secrets; print(secrets.token_urlsafe())"`
