docker build -f docker/Dockerfile.CodeLocation -t dagster-code-location:lastest .

docker build -f docker/Dockerfile.Daemon -t dagster-daemon:lastest .

docker build -f docker/Dockerfile.Dagit -t dagster-dagit:lastest .
