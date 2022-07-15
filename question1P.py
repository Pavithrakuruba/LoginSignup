# from aifc import open
# from builtins import input, print
# import json
# print("Welcome to login or signup")
# b={}
# c=[]
# a=input("enter login or signup")
# if a=="signup":
#     print("u can sign up hear")
#     fn=input("first name")
#     ln=input("last name:")
#     phoneno=(input("enter phone number"))
#     pw=(input("enter password:"))
#     comform=input("conform password")
#     print("ur signup is succesful")
#     # b["FirstName"]=fn
#     # b["LastName"]=ln
#     # b["PhoneNo"]=phoneno
#     # b["Password"]=pw
#     # b["Comformpw"]=comform
#     b={"firstname":fn,"lastname":ln,"pnonenumber":phoneno,"password":pw,"conformpa":comform}
#     c.append(b)
#     with open("pavigopal.json","a")as f:
#         json.dump(b,f,indent=3)
#     # print(a)
# elif a=="login":
#     x=input("enter user name")
#     y=input("enter password")
#     b["UserName"]=x
#     b["Password"]=y
#     c.append(b)
#     with open("pavigopal.json","w")as f:
#         json.dump(b,f,indent=3)
#     print(b)


from aifc import open
from builtins import input, print
import json
print("Welcome to login or signup")
b={}
c=[]
a=input("enter login or signup")
if a=="signup":
    print("u can sign up hear")
    fn=input("first name")
    ln=input("last name:")
    phoneno=(input("enter phone number"))
    pw=(input("enter password:"))
    comform=input("conform password")
    print("ur signup is succesful")
    b["FirstName"]=fn
    b["LastName"]=ln
    b["PhoneNo"]=phoneno
    b["Password"]=pw
    b["Comformpw"]=comform
    # b={"firstname":fn,"lastname":ln,"pnonenumber":phoneno,"password":pw,"conformpa":comform}
    c.append(b)
    with open("pavigopal.json","a")as f:
        json.dump(b,f,indent=3)
    # print(a)
elif a=="login":
    x=input("enter user name")
    y=input("enter password")
    b["UserName"]=x
    b["Password"]=y
    c.append(b)
    with open("pavigopal.json","w")as f:
        json.dump(b,f,indent=3)
    print(b)



    

    