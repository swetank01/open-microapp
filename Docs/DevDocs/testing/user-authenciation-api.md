# user-authenciation-api

## Run user-service:
```
python3 user_service.py
```
## Testing Case:

### Create User
```
curl -X POST -H "Content-Type: application/json" -d '{"username": "testuser", "password": "testpassword"}' http://localhost:5000/register
```
###### output: 
```
{"message":"User registered successfully"}
```

### User Login and Get JWT Token:
```
curl -X POST -H "Content-Type: application/json" -d '{"username": "testuser", "password": "testpassword"}' http://localhost:5000/login
```
###### output: 
```
{"access_token":"your_access_token"}
```
##### this will print out access_token for you that you can put into env variable:

```
export YOUR_ACCESS_TOKEN='your-access_token'
```

### Authenticated Request to a Protected Endpoint:
```
curl -X GET -H "Authorization: Bearer $YOUR_ACCESS_TOKEN" http://localhost:5000/protected
```

###### output: 
```
{"logged_in_as":3}
```