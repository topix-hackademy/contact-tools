# TOP-IX Contact Tools

Django Plugin for contact management @ TOP-IX.

## Installation & Start

Clone the repository:

    git clone https://github.com/topix-hackademy/contact-tools
    
Create a virtualenv:

    virtualenv envContact
    source envContact/bin/activate
    
Move into the root directory and install the requirements:

    pip install fabric
    fab install
    fab create_setting
    
Create DB:

    fab migrate
    
Create SuperUser:

    fab create_superuser

Run migration for app ```contacts```:

    fab migrate_contacts
    fab migrate

Run migration for all:

    fab migrate_all

Run seeder for initial test database:

    fab load_db
    
Use the following credentials for the admin login:

    user:   admin
    pws:    ciao1234

Run Server:

    fab start
    
## Contacts APP

App ```contacts``` contains all the controllers, models and urls to manage customers. The views are registered on:

    http://127.0.0.1:8000/api/

## Logging

There is a custom logger configured called "ct-logger" 

    # import the logging library
    import logging
    
    # Get an instance of a logger
    logger = logging.getLogger("ct-logger")
    
    # Log an message
    logger.error("Hello Friend")

## Deploy with Apache

Be sure to create the setting file for the production env (you can use ```fab create_setting```) and create a virtualenv on your remote machine. 

You need to override the voice ```STATICFILES_DIR``` in this way:

    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, "static")
    ]

After that, you need to install your static folder:

    fab install_static

Here your apache configuration:

    <VirtualHost *:80>
    
            ServerName www.contacts.org
            ServerAdmin admin@contacts.org
    
            WSGIScriptAlias / /var/www/contact-tools/contacttools/wsgi.py
    
            WSGIDaemonProcess CONTACTS python-path=/var/www/contact-tools:/PATH/TO/ENV/lib/python2.7/site-packages
    
            WSGIProcessGroup CONTACTS
    
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
    
Well done! :)

_PS: For more information checkout the real documentation._

## Documentation

We provided a full documentation on Data Model and API. We are using MKDocs, here some utils.

To run the local documentation from the root of the project:

    fab start_doc
    
To deploy documentation under gh-pages on github:

    fab deploy_doc

[HERE](https://topix-hackademy.github.io/contact-tools/) you can find the result!