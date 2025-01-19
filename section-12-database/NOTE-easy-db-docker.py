# 1-first you need to create a virtual docker network in the same subnet as your computer

# docker network create \
#   --subnet=192.168.1.0/24 \
#   my-docker-network

# 2-Secondly, you can create the container by editing the parameters.
# docker run --name mysql-container \
#   --net my-docker-network \
#   --ip 192.168.1.x \
#   -e MYSQL_ROOT_PASSWORD=my-secret-pw \
#   -e MYSQL_DATABASE=mydatabase \
#   -e MYSQL_USER=myuser \
#   -e MYSQL_PASSWORD=myuserpassword \
#   -v mysql-data:/var/lib/mysql \
#   -p 3306:3306 \
#   -d mysql:latest //or lts 

# NOTE : If your computer is in a different subnet, edit the parameters
