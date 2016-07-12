# TOP-IX Contact Tools

Django Plugin for contact management @ TOP-IX.

## Installation & Start

Clone the repository:

    $ git clone https://github.com/topix-hackademy/contact-tools
    
Create a virtualenv:

    $ virtualenv envContact
    $ source envContact/bin/activate
    
Move into the root directory and install the requirements:

    $ pip install fabric
    $ fab install
    
Create DB:

    $ fab migrate
    
Create SuperUser:

    $ fab create_superuser

Run migration for app ```contacts```:

    $ fab migrate_contacts
    $ fab migrate

Run migration for all:

    $ fab migrate_all
    
Run Server:

    $ fab start
    
## Contacts APP

App ```contacts``` contains all the controllers, models and urls to manage customers. The views are registered on:

    http://127.0.0.1:8000/api/

## Documentation

We provided a full documentation on Data Model and API. We are using MKDocs, here some utils.

To run the local documentation from the root of the project:

    fab start_doc
    
To deploy documentation under gh-pages on github:

    fab deploy_doc

[HERE](https://topix-hackademy.github.io/contact-tools/) you can find the result!