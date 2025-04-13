# login docker
```bash
docker logout   
docker login
```

# create Dockerfile
```bash
docker init
```

# create image file
```bash
docker build -t your-image-name .
```

# run container
```bash
docker run -it --name your-container-name your-image-name
```
or
```bash
docker run -d --name your-container-name your-image
```

# container status
```bash
docker ps
```

# container logs
```bash
docker logs container-name
```