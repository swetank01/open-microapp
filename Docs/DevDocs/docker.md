# Docker 

## Build

### backend
docker build -t user-service -f ./docker/user.backend.Dockerfile .
docker build -t task-service -f ./docker/task.backend.Dockerfile .

### frontend 
docker build -t frontend-service -f ./docker/frontend.Dockerfile .

## Run 
docker run -p 5000:5000 user-service
docker run -p 5001:5001 task-service

docker run -p 3000:3000 frontend-service

## Test 

http://localhost:5000/users
http://localhost:5001/tasks

http://localhost:3000/