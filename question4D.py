# # [5:14 PM, 7/12/2022] Elder Bro1111: import json
# from aifc import open
# from builtins import input
# from aifc import open
# from builtins import input
import json
import os
def signup():
    #checking if the file already exists or not. If it does not exist create a new one.
    if os.path.exists('./userdetails.json') == False:
        dict = {}
        dict["users"] = []
        with open('userdetails.json', 'w') as fp:
            json.dump(dict, fp)

    newUser = {}
    mobilenumber_or_email = input("ENTER YOUR (mobile number or email address)>>>__")
    user_password = input("ENTER YOUR NEW PASSWORD>>>_")
    newUser["Mobile or Email"] = mobilenumber_or_email
    newUser["User Password"] = user_password
    f = open('userdetails.json')
    oldUsersDictionary = json.load()
    oldUsersList=oldUsersDictionary["users"]
    oldUsersList.append(newUser)
    newUserDictionary={}
    newUserDictionary["users"]=oldUsersList
    f.close()
    with open("userdetails.json", "w") as file:
        json.dump(newUserDictionary, file, indent=4)
signup()
# [5:15 PM, 7/12/2022] Elder Bro1111: 