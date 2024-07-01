FROM python:3.12.3-slim

RUN mkdir code
WORKDIR code



ADD . /code/
ADD .env.docker /code/.env

ENV APP_NAME = MY_NEW_PROJECT


RUN pip install -r requirements.txt

CMD gunicorn my_new_project.wsgi:application -b 0.0.0.0:8000

#CMD python manage.py runserver 8000