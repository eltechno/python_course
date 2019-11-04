from twilio.rest import Client

# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure

account_sid = ''
auth_token = ''
client = Client(account_sid, auth_token)
msg_body = "Your Yummy Cupcakes Company order of 1 dozen frosted cupcakes has shipped and should be delivered on July 10, 2019. Details: http://www.yummycupcakes.com/"

message = client.messages \
                .create(
                     body= msg_body,
                     status_callback='http://postb.in/1234abcd',
                     media_url=['https://upload.wikimedia.org/wikipedia/en/0/02/Homer_Simpson_2006.png'],
                     from_='whatsapp:+14155238886',
                     to='whatsapp:+50245020197'
                 )
print(message.sid)