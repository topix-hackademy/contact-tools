# Service

We declared a model **Service** to save and create tokens for give access to the API Service.

For each Service we have this parameters:

|FIELD NAME | NULLABLE | TYPE | DESCRIPTION|
|:----------- | :-----------: | :-----------: | :-----------|
|service_name       | False      |  CHAR          | Service Name|
|token_name         | False      |  CHAR          | Token Used to have access|
|is_valid           | False      |  BOOL          | Boolean Value|
|creation_date      | False      |  DATETIME      | Creation Date|
|activation_date    | True       |  DATETIME      | Activation Date of the service|
|delete_date        | True       |  DATETIME      | Dismission Date of the service|
|notes              | False      |  TEXT          | Address of the Company|

## Code Snippet

Here the code used to Register the Admin Form for table **Service** in the Admin Area:

    fieldsets = [
            ('Service Info', {'fields': ['service_name', 'is_valid']}),
            ('Token Management', {'fields': ['token']}),
            ('Notes', {'fields': ['notes']})
        ]
        list_display = ('service_name', 'token','is_valid', 'creation_date', 'activation_date', 'delete_date')
        list_filter = ['creation_date', 'is_valid']
        search_fields = ['service_name']


        def save_model(self, request, obj, form, change):
            if change:
                old_obj = Service.objects.get(id=obj.id)
                if old_obj.is_valid and not obj.is_valid:
                    # set service not valid
                    obj.delete_date = datetime.datetime.now()
                    obj.token = "INVALID"
                elif not old_obj.is_valid and obj.is_valid:
                    # set service valid
                    obj.delete_date = None
                    obj.activation_date = datetime.datetime.now()
            obj.save()

We are overriding the method `save_model` to set / unset the fields `activation_date` and `delete_date` when the value **is_valid** is set / unset.