# django-blog-app
Blog website for to practice django

#create virtual env
virtualenv fenv

#activate virtual env
source fenv/bin/activate

#install django
pip install django

#check django
python -m django --version

#start django project
django-admin startproject django_project

#start app
python manage.py startapp blog

#add blog app in to installed apps in settings file
'blog.apps.BlogConfig'