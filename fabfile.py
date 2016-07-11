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
########### LOCAL UTILS ############
####################################

def install():
    local('pip install -r requirements.txt')


def migrate():
    local('python manage.py migrate')

#fab migrate_app:'APP-NAME'
def migrate_app(app_name):
    local('python manage.py makemigrations %s' % app_name)

def create_superuser():
    local('python manage.py createsuperuser')


def run():
    local('python manage.py runserver 0.0.0.0:8000')
