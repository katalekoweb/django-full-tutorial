# Django Tutorial
Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design.
Created by experienced developers, it takes care of much of the hassle of web development, so you can focus on writing your app without needing to reinvent the wheel.

### Check Python Version

```bash
python3 --version
```

## Create Virtual Enviroment

```bash
python3 -m venv ven
```

## Activate Virtual Environment

```bash
source ven/bin/activate
```

## Deactivate Virtual Environment

```bash
deactivate
```

## Install Requirements

```bash
pip install -r requirements.txt
```

## Create Django Project

```bash
django-admin startproject project_name
```

## Run Django Server

```bash
python manage.py runserver
```

## Create Django App

```bash
python manage.py startapp app_name
```

## Create Database Migrations

```bash
python manage.py makemigrations
```

## Apply Database Migrations

```bash
python manage.py migrate
```

## Create Superuser

```bash
python manage.py createsuperuser
```

## What is an ORM
Object Relational Mapping (ORM) is a programming technique that allows developers to interact with a database using an object-oriented paradigm. It abstracts the database interactions, enabling developers to work with database records as if they were regular Python objects, without writing raw SQL queries.

## Libs
- **Django**: A high-level Python web framework that encourages rapid development and clean design.
- **Django REST Framework**: A powerful toolkit for building Web APIs in Django.
- **Pillow**: A Python Imaging Library that adds image processing capabilities to your application.