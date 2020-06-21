## How to run Django and postgreSQL with docker

## 1. Create docker file
```
""" Dockerfile """

FROM python:3.8

# Install missing libs
RUN apt-get  update \
    && apt-get install -y  curl libpq-dev gcc python3-cffi git && \
    apt-get clean autoclean && \
    apt-get autoremove --purge -y && \
    rm -rf /var/lib/apt/lists/* && \
    rm -f /var/cache/apt/archives/*.deb

# Creating Application Source Code Directory
RUN mkdir -p /usr/app

# Setting Home Directory for containers
WORKDIR /usr/app

# Installing python dependencies
COPY requirements.txt /usr/app
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install gunicorn

# Cleanup
RUN rm -rf /var/lib/apt/lists/*
RUN rm -rf /root/.cache/*
RUN rm -rf /tmp/*
RUN apt-get -y autoremove --purge && apt-get -y autoclean && apt-get -y clean
RUN rm -rf /usr/share/man/*
RUN rm -rf /usr/share/doc/*
RUN find /var/lib/apt -type f | xargs rm -f
RUN find /var/cache -type f -exec rm -rf {} \;
RUN find /var/log -type f | while read f; do echo -ne '' > $f; done;

# Copying src code to Container
COPY . /usr/app
RUN pip install --no-cache-dir -r requirements.txt

# Exposing Ports
EXPOSE 8000

# Environemnt variables
ENV DJANGO_ENV  development
ENV GUNICORN_BIND  0.0.0.0:8000
ENV GUNICORN_WORKERS 4
ENV GUNICORN_WORKERS_CONNECTIONS 1001

# Running Python Application
# CMD python manage.py runserver 0.0.0.0:8000
# CMD gunicorn --workers=${GUNICORN_WORKERS} config.wsgi:application -b ${GUNICORN_BIND} --log-level info

```

## 2. Create docker-compose.yaml file
```
""" docker-compose.yaml """

version: '3.8'

services:
  web:
    build: .
    command: python manage.py runserver 0.0.0.0:8000
    ports:
      - 8000:8000
    depends_on:
      - db
  db:
    image: postgres:11
    environment:
      POSTGRES_DB: "db"
      POSTGRES_PASSWORD: "postgres"

```

## 3. Set postgreSQL backend connection in Django settings.py file
```
""" settings.py """

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'db',
        'PORT': 5432
    }
}
```

## 4. Build and run docker containers (web and db)
```
$ docker-compose build
$ docker-compose run
```

## 4. Run django makemigrations and migrate commands
```
$ docker-compose exec web python manage.py makemigrations

$ docker-compose exec web python manage.py migrate
```

## 5. Run django createsuperuser command
```
$ docker-compose exec web python manage.py createsuperuser
```

## 6. Visit api endpoint http://127.0.0.1:8000/api/v1/

## 7. Check logs
```
$ docker-compose logs
```