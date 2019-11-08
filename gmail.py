import poplib
import string, random
import StringIO, rfc822
import logging

bstn = "service@bstn.com"
SERVER = "pop.gmail.com"

# USER  = "test"
# PASSWORD = "test"

# connect to server
SERVER = poplib.POP3_SSL(SERVER)
# server = poplib.POP3(SERVER)

# login
SERVER.user(USER)
SERVER.pass_(PASSWORD)

#list items on server
resp, items, octets = SERVER.list()
print(items)

# download the first message in the list
id, size = string.split(items[0])
resp, text, octets = SERVER.retr(id)

# convert list to Message object
text = string.join(text, "\n")
file = StringIO.StringIO(text)
message = rfc822.Message(file)

# output message
# print(message['From']),
# print(message['Subject']),
# print(message['Date']),
# print(message.fp.read())

#OTHER GUIDE
# pop3info = SERVER.stat() #access mailbox status (message count, mailbox size)
# print("Total number of Emails: " + str(pop3info[0]))

# print ("\n\nStart Reading Messages\n\n")
# for i in range(pop3info[0]):
#     for message in SERVER.retr(i+1)[1]:
#         print (message['From'])


# (server_msg, body, octets) = SERVER.retr(7)[1]
# print(SERVER.retr(-7)[1])

SERVER.quit()
