# Useful Links

- Code formatter [black](https://black.readthedocs.io/en/stable/)
- Sentry
- Testing and mocking with coverage
- Celery
- [Gunicorn](https://gunicorn.org/) , WSGI HTTP Server.
- [GitHub Actions](https://docs.github.com/en/actions) , CI/CD.
- [Genrate django secret key](https://djecrety.ir/)
- [pipenv basics](https://blog.saurav-shrivastav.tech/-setting-up-a-basic-django-project-with-pipenv)
- [djoser](https://djoser.readthedocs.io/en/latest/getting_started.html)

- [Postgresql cheatsheet](https://www.postgresqltutorial.com/postgresql-cheat-sheet/)

- custom user

https://cpadiernos.github.io/how-to-add-fields-to-the-user-model-in-django.html
https://youtu.be/KiJFHBQ44sw
https://youtu.be/Ae7nc1EGv-A
https://youtu.be/KiJFHBQ44sw

- [Deployment Checklist](https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/)
- [Custom User Model](https://docs.djangoproject.com/en/4.0/topics/auth/customizing/#specifying-a-custom-user-model)
- [unittest library](https://docs.python.org/3/library/unittest.html)
- [Code Formatter](https://pypi.org/project/black/)
- [Upgrade all outdated packages](https://www.activestate.com/resources/quick-reads/how-to-update-all-python-packages/)
- [Model Validators](https://docs.djangoproject.com/en/2.2/ref/validators/)
- [Model Relations ](https://medium.com/django-rest/django-model-relations-63709bccb72d)

last stop -> https://youtu.be/pyV2_F9wlk8

## Requirements

**install Docker**

To run this project, you must install Docker.

- [install Docker in Linux](https://docs.docker.com/engine/install/)
- [install Docker in Windows](https://docs.docker.com/desktop/windows/install/)
- [install Docker in Mac](https://docs.docker.com/desktop/mac/install/)

and also install docker-compose.

- [install docker-compose](https://docs.docker.com/compose/install/)

# Useful Links

- [Custom User Model](https://youtu.be/8iiDWPXleIc)
- [Permissions and custom permissions](https://youtu.be/5AOn0BmSXyE)

##### Chat Feature

- [Real Time Chat](https://www.geeksforgeeks.org/realtime-chat-app-using-django/)
- [chat-app-django-channels](https://justdjango.com/blog/chat-app-django-channels)
- [Building a chat application with React and Django Channels](https://blog.logrocket.com/build-chat-application-react-django-channels/)
- [Simple Chat with Django Rest Framework](https://steemit.com/utopian-io/@ajmaln/part-1-creating-a-simple-chat-app-with-djangorestframework)
- [Djnago Channels Documentation](https://channels.readthedocs.io/en/latest/tutorial/part_2.html)

# Other Links

-[Upwork used this to hold funds](https://www.escrow.com/)

# Inspirations

- [Hnadshake College app](https://joinhandshake.com/employers/)
- [Cross Over Jobs](https://www.crossover.com/jobs)
- [Lasie Find a tech job](https://laskie.com/)
- [ Laborx](https://laborx.com/)
- [otta for onboarding](https://app.otta.com/login?_ga=2.103034179.2101910482.1670880381-165328006.1669747092)
- [Waape UG](https://waape.ug/my-feed/1637833148025x862729943357135900)
- [TeraWORK](https://www.terawork.com/)

## Work flow

- [how-to-post-job-on-upwork](https://www.upwork.com/resources/how-to-post-job-on-upwork)
- [how-to-get-started-on-upwork-as-a-freelancer](https://www.upwork.com/resources/how-to-get-started-on-upwork-as-a-freelancer)
- [how-to-create-a-proposal-that-wins-jobs](https://www.upwork.com/resources/how-to-create-a-proposal-that-wins-jobs)
- [Medihub Code](https://github.dev/MediHub-Uganda/medihub_api)
- [Mentorship](https://adplist.org/)
- [tut](https://www.brightermonday.co.ug/)

# More Linkks

- [Social Auth](https://python-social-auth.readthedocs.io/en/latest/configuration/django.html)
- [dockerize](https://semaphoreci.com/community/tutorials/dockerizing-a-python-django-web-application)
- [user Groups](https://simpleisbetterthancomplex.com/tutorial/2018/01/18/how-to-implement-multiple-user-types-with-django.html)
- [model-relationships-django-rest-framework serializers](https://corgibytes.com/blog/2022/06/14/model-relationships-django-rest-framework/)

- [dockerizing-django-with-postgres-gunicorn-and-nginx](https://testdriven.io/blog/dockerizing-django-with-postgres-gunicorn-and-nginx/)
- [Mk docs](https://www.mkdocs.org/getting-started/)
- [medihub](https://github.dev/MediHub-Uganda/medihub_api) -[Best All Auth Solution](https://medium.com/@ksarthak4ever/django-custom-user-model-allauth-for-oauth-20c84888c318)
- [ all auth 100 seconds](https://youtu.be/5guJFS0dsHY)

- [wagtail admin](https://www.revsys.com/tidbits/how-add-django-models-wagtail-admin/)
- [wagtail](https://docs.wagtail.io/en/v2.1.1/getting_started/integrating_into_django.html)
- [swagger docs with drf-yasg](https://github.com/axnsan12/drf-yasg)
- [digital ocean tutorials](https://www.digitalocean.com/community/tutorials/)
- [redis installation](how-to-install-and-secure-redis-on-ubuntu-18-04)
- [Gitinore file](https://www.toptal.com/developers/gitignore/api/django)

## Commands to note

- use this when the database refuses to run migrations
  `py manage.py migrate --run-syncdb`

- to run venv on windows
  `.venv\Scripts\activate.bat`

## Things to consider

- Add Custom comand to populate the database using `management/commands` (_refer to mosh django3 l2 tutorial_)
- Use [MKdocs](https://www.mkdocs.org/getting-started/) or [rst](https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html).
- Storage on azure
  https://youtu.be/1cgMulOqo0w

  gunicorn==20.1.0
  celery==5.2.7

- Look into logging
- caching with redis
- look into permissions
- add pillow for image processing

## azure

django-storages==1.13.2
azure-storage-blob==12.14.1

- settings

```py
STATICFILES_STORAGE = "storages.backends.azure_storage.AzureStorage"
DEFAULT_FILE_STORAGE = "storages.backend.azure_storage.AzureStorage"

AZURE_ACCOUNT_NAME = ENV_STR("AZURE_ACCOUNT_NAME", "")
AZURE_ACCOUNT_KEY = ENV_STR("AZURE_ACCOUNT_KEY", "")
AZURE_CONTAINER = ENV_STR("AZURE_CONTAINER", "")
```

<!-- lesson 21 -->

## TODO

- Other Fields Under job Proporsal
- Templated emails
- Hiring
- Configuring storage with azure
  the royal surprise
- Add DEbug Toolbar
- Consider Dj-database-url
- cONSIDER smtp EMAIL server

# docker and redis

- This will run a docker container having redis and map its port 6379 to out localhost port 6379
- Redis and Celery are both open-source software, but they serve different purposes.

- Redis is an in-memory data structure store, used as a database, cache, and message broker. It supports data structures such as strings, hashes, lists, sets, and sorted sets.

- Celery is a task queue system that allows you to execute tasks asynchronously and in the background. It supports scheduling, retrying failed tasks, and task prioritization. Celery uses a broker, such as Redis, to pass messages between the worker and client applications. In other words, you can use Redis as a message broker for Celery, but Celery is more than just a Redis client

```bash

docker run -d -p 6379:6379 redis

docker ps #list running containers

pipenv install redis
```

start celery

- Using Pipenv

```bash
pipenv run celery -A <project_name> worker -l info
```

- Using celery
  `celery -A <project_name> worker -l info`

- celery beat is used to schedule periodic tasks .

to run beat process

```
celery -A <project_name> beat

```

- To monitor celery tasks use flower

```
pipenv install flower
celery -A <project_name> flower
# access at localhost:5555
```

# testing

```bash
pipenv install pytest
pipenv install --dev pytest-django
pipenv install --dev pytest-watch # For continuous testing
pipenv install --dev model_bakery # works like faker
```

# Performance test ing with locust

# Caching

pipenv install django-redis # For cachin

```bash
access redis cli
`docker exec -it <container_id> <command>`
`docker exec -it <container_id> redis-cli`
```

db 1 is cache
db 2 is

# To change environment

- search DJANGO_SETTINGS_MODULE

# to run with gunicorn

`gunicorn config.wsgi`

3 see all commit
`git log --oneline`

# Linters

- `flake8` combines pip8 and pyflix
- then add black code formatter
- add `isort` which is a python utility for sorting imports
- create a `setup.cfg` file at the root of your project.

```cfg
[flake8]
max-line-length = 180
[flake8]
max-line-length = 119
exclude = .git,*/migrations/*,*env*,*venv*,__pycache__,*/staticfiles/*,*/mediafiles/*

[coverage:run]
source = .
omit=
    *apps.py,
    *settings.py,
    *urls.py,
    *wsgi.py,
    *asgi.py,
    manage.py,
    conftest.py,
    *base.py,
    *development.py,
    *production.py,
    *__init__.py,
    */migrations/*,
    *tests/*,
    */env/*,
    */venv/*,
[coverage:report]
show_missing = True
```

`pip list` -> show you packages
`python manage.py makemigrations users --pythonpath='apps'`
pip uninstall django-richtextfield

https://medium.com/@DawlysD/django-using-azure-blob-storage-to-handle-static-media-assets-from-scratch-90cbbc7d56be

https://medium.com/@DawlysD/deploying-django-apps-with-postgresql-on-azure-app-services-from-scratch-fe4a10db5e7c

https://pypi.org/project/pytest-cov/

# Considerations for documentation

- https://docusaurus.io/showcase
- https://www.gitbook.com/
