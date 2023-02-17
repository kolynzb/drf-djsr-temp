# Local installation for development

## Prerequisites

- If you are familiar with Docker, then you just need [Docker](https://docs.docker.com/docker-for-mac/install/). If you don't want to use Docker, then you just need Python3 and Postgres installed.

- _Note_ that the python version used is ![](https://img.shields.io/badge/python-3.11.0-red)

- Clone the repository
  ```shell
  git clone https://github.com/Eatal-dev/Hire-eatal-api.git && cd hire-eatal-api
  ```

## Local Development without Docker

- Run `cp .env.example .env`
- Fill out the missing environment variables in `.env`
- _Refer to the [.env.example](../.env.example) file at the root of the project to learn more about what variables to add to the file_

- Create a virtual environment with your prefered tool(_either conda ,pipenv,venv_)

  - For `pipenv` (_most prefered for this project_)
    - Run the following commands
    ```bash
    pip install pipenv # install pipenv
    pipenv shell # start virtual environment
    pipenv install # install all packages
    ```
  - For `venv`
    - Run the following commands
    ```bash
     pip install virtualenv
     python3 -m venv <name-of-environment> && source <name-of-environment>/bin/activate
    pip install -r requirements.txt
    ```

- Create and Run migrations

```bash
python manage.py migrate
python manage.py makemigrations
python manage.py runserver
```

- Open [localhost:8000](http://localhost:8000) or [127:0:0:1:8000](http://127:0:0:1:8000) to see the API documentation.

- You're now ready to SUFFER! ✨ 💅 🛳

### Create superuser

If you want, you can create initial super-user with next commad:

```bash
./manage.py createsuperuser
```

### Running Tests

- To run all tests with code-coverate report, simple run:

```bash
pytest #run all tests
pytest app/tests #run tests froa single app
pytest app/tests/test_module.py #run tests froa single module
pytest app/tests/test_module.py::TestClass #run tests froa single class
pytest app/tests/test_module.py::TestClass::test_func #run tests froa single function
pytest -k <pattern> # run test with a partern  in their names
ptw #pytest watch for continuous testing
```

- You can even configure the test panel in vscode to help while you run tests.

## Local Development with Docker

- Start the dev server for local development:

```bash
cp .env.dist .env
docker-compose up
```

- Run a command inside the docker container:

```bash
docker-compose run --rm web [command]
```

- For more information on the docker build process, see the included `Dockerfile`.

## Code formatting using black

To format the code automatically using `black`,
just run it in the project directory:

    black .

-
## Vscode setting

- The vscode settings can be found in the .vscode folder
