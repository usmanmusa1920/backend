# Steps of dockerizing static site using apache locally

To build docker images, we use two ports numbers as follows:

-   **Host Port: 8080 (Your machine)** This is the port on your local machine (the host) that you will use to access the application.

-   **Guest Port (Container Port i.e Inside Docker): 80** This is the port inside the Docker container where the Apache server is listening.

```sh
docker build -t apache-static-site .
```

```sh
docker images
```

Note: apache use port 80, to run docker images

```sh
docker run -p 8080:80 -d apache-static-site
```

```sh
docker ps
```

Now visit <a href="http://0.0.0.0:8080">http://0.0.0.0:8080</a>

## Publish on docker-hub

Note the `usmanmusa/apache-static-site` is my own docker-hub username with the repository name, prototype of yours would be `<your_docker_hub_username>/apache-static-site`

```sh
docker logout
```

```sh
docker login
```

```sh
docker build -t usmanmusa/apache-static-site .
```

```sh
docker push usmanmusa/apache-static-site
```

# Step of running this site after cloning from docker-hub

```sh
docker pull usmanmusa/apache-static-site
```

Now bring it to live, but make sure you have nothing running on port 80, it is the port that the `apache` will be using, while port 8080 is the one you will be visiting.

```sh
docker run -p 8080:80 -d usmanmusa/apache-static-site
```

Now visit <a href="http://0.0.0.0:8080">http://0.0.0.0:8080</a>

Clone the <a href="https://hub.docker.com/r/usmanmusa/apache-static-site">dockerhub repository</a> here!

You can run the container and access its shell using the `docker run` command with the `-it` (interactive + TTY) flag, and specify `/bin/sh` or `/bin/bash` as the shell (since Alpine-based images typically use `sh`):

```sh
docker run -it usmanmusa/apache-static-site /bin/sh

# or

docker run -it usmanmusa/apache-static-site sh
```

To create a container using the `apache-static-site` image, you are to do the following, note our container name is `my_apache_site`

```sh
docker run -d --name my_apache_site usmanmusa/apache-static-site
```

To test to see if it work properly by:

```sh
docker exec my_apache_site curl localhost
```
