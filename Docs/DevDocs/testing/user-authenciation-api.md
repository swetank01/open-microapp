# user-authenciation-api

## Run user-service:
```
python3 user_service.py
```
## Testing Case:

### Create User
```
curl -X POST -H "Content-Type: application/json" -d '{"username":"newuser","password":"newpassword"}' http://localhost:5000/register
```

### User Login and Get JWT Token:
```
TOKEN=$(curl -X POST -H "Content-Type: application/json" -d '{"username":"newuser","password":"newpassword"}' http://localhost:5000/login | jq -r '.access_token')
```

### Authenticated Request to a Protected Endpoint:
```
curl -X GET -H "Authorization: Bearer $TOKEN" http://localhost:5000/protected
```