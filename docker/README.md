# Docker
Here you can find every docker configuration for your infrastructure

### Apply a Docker Compose File

- Install Docker and Docker Compose ([Docks Here](https://docs.docker.com/engine/install/))
    Example for RHEL based systems (Fedora)
    ```bash
    # Update your system
    sudo dnf update -y
    # Set up the repository
    sudo dnf -y install dnf-plugins-core
    sudo dnf config-manager --add-repo https://download.docker.com/linux/fedora/docker-ce.repo
    # Install docker and docker compose
    sudo dnf install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
    # Start docker
    sudo systemctl start docker
    # Try docker --> It will be prompted an Hello World message
    sudo docker run hello-world

    # POST INSTALL
    # Create docker group
    sudo groupadd docker
    # Add your user to docker engine
    sudo usermod -aG docker $USER
    # Apply changes
    newgrp docker
    # Test docker in user mode
    docker run hello-world
    ```

- Apply a docker compose file
    ```bash
    docker compose -f dockge.yaml up -d
    ```
    To install dockge read dockge.md

### Use Dockge

- Install Docker and Docker Compose
- Install curl
    Example for RHEL based systems (Fedora)
    ```bash
    sudo dnf install curl
    ```

- Create directories that store your stacks and stores Dockge's stack
    ```bash
    mkdir -p /opt/stacks /opt/dockge
    cd /opt/dockge
    ```

- Download compose.yaml (you can find that file here as dockge.yaml)
    ```bash
    curl https://raw.githubusercontent.com/louislam/dockge/master/compose.yaml --output compose.yaml
    ```
- Start the server
    ```bash
    docker compose up -d
    # If you use dockge.yaml
    docker compose -f dockge.yaml up -d
    ```
