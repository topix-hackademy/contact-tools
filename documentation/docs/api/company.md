# Company API 

All the resources for the company model are reachable at this endpoint:

    /api/v1/company/
    
## Collection Resources

| Verb  | Usage | Notes  |
| :---: | :---: |   ---  |
| GET   | Read  |   ---  |
| POST  | Create| Create a new Company |
| PUT   | Create| Create a new Company if does not exists  |
| PUT   | Update| Update the company, all fields|
| DELETE|   X   | Delete is not implemented. To delete a resource use PUT verb and change the field `is_valid` |

## Error Management

In case of content error you will receive a `400 Bad Request` with a message like:

    {
      "company_type": [
        "This field is required."
      ],
      "company_tax_code": [
        "Company with this Tax Code already exists."
      ]
    }

## GET ALL

    GET /api/v1/company/
    
Example of output:

    [
      {
        "id": 1,
        "company_custom_id": 1,
        "company_name": "Custom Company 1",
        "company_short_name": "CustComp1",
        "company_business_name": "Custom Company 1",
        "company_vat_number": 12312312,
        "company_tax_code": null,
        "company_address": "address-info",
        "company_cap": "123",
        "company_city": "turin",
        "company_province": "",
        "company_country": "italy",
        "company_phone_number": "2132133112",
        "company_fax": "",
        "company_website": "",
        "company_notes": "",
        "creation_date": "2016-07-13T09:15:36.633000Z",
        "company_type": [
          {
            "id": 1,
            "type_name": "PEERING",
            "is_valid": true,
            "creation_date": "2016-07-13T09:15:34.009000Z"
          }
        ]
      },
      ...
    ]
    
## GET ONE

    GET /api/v1/company/{id-resource}/
    
Example of output:

    {
      "id": 1,
      "company_custom_id": 1,
      "company_name": "Custom Company 1",
      "company_short_name": "CustComp1",
      "company_business_name": "Custom Company 1",
      "company_vat_number": 12312312,
      "company_tax_code": null,
      "company_address": "address-info",
      "company_cap": "123",
      "company_city": "turin",
      "company_province": "",
      "company_country": "italy",
      "company_phone_number": "2132133112",
      "company_fax": "",
      "company_website": "",
      "company_notes": "",
      "creation_date": "2016-07-13T09:15:36.633000Z",
      "company_type": [
        {
          "id": 1,
          "type_name": "PEERING",
          "is_valid": true,
          "creation_date": "2016-07-13T09:15:34.009000Z"
        }
      ],
      "contacts": {
        "relations": [
          {
            "contact": {
              "contact_email": "user1@email.it",
              "id": 3,
              "contact_username": "user1"
            },
            "role": "administration"
          }
        ]
      }
    }
    
## CREATE

    POST /api/v1/company/

Example of input body:

    {
        "company_custom_id": 110, "company_short_name": "newComp1", "company_name": "newCompany1", 
        "company_business_name": "newCompany1", "company_tax_code": 111000111,
        "company_city": "Turin1", "company_province": "Turin1", 
        "company_country": "Italy1",  "company_address": "via delle vie1", 
        "company_cap": "121231",
        "company_phone_number": "1231231311", "company_fax": "1231231231",  
        "company_website": "example.com1", "company_notes": "just a simple note1", 
        "company_type":[{"type_name":"PEERING", "id":1}]
    }
    
Example of output:

    {
      "id": 11,
      "company_custom_id": 110,
      "company_name": "newCompany1",
      "company_short_name": "newComp1",
      "company_business_name": "newCompany1",
      "company_vat_number": null,
      "company_tax_code": 111000111,
      "company_address": "via delle vie1",
      "company_cap": "121231",
      "company_city": "Turin1",
      "company_province": "Turin1",
      "company_country": "Italy1",
      "company_phone_number": "1231231311",
      "company_fax": "1231231231",
      "company_website": "example.com1",
      "company_notes": "just a simple note1",
      "creation_date": "2016-07-18T12:54:33.389902",
      "company_type": [
        {
          "id": 1,
          "type_name": "PEERING",
          "is_valid": true,
          "creation_date": "2016-07-13T09:15:34.009000Z"
        }
      ],
      "contacts": {
        "relations": []
      }
    }
    
## UPDATE

    PUT /api/v1/company/{id-resource}/

Example of input body:

    {
        "company_custom_id": 110, "company_short_name": "NEW-NAME", "company_name": "newCompany1", 
        "company_business_name": "newCompany1", "company_tax_code": 111000111,
        "company_city": "Turin1", "company_province": "Turin1", 
        "company_country": "Italy1",  "company_address": "via delle vie1", 
        "company_cap": "121231",
        "company_phone_number": "1231231311", "company_fax": "1231231231",  
        "company_website": "example.com1", "company_notes": "just a simple note1", 
        "company_type":[{"type_name":"PEERING", "id":1}]
    }

Example of output:

    {
      "id": 11,
      "company_custom_id": 110,
      "company_name": "newCompany1",
      "company_short_name": "NEW-NAME",
      "company_business_name": "newCompany1",
      "company_vat_number": null,
      "company_tax_code": 111000111,
      "company_address": "via delle vie1",
      "company_cap": "121231",
      "company_city": "Turin1",
      "company_province": "Turin1",
      "company_country": "Italy1",
      "company_phone_number": "1231231311",
      "company_fax": "1231231231",
      "company_website": "example.com1",
      "company_notes": "just a simple note1",
      "creation_date": "2016-07-18T12:54:33.389902",
      "company_type": [
        {
          "id": 1,
          "type_name": "PEERING",
          "is_valid": true,
          "creation_date": "2016-07-13T09:15:34.009000Z"
        }
      ],
      "contacts": {
        "relations": []
      }
    }


## GET ONE BY TAX or VAT code

    GET /api/v1/company-by-code/{code}/

Example of output:

        {
      "id": "1",
      "company_custom_id": "1",
      "company_name": "Custom Company 1",
      "company_short_name": "Custom Company 1",
      "company_business_name": "Custom Company 1",
      "company_vat_number": "12312312",
      "company_tax_code": null,
      "company_address": "via vai 1",
      "company_cap": "123",
      "company_city": "turin",
      "company_province": "",
      "company_country": "italy",
      "company_phone_number": "2132133112",
      "company_fax": "",
      "company_website": "",
      "company_notes": "",
      "creation_date": "2016-07-13T09:15:36.633000Z",
      "company_type": [
        {
          "id": "1",
          "type_name": "IX",
          "is_valid": true,
          "creation_date": "2016-07-13T09:15:34.009000Z"
        }
      ],
      "contacts": {
        "relations": [
          {
            "contact": {
              "contact_email": "alex@alex.it",
              "id": "3",
              "contact_username": "alex"
            },
            "role": "administration"
          }
        ]
      }
    }


## GET with freesearch

performs a case insensitive search of all comanies that include the specified string in:
- company_name
- company_short_name
- company_business_name
- company_website
- company_notes



    GET /api/v1/company-freesearch/{searchstring}
    
Example of output:

    [
      {
        "id": 1,
        "company_custom_id": 1,
        "company_name": "Custom Company 1",
        "company_short_name": "CustComp1",
        "company_business_name": "Custom Company 1",
        "company_vat_number": 12312312,
        "company_tax_code": null,
        "company_address": "address-info",
        "company_cap": "123",
        "company_city": "turin",
        "company_province": "",
        "company_country": "italy",
        "company_phone_number": "2132133112",
        "company_fax": "",
        "company_website": "",
        "company_notes": "",
        "creation_date": "2016-07-13T09:15:36.633000Z",
        "company_type": [
          {
            "id": 1,
            "type_name": "PEERING",
            "is_valid": true,
            "creation_date": "2016-07-13T09:15:34.009000Z"
          }
        ]
      },
      ...
    ]
    
