# install environment
python -m venv venv

# activate environment (can be done with VS code extensions)
linux:

  source venv/bin/activate

windows:

  venv\Scripts\activate.bat
 
# install requirements (use venv to avoid destroying your computer)
pip install -r requirements.txt

# config database (skip if used docker-compose to run config in db folder)
CREATE USER se_db_user SUPERUSER;

ALTER USER se_db_user WITH PASSWORD 'se_db_secret';

CREATE DATABASE se_db WITH OWNER se_db_user;

# migrate database (create table, alter field- run when there are changes in models)
python manage.py makemigrations

python manage.py migrate

# runserver
python mange.py runserver

# or run this command to bind the port with the system ip
python mange.py runserver 0.0.0.0:8000
