docker pull sundowndev/phoneinfoga:latest

<!-- docker run --rm -it sundowndev/phoneinfoga version -->

<!-- scann -->
docker run -it sundowndev/phoneinfoga scan -n 13526006900

<!-- other -->
docker run -it sundowndev/phoneinfoga scan -n "+1 (555) 444-1212"
docker run -it sundowndev/phoneinfoga scan -n "+33 06 79368229"
docker run -it sundowndev/phoneinfoga scan -n "33679368229"


<!-- docker-compose.yml content -->
version: '3.7'

services:
    phoneinfoga:
        container_name: phoneinfoga
        restart: on-failure
        image: sundowndev/phoneinfoga:latest
        command:
            - "serve"
        ports:
            - "80:5000"

<!-- web version -->
docker run --rm -it -p 5000:5000 sundowndev/phoneinfoga serve # same as `phoneinfoga serve`
docker run --rm -it -p 8080:8080 sundowndev/phoneinfoga serve -p 8080 # same as `phoneinfoga serve -p 8080`
