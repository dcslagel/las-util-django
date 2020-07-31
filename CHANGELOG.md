# CHANGELOG


## 0.1.1 - 2020-06-20

Goal: Parsing of standard meta-data headers not including ~ASCII.

### Added

Update to Django 3.0.7
Parse all the required meta-data sections: Version, Well, Curve, Parameter.
Parse the optional Other section.
Add initial metadata-parsing tests


## 0.1.0 - 2020-05-24

Initial release of las-util-django:

Caution: This is beta software!

### Added

Upload a LAS file that includes only the VERSION and WELL sections.
Parse the VERSION and WELL sections.
Store the parsed data in a SQLite database.
Display a list of processed files with links to their details.
Display detailed data in a table format.
Provide api for listing uploaded LAS docs and details.
Provide api for uploading LAS docs.
Unit testing with data fixtures.
Test coverage reporting.
