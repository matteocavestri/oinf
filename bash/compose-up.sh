#!/bin/bash

# Example bash script to start multiple docker compose files

cd DockerCompose # Docker compose files directory

docker compose -f cloudflared.yaml up -d # Start cloudflared
docker compose -f littlelink.yaml up -d
docker compose -f pihole.yaml up -d

# Add all your docker compose file to start
# To run this script write ./compose-up.sh in your terminal
