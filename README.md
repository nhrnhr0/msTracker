# How to setup
```bash
git clone https://github.com/nhrnhr0/msTracker.git
cd msTracker
python -m venv env
source env/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
    <follow instructions>
```

# How to run
```bash
python manage.py runserver 0.0.0.0:5252
```

this server has 2 endpoints `/loc`, and `/admin`.

you can login to the admin using the created superuser.

you can POST your location to `/loc`
example settings to put in owntrack: http://52.14.213.58:5252/loc



# setup owntrack secret
edit the file `msTrack/server/config.py` to somthing like: 
```python
LOCATION_ENCRYPTION_KEY = '<YOUR SECRET>'
```