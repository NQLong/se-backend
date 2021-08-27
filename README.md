# install environment
pip install -r requirements.txt

# config database (skip if use docker-compose to run config in db folder)
CREATE USER mobile_db_user SUPERUSER;

ALTER USER mobile_db_user WITH PASSWORD 'mobile_db_secret';

CREATE DATABASE mobile_db WITH OWNER horus_dev;

# migrate database (create table, alter field- run when there are changes in models)
python manage.py makemigrations

python manage.py migrate

# runserver
python mange.py runserver

# or run this command to bind the port with the system ip
python mange.py runserver 0.0.0.0:8000
