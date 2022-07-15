# ### append()
# a=open("pavigoapl.json","a")
# b=a.write(",\n this is append")
# print(b)

# import json
# a=[{
#     "Name":"pavithra",
#    "Age":16,
#    "Class":"maths",
#    "Marks":60
#    },
#    {
#     "Name":"priya",
#    "Age":17,
#    "Class":"maths",
#    "Marks":70
#    },
#    {
#     "Name":"abhi",
#    "Age":18,
#    "Class":"maths",
#    "Marks":90
#    },
#    {
#     "Name":"jhon",
#    "Age":19,
#    "Class":"maths",
#    "Marks":80
#    }]
# with open("pavithra.json","w")as f:
#     json.dump(a,f,indent=3)
# print(a)


# from builtins import print
# print("Hii")
# def fun(a):
#     print(a)
#     def fun(b):
#         print(b)
#     fun(20)
# fun(10)


# a={"a":1,"b":2,"c":3}
# # b={"d":4,"e":5,"f":6}
# i=0
# while i<len(a):
#     d=(a,{"d":4,"e":5,"f":6})
#     i+=1
# print(d)


#### rejection more consitions
# from builtins import input, int, print
# import re
# a=(input("enter any password"))
# if re.search("[@%^*]",a) and re.search("[a-z A-Z]",a) and re.search("[0-9]",a):
#     print(a)
# else:
#     print("wrong")


####file:: write a file
# from aifc import open
# from builtins import print
# a=open("pavi.txt","w")
# b=a.write("this is my information")
# print(b)

#### file:: read a file
# import json
# from aifc import open
# from builtins import print
# a=open("pavithra.json","r")
# b=json.load(a)
# print(b)


#### file:: append information
# import json
# from builtins import open, print
# a=open("pavithra.json","w")
# a.write("\n include another information also")
# a.write("\n include office details also")
# print(a)


# import json
# with open("pavithra.json","w")as f:
#     b=json.load(f)
# print(b)

# import json
# f=open("pavithra.json")
# b=json.load(f)
# print(b)