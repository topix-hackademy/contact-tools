# Company Type API

All the resources for the contact model are reachable at this endpoint:

    /api/v1/company-type/

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

    GET /api/v1/company-type/

Example of output:

    [
        {
            "id": "2",
            "type_name": "DP",
            "is_valid": true,
            "creation_date": "2016-07-13T09:16:11.643000Z"
        },
          ...
    ]

## GET ONE

    GET /api/v1/company-type/{id-resource}/

Example of output:

    {
      "id": "2",
      "type_name": "DP",
      "is_valid": true,
      "creation_date": "2016-07-13T09:16:11.643000Z"
    }

## CREATE

    POST /api/v1/company-type/

Example of input body:

    {
      "type_name": "DP",
      "is_valid": true
    }

Example of output:

    {
      "id": "5",
      "type_name": "DP",
      "is_valid": true,
      "creation_date": "2016-07-19T10:26:09.769124"
    }

## UPDATE

    PUT /api/v1/company-type/{id-resource}/

Example of input body:

    {
      "type_name": "DP",
      "is_valid": false
      }

Example of output:

    {
      "id": "5",
      "type_name": "DP",
      "is_valid": false,
      "creation_date": "2016-07-19T10:26:09.769124Z"
    }