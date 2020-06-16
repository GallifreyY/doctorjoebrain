docker rmi $(docker images | grep "none" | awk '{print $3}')

# build image
cd flask
docker image build -t flask-demo:05 . 

#  run flask container
docker container run -d -it -p 5000:5000 flask-demo:05 