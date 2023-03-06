docker build -t bird_tracker .
docker run -v $(pwd)/output:/app/output bird_tracker
