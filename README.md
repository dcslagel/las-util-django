NAME
----

LAS Util - LAS web tools in Python/Django

TABLE-OF-CONTENTS
-----------------
- [DESCRIPTION](#description)
- [DEPENDENCIES](#dependencies)
- [SYNOPSIS](#synopsis)
- [REST-API](#rest-api)
- [PROJECT-ROADMAP](#project-roadmap)
- [FEATURE-REQUEST](#feature-request)
- [BUGS](#bugs)
- [COPYRIGHT](#copyright)


[DESCRIPTION](#name)
-----------
Caution: This is beta software!

LAS (Log Ascii Standard - Version 2.0) web utilities in Python/Django.

The current version of LAS-Util is a stand-alone Django site/app combination
that runs on a Django development server.

LAS well log file format versions are written and maintained by    
the Canadian Well Logging Society at      
https://www.cwls.org/products/

`LAS-Util-Django` current functionality:
- Upload a LAS file that includes the VERSION and optionally: WELL, CURVE,
  PARAMETER and optional OTHER sections.
- Parse the VERSION, WELL, CURVE, PARAMETER and OTHER sections.
- Store the parsed meta-data in a SQLite database.
- Display a list of processed files with links to their details.
  Note: Currently LAS-Util renames the uploaded files to `las_file-[datetime]`
- Display detailed data in a table format.
- Provide api for listing uploaded LAS docs and details.
- Provide api for uploading LAS docs.
- Unit testing with data fixtures.
- Test coverage reporting.
- Responsive display on most devices.


LAS-Util has been tested with Django version 4.1.6

The default database is sqlite.

[DEPENDENCIES](#name)
------------

| Component             | Version  |
|-----------------------|----------|
| asgiref               | 3.6.0    |
| coverage              | 7.1.0    |
| Django                | 4.1.6    |
| Django-Rest-Framework | 3.14.1   |
| Pytz                  | 2022.7.1 |
| Sqlparse              | 0.4.3    |
| Sqlite3               | 3.24.0   |

Django and Django-Rest-Framework can be installed with
```
cd las-util-django/
pip install -r requirements.txt
```

[SYNOPSIS](#name)
---------

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
  curl -L https://github.com/dcslagel/las-util-django/archive/v0.1.2tar.gz -o v0.1.2.tar.gz
  ### or
  wget https://github.com/dcslagel/las-util-django/archive/v0.1.2.tar.gz

  ###  Unpack release package with
  unzip v0.1.2.zip
  ### or (your tar cmd may require different flags).
  tar -xvf v0.1.2.tar.gz


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


[REST-API](#name)
--------

To upload a LAS doc use a post command:
```bash
# Cd to the example_data directory
cd las-util-django/src/las_util/example_data

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

To retrieve details of a specific LAS doc in JSON format:

Syntax:    
```bash
curl http://127.0.0.1:8000/api/detail/[filename]    
```

Example:     
```bash
# first retrieve a filename from the pervious 'api/list' call.
# example: las_file-2019-08-29-21-41-42.las
curl http://127.0.0.1:8000/api/detail/las_file-2019-08-29-21-41-42.las
```


[PROJECT-ROADMAP](#name)
----------------
NOTE: This project is NOT being actively developed.

Here is the last roadmap before development stopped.    
`LAS-Util-Django`'s project road-map is managed in github milestones at:
- https://github.com/dcslagel/las-util-django/milestones

The current work-in-progress milestone is 0.1.3:
- https://github.com/dcslagel/las-util-django/milestone/6
- Goals:
  - Add initial parse and display functionality for the ~ASCII (data) section


[FEATURE-REQUEST](#name)
----------------
To request and discuss a potiential feature create an issue at:
- https://github.com/dcslagel/las-util-django/issues


[BUGS](#name)
----

- Functionality is basic.
- Report bugs by creating an issue at:    
  https://github.com/dcslagel/las-util-django/issues

[COPYRIGHT](#name)
---------

Copyright (c) 2019 DC Slagel and contributors
