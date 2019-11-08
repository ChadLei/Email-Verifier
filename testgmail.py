import imaplib
import email
import quopri
import HTMLParser

class parseLinks(HTMLParser.HTMLParser):
    def handle_starttag(self, tag, attrs):
        global global_futures_fair_value
        if tag == 'a':
            for name in attrs:
                # if name == 'href':
                print name
                # print value
        else:
            print('NAOPE')

M = imaplib.IMAP4_SSL('imap.gmail.com')
M.login('test','test')


M.select('Inbox')

rv, data = M.search(None, '(FROM "service@bstn.com")')
typ, msg_data = M.fetch('1', '(RFC822)')

msg = email.message_from_string(msg_data[0][1])

# html_text = msg.get_payload(0)

msg = str(msg.get_payload()[0])
msg = quopri.decodestring(msg)

linkParser = parseLinks()
linkParser.handle_starttag('a',msg)




<a #000000;="" #ffffff;="" background-color:="" c4b7668ad54792222642e31806896f"="" center;="" class='3D"button__link"' color:="" com="" display:=""
href='3D"https://raffle.bstn.=' inline-block;"="" none;="" style='3D"=' text-align:="" text-decorat="ion:" verify="">\n<span "="" #ffffff;=""
class='3D"button__text=' none;"="" style='3D"color:' text-decoration:="">
