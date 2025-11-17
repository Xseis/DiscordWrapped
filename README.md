# DiscordWrapped
Similar to Spotify wrapped, but for discord

## 1. Get your discord bot token 
Go to [Discord Developer Portal](https://discord.com/developers/applications), create a new application. (The application name does not matter)<br>
Then go to the Bot tab and scroll down to reset / reveal your bot's token (DO NOT SHARE THIS WITH ANYONE)

<img width="459" height="212" alt="{0EFA3FD1-AEBA-40F7-862F-88E0B19B0B04}" src="https://github.com/user-attachments/assets/432a1654-d756-4bab-ac0e-f8a6d221c0f6" />


## 2. Set the token as an environment variable
Set the environment variable "DISCORD_TOKEN" to your token by running setx
### Windows
```cmd
setx DISCORD_TOKEN YOUR_TOKEN_HERE
```
<img width="860" height="196" alt="image" src="https://github.com/user-attachments/assets/67ff098d-b172-46ca-9b3f-f2078be05f63"/><br>
### Linux / macOS
```bash
export DISCORD_TOKEN="YOUR_TOKEN_HERE"
```

