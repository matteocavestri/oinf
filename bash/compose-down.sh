#!/bin/bash

# Example bash script to stop all docker compose 

cd DockerCompose # Docker compose files directory

docker compose -f cloudflared.yaml down # stop cloudflared
docker compose -f littlelink.yaml down
docker compose -f pihole.yaml down

# Add all your docker compose file to stop
# To run this script write ./compose-down.sh in your terminal
