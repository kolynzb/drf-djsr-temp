# drf-djsr-temp

![14Um](https://user-images.githubusercontent.com/45392987/219878753-db6aa205-4c12-4940-bf64-2f0cf811118d.gif)

- This is a template for django API authentication with djoser

- **⚠️ Still a Under Contruction**

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

- Application Programming interface for a auth built in [django](https://docs.djangoproject.com/) and [djangorestframework](https://www.django-rest-framework.org/) with [python](https://www.python.org/).

![](https://img.shields.io/badge/python-3.11.0-red)

## Highlights

- [x] Modern Python development with Python 3.11+
- [x] Bleeding edge Django 4.0+
- [ ] Fully dockerized, local development via docker-compose.
- [x] PostgreSQL
- [ ] Full test coverage, continuous integration, and continuous deployment.
- [ ] Celery tasks

## Features built-in

- [x] Email and Password Authetication with Djoser.
- [x] Custom User
- [x] Code Formating with [Black](https://black.readthedocs.io/en/stable/),`Flake8` & `isort`
- [ ] Social (FB + G+) signup/sigin
- [x] Custom API Home Page
- [ ] Custom Email Templates
- [ ] Tests (with mocking and factories) with code-coverage support
- [x] Swagger API docs out-of-the-box
- [x] Password reset endpoints

## Table Of Contents

- [Project Folder Structure](#folder-structure)
- [Django Apps](#django-apps)
- [How to Run API Locally](./docs/installation.md)

## Folder Structure

```
C:.
├───conf
├───docs
├───accounts
├── apps
│   ├──
│   └── core
└── README.md
```

## Django Apps

- [**Config**](.conf/)
  - App containing django project settings and rject configurations.
- [**Accounts**](./accounts)
  - App to control `User` Accounts , models and Profiles.
- [**Core**](./apps/core/)
  - App for core logic .
  <!-- - [**Profiles**](./profiles/)
  - App for core logic in relation to freelancer and client profiles. -->

## How to Run Project

- [👉🏿Click Me👈🏿](./docs/installation.md) to get project installation instrutions.

## Python Version

- `python 3.11.0`
- Check `runtime.txt` file

## Important Urls

1. Visit the browsable API at [http://localhost:8000/api/v1/](http://localhost:8000/api/v1/)

2. Access the Django admin at [http://localhost:8000/admin](http://localhost:8000/admin/)

3. Visit reDoc documentation [http://localhost:8000/redoc](http://localhost:8000/redoc)

4. Visit Swagger documentation [http://localhost:8000/doc](http://localhost:8000/doc)

5. Visit API Home Page [http://localhost:8000](http://localhost:8000)

6. To access useful links and tutorial that helped during the project [click me 😉](./tut.md)

## Concept Diagrams

- [Link to ERD Diagram]()

<!-- &copy;Kolynzb -->
