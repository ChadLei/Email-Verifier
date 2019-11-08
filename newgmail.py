import sys
import imaplib
import getpass
import email
import email.header
import datetime
import re
# import bs4
import webbrowser
import time



EMAIL_FOLDER = "Inbox"

# EMAIL_ACCOUNT  = "test"
# PASSWORD = "test"

bstn = '(FROM "service@bstn.com")'

def process_mailbox(M):
    """
    Do something with emails messages in the folder.
    For the sake of this example, print some headers.
    """

    rv, data = M.search(None, bstn)
    if rv != 'OK':
        print "No messages found!"
        return

    URLS = []

    for num in data[0].split():
        rv, data = M.fetch(num, '(RFC822)')
        if rv != 'OK':
            print "ERROR getting message", num
            return

        msg = email.message_from_string(data[0][1])
        decode = email.header.decode_header(msg['Subject'])[0]
        subject = unicode(decode[0])
        # print 'Message %s: %s' % (num, subject)

        raw_email = data[0][1] # here's the body, which is raw headers and html and body of the whole email including headers and alternate payloads
        msg = email.message_from_string(raw_email)

        for part in msg.walk():
            # each part is a either non-multipart, or another multipart message
            # that contains further parts... Message is organized like a tree
            if part.get_content_type() == 'text/html':
                plain_text = part.get_payload()
                # print plain_text # prints the raw text
                # break

                # expr = r'((http)s?:\/\/((\.)?\w+)+(\/\S*)*)'
                # #Parse with regex: Grabs possible URLs (first only). Case insensitive.
                # matches = re.match(expr, plain_text)
                # url = matches[0]
                # print(url)
                # break

                # <a href=3D"https://raffle.bstn.=
                # com/verify/c4b7668ad54792222642e31806896f" class=3D"button__link" style=3D"=
                # text-align: center; background-color: #000000; color: #FFFFFF; text-decorat=
                # ion: none; display: inline-block;">

                # soup = bs4.BeautifulSoup(plain_text, features="html.parser")
                # aTags = soup.find_all("a",href=True)
                # urls = [tag['href'] for tag in aTags if 'href' in tag.attrs and "https://raffle.bstn" in tag['href']]
                # print aTags
                # for i in aTags:
                #     print(i['href'])
                # print urls

                match = re.search(r'href=3D"https://raffle[\'"]?([^\'" >]+)', plain_text, flags=re.MULTILINE)
                if match:
                    # url = "".join(match.groups)
                    url = match.group(0).replace('href=3D"', '').replace('=', '').replace('\r\n', '')
                    URLS.append(url)

    for link in URLS:
        webbrowser.open(link)
        time.sleep(4)


    # Iterate through newest messages in decending order starting with latest_email_id
    # ids = data[0]
    # id_list = ids.split()
    # #get the most recent email id
    # latest_email_id = int( id_list[-1] )

    #the '-1' dictates reverse looping order
    # for i in range( latest_email_id-6, latest_email_id-7, -1 ):
    #    typ, data = M.fetch( i, '(RFC822)' )
    #
    #    for response_part in data:
    #       if isinstance(response_part, tuple):
    #           msg = email.message_from_string(response_part[1])
    #           varSubject = msg['subject']
    #           varFrom = msg['from']
    #
    #    #remove the brackets around the sender email address
    #    varFrom = varFrom.replace('<', '')
    #    varFrom = varFrom.replace('>', '')
    #
    #    #add ellipsis (...) if subject length is greater than 35 characters
    #    if len( varSubject ) > 35:
    #       varSubject = varSubject[0:32] + '...'
    #
    #    print '[' + varFrom.split()[-1] + '] ' + varSubject


M = imaplib.IMAP4_SSL('imap.gmail.com')

try:
    rv, data = M.login(EMAIL_ACCOUNT, PASSWORD)
except imaplib.IMAP4.error:
    print "Login Failed! "
    sys.exit(1)

print rv, data

# rv, mailboxes = M.list()
# if rv == 'OK':
#     print "Mailboxes:"
#     print mailboxes

rv, data = M.select(EMAIL_FOLDER, readonly=True)
if rv == 'OK':
    print "Searching mailbox...\n"
    process_mailbox(M)
    M.close()
else:
    print "ERROR: Unable to open mailbox. ", rv
#
# M.logout()
