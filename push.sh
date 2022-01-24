python manage.py collectstatic --noinput --clear
sleep 1
python manage.py makemigrations
sleep 1
python manage.py migrate
sleep 1

mv mmysite/settings.py mmysite/localsettings.py
sleep 1
mv mmysite/herokusettings.py mmysite/settings.py
sleep 1
git add .
sleep 1
git commit -m "auto"
sleep 1
git push
sleep 1
git push heroku master
sleep 1
mv mmysite/settings.py mmysite/herokusettings.py
sleep 1
mv mmysite/localsettings.py mmysite/settings.py
sleep 1
heroku run python manage.py migrate
sleep 1
