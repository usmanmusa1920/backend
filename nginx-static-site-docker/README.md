# Steps of dockerizing static site using nginx locally

To build docker images, we use two ports numbers as follows:

-   **Host Port: 8080 (Your machine)** This is the port on your local machine (the host) that you will use to access the application.

-   **Guest Port (Container Port i.e Inside Docker): 80** This is the port inside the Docker container where the Nginx server is listening.

```sh
docker build -t nginx-static-site .
```

```sh
docker images
```

Note: nginx use port 80, to run docker images

```sh
docker run -p 8080:80 -d nginx-static-site
```

```sh
docker ps
```

Now visit <a href="http://0.0.0.0:8080">http://0.0.0.0:8080</a>

## Publish on docker-hub

Note the `usmanmusa/nginx-static-site` is my own docker-hub username with the repository name, prototype of yours would be `<your_docker_hub_username>/nginx-static-site`

```sh
docker logout
```

```sh
docker login
```

```sh
docker build -t usmanmusa/nginx-static-site .
```

```sh
docker push usmanmusa/nginx-static-site
```

# Step of running this site after cloning from docker-hub

```sh
docker pull usmanmusa/nginx-static-site
```

Now bring it to live, but make sure you have nothing running on port 80, it is the port that the NGINX will be using, while port 8080 is the one you will be visiting.

```sh
docker run -p 8080:80 -d usmanmusa/nginx-static-site
```

Now visit <a href="http://0.0.0.0:8080">http://0.0.0.0:8080</a>

Clone the <a href="https://hub.docker.com/r/usmanmusa/nginx-static-site">dockerhub repository</a> here!

You can run the container and access its shell using the `docker run` command with the `-it` (interactive + TTY) flag, and specify `/bin/sh` or `/bin/bash` as the shell (since Alpine-based images typically use `sh`):

```sh
docker run -it usmanmusa/nginx-static-site /bin/sh

# or

docker run -it usmanmusa/nginx-static-site sh
```
