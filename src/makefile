# File-Name: makefile 
# File-Desc: Makefile for main commands running ludr
# App-Name: las-util-django
# Project-Name: Las-Util-Django
# Copyright: Copyright (c) 2019, DC Slagel
# License-Identifier: BSD-3-Clause

run: ## run django dev server
	python manage.py runserver

makemigrations: ## update database migration configs
	python manage.py makemigrations

migrate: ## apply any database migrations
	python manage.py migrate

dumpdata: ## dump data to fixture
	python manage.py dumpdata --indent 2 las_util.versioninfo > las_util/fixtures/version_info_data.json

loadtestdata:
	python manage.py loaddata las

test: ## Run las_util test suite
	# python manage.py test las_util
	# python -Wa manage.py test las_util
	python -Wignore::DeprecationWarning:distutils.* manage.py test las_util

testmodels: ## Run las_util model tests
	python manage.py test las_util.tests.test_models

testviews: ## Run las_util route tests
	python manage.py test las_util.tests.test_views

coverage: ## Run coverage report: see local .coveragerc for settings
	# coverage run --source=las_util manage.py test las_util
	coverage run manage.py test las_util
	coverage report -m
	# coverage html


# Add the following 'help' target to your Makefile
# # And add help text after each target name starting with '\#\#'

help: ## This help dialog.
	@IFS=$$'\n' ; \
	help_lines=(`fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##/:/'`); \
	printf "%-30s %s\n" "target" "help" ; \
	printf "%-30s %s\n" "------" "----" ; \
	for help_line in $${help_lines[@]}; do \
	    IFS=$$':' ; \
	    help_split=($$help_line) ; \
	    help_command=`echo $${help_split[0]} | sed -e 's/^ *//' -e 's/ *$$//'` ; \
	    help_info=`echo $${help_split[2]} | sed -e 's/^ *//' -e 's/ *$$//'` ; \
	    printf '\033[36m'; \
	    printf "%-30s %s" $$help_command ; \
	    printf '\033[0m'; \
	    printf "%s\n" $$help_info; \
	done
