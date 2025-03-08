Email Sending Platform using Gmail

How to use the app:
1. create a new virtual environment:
```python3-venv -m venv .venv ```
2. activate the environment:
``` source .venv/bin/activate ```
3. clone the repository:
``` git clone https://github.com/naeem-md93/EmailProject.git ```
4. change directory:
``` cd EmailProject ```
5. install requirements:
``` pip install -r requirements.txt ```
6. create the .env file:
``` cp .env.copy .env ```
7. create an app password from gmail (Gmail->Manage Your Google Account->Security->2-Step Verification->App passwords); then place your email address and the app password in the .env file
8. run the app
``` python manage.py runserver ```