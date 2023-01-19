import firebase_admin
from firebase_admin import credentials
from firebase_admin import messaging

cred = credentials.Certificate("config/serviceAccountKey.json")
firebase_admin.initialize_app(cred)

# This registration token comes from the client FCM SDKs.
registration_token = ''

# See documentation on defining a message payload.
message = messaging.Message(
    notification=messaging.Notification(
        title='test server',
        body='test server message',
    ),
    token=registration_token,
)

# Send a message to the device corresponding to the provided
# registration token.
response = messaging.send(message)
# Response is a message ID string.
print('Successfully sent message:', response)