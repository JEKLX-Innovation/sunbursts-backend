# JEKLX Innovation

## Team

Johnny Backus, Kaitlin Davis, Xin Deng, Errol Vidad, Lana Zumbrunn

## Summary of project

This app allows an admin to upload participant data from a .csv file and visualize the data in a circular barplot.

It strives to make analyzing participant data easier for the admin and allow for beautiful and easily digestible data for the admin's clients.

### Features

#### Full Implementation

* Upload static .csv data and visualize in circular barplot
* Upload elements and assign to project
* Create surveys customized for project
* Participant survey administration and data collection via unique link

#### Partial Implementation

The app also provides database models and partial implementation of additional functionality including:

* Analysis capabilities of participant survey data
* Calculation of participant data received, displayed per project from survey submissions
* Survey creation with multiple customized admin inputs

Bug Fixes
* Math calculations are able to get data from database but not able to separate surveys and apply calculations per survey.
* Bug fix needed on naming conventions to properly match data.

#### Recommended Features

* Admin Dashboard
    * Create an html interface for smoother admin UI/UX to
* Implement by adding additional views, templates and urls for usability
* Upgrade styling to align with BeSpace branding
* Integrate with existing BeSpace site client login


## Technical Overview - Django Permissions & Postgresql

This project uses Django and Django Rest Framework together. It builds out a Restful API as well as a user facing site and data in a remote database.

### Tech Stack

* Django
* Django REST Framework
* Matplotlib
* NumPy
* Pandas

## Getting Started

* Install python if not already installed `pip install python`
* Create a virtual environment

``` python
mkdir myproject
cd myproject
python3 -m venv venv
```

* Activate virtual environment `source venv/bin/activate`
* Install requirements `pip install requirements.txt`
* Host database
* Add database engine, name, user, password, host and port to .env

### How to Initialize/Run Application

* `python manage.py runserver`
