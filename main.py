import os
import json
import requests
import time

os.chdir(os.path.dirname(os.path.abspath(__file__)))

bot_token = os.environ.get("DISCORD_TOKEN")
totalmessages = {"total": 0}
channelmessages = {}
servermessages = {}
dms = {}
groupdms = {}

message_activity = {}

current_year = "2025"

userID = 0
if "package" not in os.listdir():
    print("Could not find the package folder\nMake sure to put it in the same folder as the main.py file!")
    print("\nClosing program in 5 seconds. . .")
    time.sleep(5)
    exit()
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
                    year = message["Timestamp"][0:4]
                    month = message["Timestamp"][5:7]
                    day = message["Timestamp"][8:10]
                    hour = message["Timestamp"][11:13]
                    minute = message["Timestamp"][14:16]
                    second = message["Timestamp"][17:19]
                    # ONLY DMS
                    if channeldata["type"] == "DM":
                        recipient = [recipient for recipient in channeldata["recipients"] if recipient != userID][0]
                        if recipient not in dms:
                            dms[recipient] = {"total": 0}
                        dms[recipient]["total"] += 1
                        if message["Timestamp"][0:4] not in dms[recipient]:
                            dms[recipient][message["Timestamp"][0:4]] = 0
                        dms[recipient][message["Timestamp"][0:4]] += 1
                    
                    if channeldata["type"] == "GROUP_DM":
                        if "recipients" in channeldata:
                            recipients = [recipient for recipient in channeldata["recipients"] if recipient != userID]
                            if channeldata["id"] not in groupdms:
                                groupdms[channeldata["id"]] = {"total": 0, "recipients": recipients, "name": channeldata["name"]}
                            groupdms[channeldata["id"]]["total"] += 1
                    
                    if channeldata["type"] == "GUILD_TEXT":
                        if "guild" in channeldata:
                            if channeldata["guild"]["name"] not in servermessages:
                                servermessages[channeldata["guild"]["name"]] = 0
                            servermessages[channeldata["guild"]["name"]] += 1

                    # EVERY MESSAGE
                    totalmessages["total"] += 1
                    if message["Timestamp"][0:4] not in totalmessages:
                        totalmessages[message["Timestamp"][0:4]] = 0
                    totalmessages[message["Timestamp"][0:4]] += 1        

                    if year not in message_activity:
                        message_activity[year] = {"total": 0}
                    if month not in message_activity[year]:
                        message_activity[year][month] = {"total": 0}
                    if day not in message_activity[year][month]:
                        message_activity[year][month][day] = {"total": 0}
                    message_activity[year][month][day]["total"] += 1
                    message_activity[year][month]["total"] += 1
                    message_activity[year]["total"] += 1
                
    elif file == "Servers":
        pass
    elif file == "Support_Tickets":
        pass

def getUsernameFromID(id):
    data = requests.get(f"https://discord.com/api/users/{id}", headers={"Authorization": f"Bot {bot_token}"}).json()
    try:
        return data["username"]
    except:
        return "Deleted User"

dms_sorted = sorted(dms.items(), key= lambda dm: dm[1]["total"])

# print(message_activity)
# for year in message_activity:
#     print(year)
#     for month in message_activity[year]:
#         if month != "total":
#             print(month, message_activity[year][month]["total"])

print(json.dumps(sorted(groupdms.items(), key= lambda gdm: gdm[1]["total"]), indent= 4))

def Display():
    print(f"Total messages ever: {totalmessages["total"]}")
    print(f"Messages this year: {totalmessages[current_year]}")
    mostMessaged = dms_sorted[-1]
    num2Messaged = dms_sorted[-2]
    num3Messaged = dms_sorted[-3]
    num4Messaged = dms_sorted[-4]
    num5Messaged = dms_sorted[-5]
    num6Messaged = dms_sorted[-6]
    num7Messaged = dms_sorted[-7]
    num8Messaged = dms_sorted[-8]
    num9Messaged = dms_sorted[-9]
    num10Messaged = dms_sorted[-10]
    dms_thisyear = []
    for dm in dms.items():
        if current_year in dm[1]:
            dms_thisyear.append(dm)
    dms_thisyear = sorted(dms_thisyear, key= lambda dm: dm[1][current_year])
    mostMessagedthisyear = dms_thisyear[-1]
    num2Messagedthisyear = dms_thisyear[-2]
    num3Messagedthisyear = dms_thisyear[-3]
    num4Messagedthisyear = dms_thisyear[-4]
    num5Messagedthisyear = dms_thisyear[-5]
    num6Messagedthisyear = dms_thisyear[-6]
    num7Messagedthisyear = dms_thisyear[-7]
    num8Messagedthisyear = dms_thisyear[-8]
    num9Messagedthisyear = dms_thisyear[-9]
    num10Messagedthisyear = dms_thisyear[-10]
    print(f"\nMost messaged DM is {getUsernameFromID(mostMessaged[0])} with {mostMessaged[1]["total"]} total messages!")
    print(f"You sent them {mostMessaged[1][current_year]} messages this year")
    print(f"2nd most messaged: {getUsernameFromID(num2Messaged[0])} with {num2Messaged[1]["total"]} total messages!")
    print(f"3rd most messaged: {getUsernameFromID(num3Messaged[0])} with {num3Messaged[1]["total"]} total messages!")
    print(f"4th most messaged: {getUsernameFromID(num4Messaged[0])} with {num4Messaged[1]["total"]} total messages!")
    print(f"5th most messaged: {getUsernameFromID(num5Messaged[0])} with {num5Messaged[1]["total"]} total messages!")
    print(f"6th most messaged: {getUsernameFromID(num6Messaged[0])} with {num6Messaged[1]["total"]} total messages!")
    print(f"7th most messaged: {getUsernameFromID(num7Messaged[0])} with {num7Messaged[1]["total"]} total messages!")
    print(f"8th most messaged: {getUsernameFromID(num8Messaged[0])} with {num8Messaged[1]["total"]} total messages!")
    print(f"9th most messaged: {getUsernameFromID(num9Messaged[0])} with {num9Messaged[1]["total"]} total messages!")
    print(f"10th most messaged: {getUsernameFromID(num10Messaged[0])} with {num10Messaged[1]["total"]} total messages!")

    print(f"\nMost messaged this year: {getUsernameFromID(mostMessagedthisyear[0])} with {mostMessagedthisyear[1][current_year]} total messages!")
    print(f"2nd most messaged this year: {getUsernameFromID(num2Messagedthisyear[0])} with {num2Messagedthisyear[1][current_year]} total messages!")
    print(f"3rd most messaged this year: {getUsernameFromID(num3Messagedthisyear[0])} with {num3Messagedthisyear[1][current_year]} total messages!")
    print(f"4th most messaged this year: {getUsernameFromID(num4Messagedthisyear[0])} with {num4Messagedthisyear[1][current_year]} total messages!")
    print(f"5th most messaged this year: {getUsernameFromID(num5Messagedthisyear[0])} with {num5Messagedthisyear[1][current_year]} total messages!")
    print(f"6th most messaged this year: {getUsernameFromID(num6Messagedthisyear[0])} with {num6Messagedthisyear[1][current_year]} total messages!")
    print(f"7th most messaged this year: {getUsernameFromID(num7Messagedthisyear[0])} with {num7Messagedthisyear[1][current_year]} total messages!")
    print(f"8th most messaged this year: {getUsernameFromID(num8Messagedthisyear[0])} with {num8Messagedthisyear[1][current_year]} total messages!")
    print(f"9th most messaged this year: {getUsernameFromID(num9Messagedthisyear[0])} with {num9Messagedthisyear[1][current_year]} total messages!")
    print(f"10th most messaged this year: {getUsernameFromID(num10Messagedthisyear[0])} with {num10Messagedthisyear[1][current_year]} total messages!")

#Display()
input("Press enter to exit")