from twilio.rest import Client
import os

def make_call(to_number):
    client = Client(os.getenv("TWILIO_SID"), os.getenv("TWILIO_AUTH"))
    call = client.calls.create(
        to=to_number,
        from_=os.getenv("TWILIO_NUMBER"),
        url='https://yourdomain.com/voice/webhook'
    )
    return call.sid
