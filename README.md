# Simple User Crud
Simple user CRUD with token auth, pagination and permissions 
## Usage
Run in docker:

`docker-compose up --build`

or:

Activate your virtualenv and run:

`pip install -r requirements.txt`

`./manage.py migrate`

`./manage.py runserver`

App available on localhost:8000

## Swagger 
/swagger/ (some endpoint info ain't correct)

## API
### Users List
#### GET
`curl -X GET "http://127.0.0.1:8000/api/users/" -H  "accept: application/json"`

#### Response
```
  "count": 1,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": 1,
      "username": "testuser",
      "first_name": "",
      "last_name": "",
      "is_active": true,
      "last_login": "2021-10-04T04:33:45.940014Z",
      "is_superuser": false
    }
  ]
}
```

#### POST
`curl -X POST "http://127.0.0.1:8000/api/users/" -H  "accept: application/json" -H  "Content-Type: application/json" -d "{  \"username\": \"string\", \"is_active\": true,  \"password\": \"string\"}"`

#### Response
```
{
  "id": 3,
  "username": "string",
  "first_name": "",
  "last_name": "",
  "is_active": true,
  "last_login": null,
  "is_superuser": false
}
```
### Users Detail
#### GET
`curl -X GET "http://127.0.0.1:8000/api/users/1/" -H  "accept: application/json"`

#### Response
```
{
  "id": 1,
  "username": "testuser",
  "first_name": "",
  "last_name": "",
  "is_active": true,
  "last_login": "2021-10-04T04:33:45.940014Z",
  "is_superuser": false
}
```
### Permissions
All can list, retrieve and create objects.
Only owners and staff can update and partial update.
Only staff users can destroy (delete) objects
(users should set is_active to false).

### Toke Auth
`curl -X POST "http://127.0.0.1:8000/api-token-auth/" -H  "accept: application/json" -H  "Content-Type: application/json" -d "{  \"username\": \"string\",  \"password\": \"string\"}"`

#### Response
```
{
  "token": "9dd917c291b9132bd899291fb13c46a1f7f2f2bb"
}
```