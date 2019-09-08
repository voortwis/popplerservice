# PopplerService - RESTfull poppler utils in a docker container
Allows upload of an image for PopplerUtils running in a container. 
- /pdfinfo (should be transformed to json)
- /thumbnail (will return thumbnail (max 200x200px) of first page of uploaded pdf)
- MORE TO COME..

### Installing and Running

You can clone this repository or download a zip file, build and run the Docker image.

```
$ docker build -t popplerservice .
$ docker run -d -p 5000:5000 popplerservice
```

OR you can pull and/or run the Docker image from my repository on Docker Hub

```
docker pull voortwis/popplerservice
docker run -d -p 5000:5000 voortwis/popplerservice
```
Then open up browser to http://localhost:5000
