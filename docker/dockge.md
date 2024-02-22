# Create directories that store your stacks and stores Dockge's stack

```bash
mkdir -p /opt/stacks /opt/dockge
cd /opt/dockge
```

# Download the compose.yaml

```bash
curl https://raw.githubusercontent.com/louislam/dockge/master/compose.yaml --output compose.yaml
```

# Start the server

```bash
docker compose up -d
```
# If you are using docker-compose V1 or Podman
# docker-compose up -d
