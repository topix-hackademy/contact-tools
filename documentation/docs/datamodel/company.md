# Company

In this model we are going to save all the list of companies. 

Using the key **company_type** we have created a *Many To Many Relation* between tables Company and CompanyType.
For each Company we save this list of attributes:

|FIELD NAME | NULLABLE | TYPE | DESCRIPTION|
|:----------- | :-----------: | :-----------: | :-----------|
|company_custom_id       | True      |  INT           | Custom ID on external systems (eg. ESolver)|
|company_name            | False      |  CHAR          | Name of the Company|
|company_short_name      | True      |  CHAR          | Short Name of the Company|
|company_business_name   | True      |  CHAR          | Unique Name of the Company|
|company_vat_number      | True       |  INT           | VAT Number (eg. partita IVA)|
|company_tax_code        | True       |  INT           | TAX Code (eg. codice fiscale)|
|company_address         | True      |  CHAR          | Address of the Company|
|company_cap             | True      |  CHAR          | CAP Address of the Company|
|company_city            | True      |  CHAR          | City of the Company|
|company_province        | True       |  CHAR          | Province of the Company|
|company_country         | True      |  CHAR          | Country of the Company|
|company_phone_number    | True       |  CHAR          | Phone Number of the Company|
|company_fax             | True       |  CHAR          | Fax of the Company|
|company_website         | True       |  CHAR          | WebSite of the Company|
|company_notes           | True       |  TEXT          | Notes about the Company|
|creation_date           | False      |  DATETIME      | Creation Date of the Record|
|company_type            | False       |  CHAR          | Type (ManyToMany  with CompanyType)|
|company_logo            | False       |  ImageField          | logo image of the company |
|company_logo_thumbnail  | False       |  ImageSpecField      | dynamic property, does not go into the DB |

## Code Snippet 

Here the code used to Register the Admin Form for table **Company** in the Admin Area:

    class CompanyAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Company Info', 
            {'fields': ['company_custom_id', 'company_name', 'company_short_name',
            'company_business_name', 'thumb_logo_display', 'company_logo', 'company_vat_number', 'company_tax_code']}),
        ('Company Address', {'fields': ['company_address', 'company_cap', 'company_city', 'company_province',
                                        'company_country']}),
        ('Company Contacs', {'fields': ['company_phone_number', 'company_fax', 'company_website']}),
        ('Company Type', {'fields': ['company_type']}),
        ('Notes', {'fields': ['company_notes']})
    ]
    list_display = ('company_name', 'thumb_logo_display', 'company_short_name', 'company_custom_id', 'company_vat_number', 'company_tax_code')
    search_fields = ['company_name', 'company_short_name', 'company_vat_number', 'company_tax_code']
    readonly_fields = ['thumb_logo_display']
    thumb_logo_display = AdminThumbnail(image_field='get_logo_or_default', template='admin/thumbnail.html')
    thumb_logo_display.short_description = "Company logo"
    

# Company Type

This model is used to specify the type of each Company (Peering / Clients / ...).
Here the attributes:

|FIELD NAME | NULLABLE | TYPE | DESCRIPTION|
|:----------- | :-----------: | :-----------: | :-----------|
|type_name              | False     |  CHAR       | Name of the type|
|is_valid               | False     |  BOOLEAN    | TRUE if the type is available|
|creation_date          | False     |  DATETIME   | Creation Date|

## Code Snippet

Here the code used to Register the Admin Form for table **CompanyType** in the Admin Area:

    class CompanyTypeAdmin(admin.ModelAdmin):

        fieldsets = [
            ('Company Type', {'fields': ['type_name', 'is_valid']}),
        ]
        list_display = ('type_name', 'is_valid', 'creation_date')
        list_filter = ['creation_date', 'is_valid']
        search_fields = ['type_name']

