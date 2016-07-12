# CCRelations

In this model we are going to save the relations between **Company** and **Contacts**. Since each contacts can belong to more then one Company we've created a pivot Table.

We have only 3 parameters, each one is a `ForeignKey` for the One To Many Relation. We also added to this table the information about the Type of contacts for each relation Contact / Company.


|FIELD NAME | NULLABLE | TYPE | DESCRIPTION|
|:----------- | :-----------: | :-----------: | :-----------|
|company            | False      |  FOREIGN-KEY      | Company ID     |
|contact            | False      |  FOREIGN-KEY      | Contact ID     |
|contact_type       | False      |  FOREIGN-KEY      | ContactType ID |
|creation_date      | False      |  DATETIME         | Creation Date  |

## Code Snippet

Here the code used to Register the Admin Form for table **CCRelation** in the Admin Area:

    class CCRelationAdmin(admin.ModelAdmin):
        list_display = ('company', 'contact', 'contact_type')
