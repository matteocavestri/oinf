# Setup FreqTrade using Dockge

- Add the docker compose file to Dockge
- Go to the freqtrade configuration folder (usually `/opt/freqtrade`)
- Run

```bash
# Pull the freqtrade image
docker compose pull

# Create user directory structure
docker compose run --rm freqtrade create-userdir --userdir user_data

# Create configuration - Requires answering interactive questions
docker compose run --rm freqtrade new-config --config user_data/config.json
```
