<h1 align="center"> Python Pizza Planet </h1>

![python-badge](https://img.shields.io/badge/python-%2314354C.svg?style=for-the-badge&logo=python&logoColor=white)

This is an example software for a pizzeria that takes customizable orders.

## Table of Contents

- [Getting started](#getting-started)
- [Running the backend project](#running-the-backend-project)
- [Running the frontend](#running-the-frontend)
- [Testing the backend](#testing-the-backend)

## Getting started

You will need the following general tools:

- A Python interpreter installed. [3.8.x](https://www.python.org/downloads/release/python-3810/) is preffered.

- A text editor: preferably [Visual Studio Code](https://code.visualstudio.com/download)

- Extensions such as [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python) and [Live Server](https://marketplace.visualstudio.com/items?itemName=ritwickdey.LiveServer)

## Running the backend project

- Clone the repo

```bash
git clone https://github.com/ioet/python-pizza-planet.git
```

- Create a virtual environment in the root folder of the project

```bash
python3 -m venv venv
```

- Activate the virtual environment (In vscode if you select the virtual env for your project it will activate once you open a new console window)

_For linux/MacOS users:_

```bash
source venv/bin/activate 
```

_For windows users:_

```cmd
\path\to\env\Scripts\activate
```

- Install all necessary dependencies:

```bash
pip3 install -r requirements.txt
```

- Start the database (Only needed for the first run):

```bash
python3 manage.py db init
python3 manage.py db migrate
python3 manage.py db upgrade
```

Or just:

```
make init-db
```

Once your database is initialized you can populate it with data by using the following command:

```
make populate-db
```

- If you want to use the hot reload feature set FLASK_ENV before running the project:

_For linux/MacOS users:_

```bash
export FLASK_ENV=development 
```

_For windows users:_

```CMD
set FLASK_ENV=development
```

- Run the project with:

```bash
python3 manage.py run
```

## Running the frontend

- Clone git UI submodule

```bash
git submodule update --init
```

Or

```bash
make submodule
```

- Install Live Server extension if you don't have it from [here](https://marketplace.visualstudio.com/items?itemName=ritwickdey.LiveServer) on VSCode Quick Open (`Ctrl + P`)

```bash
ext install ritwickdey.LiveServer
```

- To run the frontend, start `ui/index.html` file with Live Server (Right click `Open with Live Server`)

- **Important Note** You have to open vscode in the root folder of the project.

- **To avoid CORS errors** start the backend before the frontend, some browsers have CORS issues otherwise

### Testing the backend

- Make sure that you have `pytest` installed

- Run the test command

```bash
python3 manage.py test
```

Or just:

```
make test
```

### Docker

#### Build docker image
You can build a docker image for both `backend` and `frontend` by running the following commands:

##### Backend:
Wodking directory ```./``` (project root)
```bash
make build
```

##### Frontend:
Wodking directory ```ui/``` (project submodule)
```bash
make build
```

#### Docker compose
You can run both services in separate container with the following command:

```bash
docker compose up
```

> Important note: you need to provide a `.env` file with the ports you want both of the services to run on.

> You need to initialize the submodule before runninng the command

This will build both images if they don't already exist and run them in separate containers.



The `.env` file should have the following variables:
```
BACKEND_PORT=5000
FRONTEND_PORT=8080
```
