# Contact

In this model we are going to save all the list of contacs. 

For each Contact we save this list of attributes:

|FIELD NAME | NULLABLE | TYPE | DESCRIPTION|
|:----------- | :-----------: | :-----------: | :-----------|
|contact_username       | False     |  CHAR   | Username of the Contacts|
|contact_first_name     | True      |  CHAR   | First Name of the Contacts|
|contact_last_name      | True      |  CHAR   | Last Name of the Contacts|
|contact_email          | False     |  EMAIL  | Email of the Contacts|
|contact_email_secondary | True     |  EMAIL  | Secondary Email of the Contacts|
|contact_phone          | True      |  CHAR   | Phone Number of the Contacts|
|contact_phone_secondary | True      |  CHAR   | Secondary Phone Number of the Contacts|
|contact_notes          | True      |  TEXT   | Notes about of the Contacts|
|creation_date          | False     |  DATETIME   | Creation Date|

## Code Snippet 

Here the code used to Register the Admin Form for table **Contact** in the Admin Area:

    class ContactAdmin(admin.ModelAdmin):
        fieldsets = [
            ('Contact Info', {'fields': ['contact_username', 'contact_first_name', 'contact_last_name']}),
            ('Contact Address', {'fields': ['contact_email', 'contact_email_secondary', 'contact_phone', 'contact_phone_secondary']}),
            ('Notes', {'fields': ['contact_notes']})
        ]
        list_display = ('contact_username', 'contact_email', 'contact_first_name', 'contact_last_name')
        search_fields = ['contact_username', 'contact_email', 'contact_last_name']



# Contact Type

This model is used to specify the type of each Contact (Technical / Manager / Consultant / ...). 
Here the attributes:

|FIELD NAME | NULLABLE | TYPE | DESCRIPTION|
|:----------- | :-----------: | :-----------: | :-----------|
|type_name              | False     |  CHAR       | Name of the type|
|is_valid               | False     |  BOOLEAN    | TRUE if the type is available|
|creation_date          | False     |  DATETIME   | Creation Date|

## Code Snippet

Here the code used to Register the Admin Form for table **ContactType** in the Admin Area:

    class ContactTypeAdmin(admin.ModelAdmin):

        fieldsets = [
            ('Contact Type', {'fields': ['type_name', 'is_valid']}),
        ]
        list_display = ('type_name', 'is_valid', 'creation_date')
        list_filter = ['creation_date', 'is_valid']
        search_fields = ['type_name']

