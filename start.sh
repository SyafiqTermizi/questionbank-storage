export FLASK_ENV=prod
export FLASK_APP=converter.py 

gunicorn converter:app --bind 0:80