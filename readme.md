### to run
make sure you have django installed
fork and clone this repo

run `pip3 install psycopg2` <br>
then `createdb monikr` <br>
run these next 2 lines of code after any database changes you have <br>
`python3 manage.py makemigrations`
and `python3 manage.py migrate`

if you add any new models, to see them on the admin page, you must
import and register them in admin.py

