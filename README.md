NAME
----

LAS Util - LAS web tools in Python/Django


DESCRIPTION
-----------
Caution: This is beta software!

LAS (Log Ascii Standard - Version 2.0) web utilities in Python/Django.

The current version is a stand-alone Django site/app combination that runs on
a Django development server.

LAS well log file format versions are written and maintained by    
the Canadian Well Logging Society at      
https://www.cwls.org/products/

`LAS-Util-Django` current functionality:
- Upload a LAS file that includes only the VERSION and WELL sections.
- Parse the VERSION and WELL sections.
- Store the parsed data in a SQLite database.
- Display a list of processed files with links to their details.
- Display detailed data in a table format.
- Provide api for listing uploaded LAS docs and details.
- Provide api for uploading LAS docs.
- Unit testing with data fixtures.
- Test coverage reporting.

It has been tested with Django 2.2.10.

The default database is sqlite.

Future versions will implement:
- Parse the PARAMETER section.
- Add test for file upload.
- Update interface for multiple device formats.
- Update packaging to include a reusable-app that can be installed at other
  Django sites.



SYNOPSIS
--------

  ```bash
  # Setup:

  ## 1. Make workdir.
  mkdir workdir
  cd workdir

  ## 2. Create virualenv.
  python3 -m venv site-venv
  source site-env/bin/activate


  ## 3. Either clone this GitHub repository, or download a release package.

  ### Option 1: Clone the GitHub repository.
  git clone https://github.com/dcslagel/las-util-django

  ### Option 2: Download a release package (either a .zip or a .tar.gz package).
  ###   Packages can be found at: https://github.com/dcslagel/las-util-django/releases.

  ###   Example download cmds:
  ###     Note: Even though these paths say 'archive' rather than 'release' it looks like we
  ###           still need to go to the release url to find these paths.
  curl -L https://github.com/dcslagel/las-util-django/archive/v0.1.0tar.gz -o v0.1.0.tar.gz
  ### or
  wget https://github.com/dcslagel/las-util-django/archive/v0.1.0.tar.gz

  ###  Unpack release package with
  unzip v0.1.0.zip 
  ### or (your tar cmd may require different flags).
  tar -xvf v0.1.0.tar.gz


  ## 4. Install python/django dependencies.
  cd las-util-django/
  pip install -r requirements.txt

  ## 5. Prep django database.
  ## cd las-util-django/src/
  cd src
  ## makemigrations should report no new migrations.
  python manage.py makemigrations
  python manage.py migrate


  ## 6. Run test suite: All tests should pass.
  ## If any test fails report test failure at:
  ##  https://github.com/dcslagel/las-util-django/issues
  ##    Include the release number or git commit of las_util_django
  ##    and the test failure text.
  python manage.py test

  ## 7. Run dev web server.
  python manage.py runserver
  ```

  then in a web browser browse to:  
  http://127.0.0.1:8000/upload/

  Select one of these LAS files to upload:
  - las-util-django/src/las_util/example_data/version.las
  - las-util-django/src/las_util/example_data/sample_2.0_well_section.las

  Click 'upload'    

  LAS-Util will:
  - parse the version and well sections and save them to the database

Select the 'Display-Files' menu item. The uploaded file will have the most recent date.

  The resulting data files will be displayed at:  
  http://127.0.0.1:8000/list/

REST API
--------

To upload a LAS doc use a post command:
```bash
# Run a GET in order to retrieve the csrftoken in a cookie.
curl -c cookie.txt http://127.0.0.1:8000/upload/ --silent -S --output /dev/null

# The crsf token is in the 7th field of the cookie.
# optionally: grep csrftoken cookie.txt | cut -f 7
token=$(awk '/.*csrftoken/ {print $7}' cookie.txt)


# Notes:
# In '-F' 'filename' is the name field of: 
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

To retrieve details of a specific LAS doc:
Syntax:    
```bash
curl http://127.0.0.1:8000/api/detail/[filename]    
```

Example:     
```bash
# first retrieve a filename from the pervious 'api/list' call.
# example: las_file-2019-08-29-21-41-42
curl http://127.0.0.1:8000/api/detail/las_file-2019-08-29-21-41-42
```


DEPENDENCIES
------------

| Component | Version |
|-----------|---------|
| coverage              | 4.5.4  | 
| Django                | 2.2.10 | 
| Django-Rest-Framework | 3.10.3 | 
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
- Report bugs by creating an issue at:    
  https://github.com/dcslagel/las-util-django/issues

COPYRIGHT
------

Copyright (c) 2019 - 2020 DC Slagel
