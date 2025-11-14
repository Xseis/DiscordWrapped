import os
import json
import requests

bot_token = os.environ.get("DISCORD_TOKEN")
totalmessages = {"total": 0}
channelmessages = {}
servermessages = {}
dms = {}

message_activity = {}

current_year = "2025"

userID = 0

for file in os.listdir("package"):
    if file == "Account":
        with open("package/Account/user.json", "r", encoding="utf-8") as f:
            userdata = json.loads(f.read())
        
        userID = userdata["id"]

    elif file == "Activities":
        pass
    elif file == "Activity":
        pass
    elif file == "Ads":
        pass
    elif file == "Messages":
        for channel in os.listdir(f"package/Messages"):
            if channel[0] == "c":
                with open(f"package/Messages/{channel}/channel.json", "r", encoding="utf-8") as f:
                    channeldata = json.loads(f.read())
                with open(f"package/Messages/{channel}/messages.json", "r", encoding="utf-8") as f:
                    messagesdata = json.loads(f.read())
                
                for message in messagesdata:
                    if channeldata["type"] == "DM":
                        recipient = [recipient for recipient in channeldata["recipients"] if recipient != userID][0]
                        if recipient not in dms:
                            dms[recipient] = {"total": 0}
                        dms[recipient]["total"] += 1
                        if message["Timestamp"][0:4] not in dms[recipient]:
                            dms[recipient][message["Timestamp"][0:4]] = 0
                        dms[recipient][message["Timestamp"][0:4]] += 1

                    totalmessages["total"] += 1
                    if message["Timestamp"][0:4] not in totalmessages:
                        totalmessages[message["Timestamp"][0:4]] = 0
                    totalmessages[message["Timestamp"][0:4]] += 1        
                
    elif file == "Servers":
        pass
    elif file == "Support_Tickets":
        pass

def getUsernameFromID(id):
    data = requests.get(f"https://discord.com/api/users/{id}", headers={"Authorization": f"Bot {bot_token}"}).json()
    return data["username"]

dms_sorted = sorted(dms.items(), key= lambda dm: dm[1]["total"])

print(f"Total messages ever: {totalmessages["total"]}")
print(f"Messages this year: {totalmessages[current_year]}")
mostMessaged = dms_sorted[-1]
print(f"\nMost messaged DM is {getUsernameFromID(mostMessaged[0])} with {mostMessaged[1]["total"]} total messages!")
print(f"You sent them {mostMessaged[1][current_year]} messages this year")