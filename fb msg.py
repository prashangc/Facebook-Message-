import fbchat
from getpass import getpass
username = str(input("Username: "))
client = fbchat.Client(username, getpass())
no_of_friends = int(input("Number of friends: "))
print("\n")
print("\n")
print("\n")
num=10
for i in range(no_of_friends):
    name = str(input("Name of friend: "))
    print("\n")
    friends = client.searchForUsers(name) # return a list of names
    friend = friends[0]
    msg = str(input("Type the message: "))
    print("\n")
    while num<20:
        sent = client.sendMessage(msg, thread_id=friend.uid)
        if sent:
            print("\n")
            print("Message sent successfully","to",name)
