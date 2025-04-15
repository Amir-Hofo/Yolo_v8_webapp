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
docker build -t yolov8-app .
```

# run container
```bash
docker run -p 8501:8501 --name yolov8-container yolov8-app
```

# container status
```bash
docker ps
```

# container logs
```bash
docker logs yolov8-container
```

# dockerhub

## tag image
```bash
docker tag yolov8-app amirhofo/yolov8-app:1.0
```
## push
```bash
docker push amirhofo/yolov8-app:1.0
```