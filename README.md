# Django Girls Tutorial

This is an application written as a tutorial for Django girls

## Getting Started

To get started first go to the project Github URL and then open VsCode

Click File -> New Window
Click on Clone Git Repository in the Main screen
Paste the URL of the Github Repo

## Running the Application

First you need to make a virtual environment
Type this in your preferred terminal (Powershell or anything else)

```console
> python -m venv myvenv
> myvenv\Scripts\activate
```
Then you want to install everything from the requirements.txt file

```console
> pip install -r requirements.txt
```

Migrate the existing migrations to a new database

```console
> python manage.py migrate
```

Then you can run the server

```console
> python manage.py runserver
```


