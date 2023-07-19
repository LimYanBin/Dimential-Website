Install Virtual environment

1. python -m venv env
2. cd env
3. Scripts\activate
4. pip install django
5. Git clone all project to here

Services and package needed

1. pip install django-allauth
2. pip install social-auth-app-django
3. pip install redis
4. pip install celery django-celery-beat
5. pip install ngrok
6. pip install Pillow

Start server
1. manage.py runserver
2. ngrok http 8000

How to use redis
1. github.redis.release
2. Install link.msi
3. Set the port to 6379
4. Open User\Users\ProgramFile
5. Find redis
6. Click on redis.cli

Schedule Email
1. celery -A assignment worker -P solo -l info
2. celery -A assignment beat -l info

Github command
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/LimYanBin/IWD.git
git push -u origin main

Github Update
1. git status


