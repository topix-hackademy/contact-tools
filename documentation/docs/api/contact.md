# Contact API 

All the resources for the contact model are reachable at this endpoint:

    /api/v1/contact/
    
## Collection Resources

| Verb  | Usage | Notes  |
| :---: | :---: |   ---  |
| GET   | Read  |   ---  |
| POST  | Create| Create a new Contact |
| PUT   | Update| Update the Contact, all fields|
| DELETE|   X   | Delete is not implemented. To delete a resource use PUT verb and change the field `is_valid` |

## Error Management

In case of content error you will receive a `400 Bad Request` with a message like:

    {
      "contact_username": [
        "This field is required."
      ]
    }

## GET ALL

    GET /api/v1/contact/
    
Example of output:

    [
      {
        "id": 1,
        "contact_username": "alex",
        "contact_first_name": "alex",
        "contact_last_name": "alex",
        "contact_email": "alex@alex.it",
        "contact_email_secondary": "asd@asd.com",
        "contact_phone": "312312312",
        "contact_phone_secondary": "",
        "contact_notes": ""
      },
      ...
    ]
    
## GET ONE

    GET /api/v1/contact/{id-resource}/
    
Example of output:

    {
      "id": 1,
      "contact_username": "alex",
      "contact_first_name": "alex",
      "contact_last_name": "alex",
      "contact_email": "alex@alex.it",
      "contact_email_secondary": "asd@asd.com",
      "contact_phone": "312312312",
      "contact_phone_secondary": "",
      "contact_notes": "",
      "role": {
        "relations": [
          {
            "company": {
              "id": 1,
              "company_name": "Custom Company 1"
            },
            "role": "administration"
          }
        ]
      }
    }
    
## CREATE

    POST /api/v1/contact/

Example of input body:

    {
      "contact_username": "newuser",
      "contact_first_name": "alex",
      "contact_last_name": "alex",
      "contact_email": "new@user.it",
      "contact_email": "secondary@email.com",
      "contact_phone": "312312312",
      "contact_phone_secondary": "111111",
      "contact_notes": "",
      "role": {
        "relations": [
          {
            "company": {
              "id": 2,
              "company_name": "Custom Company 2"
            },
            "role": "administration"
          }
        ]
      }
    }
    
Example of output:

    {
      "id": 5,
      "contact_username": "newuser",
      "contact_first_name": "alex",
      "contact_last_name": "alex",
      "contact_email": "secondary@email.com",
      "contact_phone": "312312312",
      "contact_phone_secondary": "111111",
      "contact_notes": "",
      "role": {
        "relations": [
          {
            "company": {
              "id": 2,
              "company_name": "Custom Company 2"
            },
            "role": "administration"
          }
        ]
      }
    }
    
## UPDATE

    PUT /api/v1/contact/{id-resource}/

Example of input body:

    {
      "contact_username": "newuser",
      "contact_first_name": "alexXXXXX",
      "contact_last_name": "alex",
      "contact_email": "secondary@email.com",
      "contact_phone": "312312312",
      "contact_phone_secondary": "111111",
      "contact_notes": "",
      "role": {
        "relations": [
          {
            "company": {
              "id": 2,
              "company_name": "Custom Company 2"
            },
            "role": "administration"
          }
        ]
      }

Example of output:

    {
      "id": 5,
      "contact_username": "newuser",
      "contact_first_name": "alexXXXXX",
      "contact_last_name": "alex",
      "contact_email": "secondary@email.com",
      "contact_phone": "312312312",
      "contact_phone_secondary": "111111",
      "contact_notes": "",
      "role": {
        "relations": [
          {
            "company": {
              "id": 2,
              "company_name": "Custom Company 2"
            },
            "role": "administration"
          }
        ]
      }
    }
    
## GET BY EMAIL

    GET /api/v1/contact-by-email/{email-resource}/
    
Example of output:

    [
      {
        "id": 1,
        "contact_username": "pippoPLuto",
        "contact_first_name": "qweqwe\\",
        "contact_last_name": "asfcvzxcvv",
        "contact_email": "alex.comunian@top-ix.org",
        "contact_email_secondary": "alex.comunian@top-ix.org",
        "contact_phone": "0118390191",
        "contact_phone_secondary": "0118390191",
        "contact_notes": "",
        "role": {
          "relations": []
        }
      },
      {
        "id": 2,
        "contact_username": "ciccio pasticcio",
        "contact_first_name": "asd",
        "contact_last_name": "asd",
        "contact_email": "alex.comunian@top-ix.org",
        "contact_email_secondary": "alex.comunian@top-ix.org",
        "contact_phone": "0118390191",
        "contact_phone_secondary": "0118390191",
        "contact_notes": "",
        "role": {
          "relations": []
        }
      }
    ]
    
	
	
	
## GET BY Centralservices ID

returns an array of contacts (max one in normal conditions)

    GET /api/v1/contact-by-csid/{old_cs_id}/
