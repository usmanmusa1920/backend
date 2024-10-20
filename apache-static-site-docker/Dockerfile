# This is the the code used to build the Dockerfile. This Dockerfile is used to create a Docker image based on the Ubuntu operating system, which will run an Apache web server.

# This line specifies the base image for the Docker container, which in this case is the latest version of Ubuntu.
FROM ubuntu:latest

# The -y flag automatically answers "yes" to any prompts during the update process.
RUN apt-get -y update

# This installs the Apache web server and curl tool (used for making HTTP requests). The -y flag automatically agrees to any installation prompts.
RUN apt-get install -y apache2 curl

# This informs Docker that the container will listen on port 80, the default port for HTTP traffic.
EXPOSE 80

# This sets the working directory inside the container. Future commands will run in the /var/www/html directory, which is the default location for serving web files in Apache.
WORKDIR /var/www/html

# This copies the index.html file from the local machine (where the Dockerfile is built) to the container's /var/www/html directory, effectively making it the main page of the Apache server.
COPY index.html /var/www/html/index.html

# This specifies the command that will be run when the container starts. apache2ctl is the control script for Apache.
ENTRYPOINT ["/usr/sbin/apache2ctl"]

# This provides additional arguments to the ENTRYPOINT command. -D FOREGROUND ensures that Apache runs in the foreground and doesn't exit, keeping the container alive and the web server running.
CMD ["-D", "FOREGROUND"]

# In summary, this Dockerfile creates a container that runs an Apache web server on Ubuntu, serving an index.html file, and listens for HTTP traffic on port 80.
