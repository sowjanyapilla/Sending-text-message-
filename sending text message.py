#sending text message

# Install Twilio library : pip install twilio
from twilio.rest import Client

# Your Twilio account SID and Auth Token
account_sid = 'AC5*****2fd3cf957bbfbdb502377****'
auth_token = '******35bec436a1204b*********88'

# Create a Twilio client
client = Client(account_sid, auth_token)

# Replace 'to_phone_number' with the recipient's phone number
# Replace 'from_phone_number' with your Twilio phone number
message = client.messages.create(
    body="Hey,Hi I just text u using python",
    from_='+15312312282',  # Replace with your Twilio phone number
    to='+91234567890'      # Replace with the recipient's phone number
)

