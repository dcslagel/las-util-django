NAME
----
ludr - basic Las-Util app in Django

SYNOPSIS
--------

  ```
  # Setup:
  git clone https://github.com/dcslagel/las-util-django

  ## install python/django dependencies
  cd las-util-django/
  pip install -r requirements.txt

  ## prep django database
  ## cd las-util-django-rest/src/
  cd src
  python manage.py makemigrations
  python manage.py migrate


  ## Run dev web server
  python manage.py runserver
  ```

  then in a web browser browse to:  
  http://127.0.0.1:8000/upload

  Select a LAS file to upload. Ludr will upload the file, parse the data and store
  the date in a database for retrieval.

  the resulting data files will be displayed at:  
  http://127.0.0.1:8000/display


DESCRIPTION
-----------
Caution: This is very beta software!

`ludr` currently uploads and reads the version section of LAS formatted file.
Additional sections will be added in future pushes.

It has been tested with Django 2.2.4.

The default database is sqlite.

DEPENDENCIES
------------

| Component | Version |  
|-----------|---------|
| Django |  2.2.4 |  
| Django-Rest-Framework |  3.10.2 |  
| Pytz |  2019.2 |  
| Reactjs    |  
| Sqlite3    |  

Django and Django-Rest-Framework can be installed with
```
cd las-util-django/
pip install -r requirements.txt
```

BUGS
----

- Functionality is very basic.


COPYRIGHT
------

Copyright (c) 2019 DC Slagel
