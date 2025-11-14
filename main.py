import os
import json

totalmessages = 0
channelmessages = {}
servermessages = {}
dms = {}

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
                
                channelmessages[channel] = {"messages": 0, "name": ""}

                if "name" in channeldata:
                    channelmessages[channel]["name"] = channeldata["name"]
                if "guild" in channeldata:
                    if channeldata["guild"]["id"] not in servermessages:
                        servermessages[channeldata["guild"]["id"]] = {"name": channeldata["guild"]["name"], "messages": 0}

                elif channeldata["type"] == "DM":
                    channelmessages[channel]["type"] = "DM"
                    channelmessages[channel]["name"] = [id for id in channeldata["recipients"] if id != userID]

                for message in messagesdata:
                    totalmessages += 1
                    channelmessages[channel]["messages"] += 1
                    if "guild" in channeldata:
                        servermessages[channeldata["guild"]["id"]]["messages"] += 1
                    #print(json.dumps(message, ensure_ascii=False, indent=4))
                
    elif file == "Servers":
        pass
    elif file == "Support_Tickets":
        pass
    print(file)

print(f"Total messages: {totalmessages}")
sorted_dict = dict(sorted(channelmessages.items(), key=lambda k: k[1]["messages"]))
print(json.dumps(sorted_dict, indent=4, ensure_ascii=False))

sorted_dict = dict(sorted(servermessages.items(), key= lambda k: k[1]["messages"]))
print(json.dumps(sorted_dict, indent=4, ensure_ascii=False))