# run a GET in order to retrieve the csrftoken in a cookie
curl -c cookie.txt http://127.0.0.1:8000/upload/ --silent -S --output /dev/null

# the crsf token is in the 7th field of the cookie
# optionally: grep csrftoken cookie.txt | cut -f 7
token=$(awk '/.*csrftoken/ {print $7}' cookie.txt)


curl http://127.0.0.1:8000/upload/ \
-X POST \
-F "myinfile=@version.las" \
-H "X-CSRFToken: ${token}" \
-H "Cookie: csrftoken=${token}"
