# CONTACT-TOOLS API DOCUMENTATION

## Resources

Through APIs we perform access to Contact and Company data models. Check this two links for the details:

* [Company](/api/company)

* [Contact](/api/contact)

## Version 

APIs are reachable from a standard endpoint for version-1:

    /api/v1/{resource-name}

## Authorization

All the APIs are authenticated. To have access you need to specify a `service-token` from the data model `Service` in your request header. Here an example:

    wget http://example.com/api/v1/company/1 
            --header="AUTH-TOKEN: YOUR-SERVICE-TOKEN" 
            --header="CONTENT-TYPE: application/json" 

Without the `service-token` you will receive a **403 Forbidden** with message:

    {
      "message": "Permission denied"
    }
    
