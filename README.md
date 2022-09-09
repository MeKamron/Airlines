### ZipAirlines

## Local development setup

0. have ubuntu 22.04 LTS
1. use python 3.9, pip 21+
2. clone the repo into `airlines` directory
3. crete virtual environment in the root directory of the project where `core` dir lies (python3 -m venv venv)
4. activate the venv
5. install requirements (`pip3 install -r requirements.txt`)
6. initial db (`python3 manage.py migrate`)
7. run the project (`python3 manage.py runserver`)
