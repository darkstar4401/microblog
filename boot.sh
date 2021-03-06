#!/bin/sh
# this script is used to boot a Docker container
source venv/bin/activate
while true; do
    #flask db upgrade
    if [[ "$?" == "0" ]]; then
        break
    fi
    echo Deploy command failed, retrying in 5 secs...
    sleep 5
done
flask translate compile
exec gunicorn --certfile cert.pem --keyfile key.pem -b :7000 --access-logfile - --error-logfile - microblog:app
