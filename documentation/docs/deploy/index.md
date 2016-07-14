# Deploy Django - Apache2

## Upgrade Virtual Machine

```
sudo apt-get update
sudo apt-get upgrade
```

## Apache2 Installation

```
sudo apt-get install apache2
sudo apt-get install libapache2-mod-wsgi
```

## Installation DB mySql e phpMyAdmin

```
sudo apt-get install mysql-server
sudo apt-get install libmysqlclient-dev
sudo apt-get install phpmyadmin php-mbstring php-gettext
```

## Installation requirements for python, pip and virtualenv

```
apt-get install build-essential
apt-get install python-setuptools
apt-get install python-dev python-pip
pip install virtualenv
pip install MySQL-python
```

## Installation git

```
apt-get install git
```

## Download and setup APP Django

Use GIT to download the app inside folder `/var/www/`, then create a virtualenv. 
After that install inside the virtualenv the requirements (infos are on Readme.md).


## Create VirtualHost

Here a base example of virtualhost:

```
  <VirtualHost *:80>

          ServerName contacts.top-ix.org
          ServerAdmin hackademy@top-ix.org

          WSGIScriptAlias / /var/www/contact-tools/contacttools/wsgi.py

          WSGIDaemonProcess CONTACTS-TOPIX python-path=/var/www/contact-tools:/var/www/envContactTools/lib/python2.7/site-packages

          WSGIProcessGroup CONTACTS-TOPIX

          DocumentRoot /var/www/contact-tools

          Alias /static/ /var/www/contact-tools/static_root/

  <Directory /var/www/contact-tools/>

    Options ExecCGI MultiViews Indexes

    MultiViewsMatch Handlers

    AddHandler wsgi-script .py

    AddHandler wsgi-script .wsgi

    DirectoryIndex index.html index.py app.wsgi

    Order allow,deny

    Require all granted

    Allow from all

  </Directory>
          ErrorLog ${APACHE_LOG_DIR}/contact-tools-error.log
          CustomLog ${APACHE_LOG_DIR}/contact-tools-access.log combined

  </VirtualHost>
```

Now, enable the virtualhost and reload Apache:

```
a2ensite 001-myapp.conf
service apache2 reload
```
