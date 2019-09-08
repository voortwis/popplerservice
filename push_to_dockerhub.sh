docker build . -t voortwis/popplerservice:latest

# run:
# docker run -p 5000:5000 voortwis/poppelerservice:latest

docker login --username=voortwis
docker push voortwis/popplerservice