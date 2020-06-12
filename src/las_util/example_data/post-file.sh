#
# File-Name: post-file.sh
# File-Desc: Use the las-util api to post a log ascii file
# App-Name: las-util-django
# Project-Name: Las-Util-Django
# Copyright: Copyright (c) 2019, DC Slagel and contributors
# License-Identifier: BSD-3-Clause

# Check for command line arguments and display usage if needed
if [ $# -eq 0 ]
then
  echo "Usage: post-file.sh [las filepath]"
  exit 1
fi

las_file_path="${1}"

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
-F "filename=@${las_file_path}" \
-H "X-CSRFToken: ${token}" \
-H "Cookie: csrftoken=${token}"
