#/bin/bash
for i in 1 2 3
do
mkdir nginx$i
echo "FROM nginx:latest
 COPY ./index.html /usr/share/nginx/html/index.html" > nginx$i/Dockerfile
echo "<html> <h1> Hello from container $i </h2> </html>" > nginx$i/index.html
done
docker-compose up -d
