# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = 'AC0b105896a53727876c4fea3e6c21d8e2'
auth_token = '5f1518ef578fe4a5caf9f19fe4b57a9e'
client = Client(account_sid, auth_token)

message = client.messages.create(
                              body='Hi there!',
                              from_='+14704503756',
                              to='+91 73959 84796'
                          )

print(message.sid)
