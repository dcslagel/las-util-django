NAME
----

LAS Util - LAS web tools in Python/Django


DESCRIPTION
-----------
Caution: This is beta software!

LAS (Log Ascii Standard) web utilities in Python/Django

LAS well log file format versions are written and maintained by    
the Canadian Well Logging Society at      
http://www.cwls.org/las/

`LAS-Util-Django` current functionality:
- Upload a LAS file that includes only the VERSION section
- Parse the VERSION section and save it to the database
- Store the parsed data in a SQLite database.
- Display a list of processed files with links to their details
- Display detailed data in a table format
- Provide api for listing uploaded LAS docs and details
- Provide api for uploading LAS docs
- Unit testing with data fixtures
- Test coverage reporting

It has been tested with Django 2.2.6.

The default database is sqlite.

Future versions will implement:
- Parse the 'Well-Information' section if included in the upload file
- Add test for file upload
- Update interface for multiple device formats


SYNOPSIS
--------

  ```bash
  # Setup:

  ## Make workdir
  mkdir workdir
  cd workdir

  ## Create virualenv
  python3 -m venv site-venv
  source site-env/bin/activate

  ## Clone the project
  git clone https://github.com/dcslagel/las-util-django

  ## Install python/django dependencies
  cd las-util-django/
  pip install -r requirements.txt

  ## Prep django database
  ## cd las-util-django/src/
  cd src
  python manage.py makemigrations
  python manage.py migrate


  ## Run test suite: All tests should pass
  python manage.py test

  ## Run dev web server
  python manage.py runserver
  ```

  then in a web browser browse to:  
  http://127.0.0.1:8000/upload/

  Select a LAS file to upload.  The version.las in    
  las-util-django/src/las_util_django/raw_data is a simple test file.   
  Click 'upload'    

  LAS-Util will:
  - upload the file to las-util-flask/src/uploads
  - parse the version section and save it to the database

Select the 'Display-Files' menu item. The uploaded file will have the most recent date.

  the resulting data files will be displayed at:  
  http://127.0.0.1:8000/list/

REST API
--------

To upload a LAS doc use a post command:
```bash
# run a GET in order to retrieve the csrftoken in a cookie
curl -c cookie.txt http://127.0.0.1:8000/upload/ --silent -S --output /dev/null

# the crsf token is in the 7th field of the cookie
# optionally: grep csrftoken cookie.txt | cut -f 7
token=$(awk '/.*csrftoken/ {print $7}' cookie.txt)


# Notes:
# 1. In '-F' 'filename' is the name field of: 
#   <input type="file" name="filename" required="" id="id_filename">

#--------------------------------------------------------------------
curl http://127.0.0.1:8000/api/upload/ \
-v \
-X POST \
-F "filename=@version.las" \
-H "X-CSRFToken: ${token}" \
-H "Cookie: csrftoken=${token}"
```

To retrieve uploaded LAS docs:
```bash
curl http://127.0.0.1:8000/api/list/
```

To retreive details of a specific LAS doc 
Syntax:    
```bash
curl http://127.0.0.1:8000/api/detail/[filename]    
```

Example:     
```bash
# first retrieve a filename from the prvious 'api/list' call
# example: las_file-2019-08-29-21-41-42
curl http://127.0.0.1:8000/api/detail/las_file-2019-08-29-21-41-42
```


DEPENDENCIES
------------

| Component | Version |  
|-----------|---------|
| coverage              | 4.5.4  | 
| Django                | 2.2.6  | 
| Django-Rest-Framework | 3.10.2 | 
| Pytz                  | 2019.2 | 
| Sqlite3               | |

Django and Django-Rest-Framework can be installed with
```
cd las-util-django/
pip install -r requirements.txt
```

BUGS
----

- Functionality is basic.


COPYRIGHT
------

Copyright (c) 2019 DC Slagel
