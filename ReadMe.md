### Steps 

#### 1.  pip  insatll  -r  requirements.txt
#### 2.  python  manage.py  makemigrations
#### 3.  python  manage.py  migrate
#### 4.  python  manage.py  runserver

#### 5.  python  manage.py createsuperuser
#### celery -A  hq  worker -l  info   (start this under the project directory celery exists)

#### 6.  python  manage.py  runserver

#### hit urls http://127.0.0.1:8000/users/  and http://127.0.0.1:8000/generate the celary task will be executed

