## Docker create all images

docker build -f docker/Dockerfile.CodeLocation -t dagster-code-location:latest .

docker build -f docker/Dockerfile.Daemon -t dagster-daemon:latest .

docker build -f docker/Dockerfile.Dagit -t dagster-dagit:latest .

## Create minikube deployment

kubectl create deployment dagster-code-location --image=dagster-code-location:latest
