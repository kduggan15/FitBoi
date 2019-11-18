#!/bin/bash
g='\033[1;32m'
n='\033[0m'
m1='cleared all __pycache__!'
m2='server hosted on: http://localhost:8000/fitboi'
rm -rfv fitboitech/fitboi_photo/__pycache__
rm -rfv fitboitech/fitboi_photo/migrations/__pycache__
rm -rfv fitboitech/fitboitech/__pycache__
rm fitboitech/db.sqlite3
echo -e "$g$m1$n"
cd fitboitech
python manage.py migrate
echo -e "$g$m2$n"
python manage.py runserver
