# DiscordWrapped
Similar to Spotify wrapped, but for discord

# HOW TO RUN
## 1. Request your discord data (REQUIRED)
1. Select the cogwheel in the lower-left corner. 
2. Select the Data & Privacy tab.
3. Under Request your data, select the Request Data button.
4. In the Submit Data Request window, select which data you'd like to receive. The data will be sent to your Discord account's email address. (For best results, choose everything)
<img width="400" height="283" alt="image" src="https://support.discord.com/hc/article_attachments/30074490845975" />

*It will take up to 30 days before you recieve your data*


## 2. Get your discord bot token 
Go to [Discord Developer Portal](https://discord.com/developers/applications), create a new application. (The application name does not matter)<br>
Then go to the Bot tab and scroll down to reset / reveal your bot's token (DO NOT SHARE THIS WITH ANYONE)

<img width="459" height="212" alt="{0EFA3FD1-AEBA-40F7-862F-88E0B19B0B04}" src="https://github.com/user-attachments/assets/432a1654-d756-4bab-ac0e-f8a6d221c0f6" />


## 3. Set the token as an environment variable
Set the environment variable "DISCORD_TOKEN" to your bot token
### Windows
```cmd
setx DISCORD_TOKEN YOUR_TOKEN_HERE
```
<img width="860" height="196" alt="image" src="https://github.com/user-attachments/assets/67ff098d-b172-46ca-9b3f-f2078be05f63"/><br>
### Linux / macOS
```bash
export DISCORD_TOKEN="YOUR_TOKEN_HERE"
```

## 4. Run
Extract your data package, and put the package folder in the same directory as the main.py before running

<img width="142" height="88" alt="{0A678610-2BC9-4A54-9971-6E46F5BD96FB}" src="https://github.com/user-attachments/assets/f16537f8-755e-47e6-be80-63e142697b73" />
