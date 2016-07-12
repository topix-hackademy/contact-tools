from __future__ import with_statement
from fabric.api import *

server_test = ['root@194.116.76.56']

####################################
########### REMOTE UTILS ###########
####################################

# Deploy sprint-x
@hosts(server_test)
def deploy_sprint(sprint_number):
    with cd('/var/www/contact-tools'):
        run('git checkout sprint-%s' % sprint_number)
        run('git pull')
        run('service apache2 reload')

@hosts(server_test)
def view_test_log():
    run('tail -f /var/log/apache2/contact-tools-error.log')


####################################
########### DJANGO UTILS ###########
####################################

def install():
    local('pip install -r requirements.txt')


def req_pop():
    local('pip freeze > requirements.txt')


def migrate():
    local('python manage.py migrate')

def migrate_contacts():
    local('python manage.py makemigrations contacts')

#fab migrate_app:'APP-NAME'
def migrate_app(app_name):
    local('python manage.py makemigrations %s' % app_name)

def migrate_all():
    local('python manage.py makemigrations contacts')
    local('python manage.py migrate')

def create_superuser():
    local('python manage.py createsuperuser')

def start():
    local('python manage.py runserver 0.0.0.0:8000')


####################################
########## DOCUMENTATION ###########
####################################

def start_doc():
    local('mkdocs serve -f documentation/mkdocs.yml')

def deploy_doc():
    local('mkdocs gh-deploy --clean -f documentation/mkdocs.yml')