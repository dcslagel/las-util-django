# run a GET in order to retrieve the csrftoken in a cookie
curl -c cookie.txt http://127.0.0.1:8000/upload/ --silent -S --output /dev/null

# the crsf token is in the 7th field of the cookie
# optionally: grep csrftoken cookie.txt | cut -f 7
token=$(awk '/.*csrftoken/ {print $7}' cookie.txt)


# Notes:
# 1. -X POST is not needed because -F implies 'POST'
# 2. In '-F' 'filename' is the name field of: 
#   <input type="file" name="filename" required="" id="id_filename">

#--------------------------------------------------------------------
curl http://127.0.0.1:8000/api/upload/ \
-v \
-X GET \
-F "filename=@version.las" \
-H "X-CSRFToken: ${token}" \
-H "Cookie: csrftoken=${token}"
