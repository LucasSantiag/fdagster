## Docker create all images

docker build -f docker/Dockerfile.CodeLocation -t dagster-code-location:latest .

docker build -f docker/Dockerfile.Daemon -t dagster-daemon:latest .

docker build -f docker/Dockerfile.Dagit -t dagster-dagit:latest .
