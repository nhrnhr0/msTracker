
git pull
source ./env/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py collectstatic --noinput
sudo supervisorctl restart gunicornMsTracker
sudo service nginx restart
