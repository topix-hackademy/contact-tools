# TOP-IX Contact Tools

Django Plugin for contact management @ TOP-IX.

## Installation & Start

Clone the repository:

    $ git clone https://github.com/topix-hackademy/contact-tools
    
Create a virtualenv:

    $ virtualenv envContact
    $ source envContact/bin/activate
    
Move into the root directory and install the requirements:

    $ fab install
    
Create DB:

    $ fab migrate
    
Create SuperUser:

    $ fab create_superuser
    
Run Server:

    $ fab run
    
Run migration for app ```contacts```:

    $ fab migrate_app:'contacts'