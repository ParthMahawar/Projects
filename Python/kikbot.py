from kik import KikApi
import requests
import json

requests.post(
    'https://api.kik.com/v1/config',
    auth=('nonamesleft6273', 'ce4b0feb-5287-4c6f-ad1c-344e958e2a09'),
    headers={
        'Content-Type': 'application/json'
    },
    data=json.dumps({
        'webhook': 'https://example.com/incoming', 
        'features': {
            'receiveReadReceipts': False, 
            'receiveIsTyping': False, 
            'manuallySendReadReceipts': False, 
            'receiveDeliveryReceipts': False
        }
    })
)

print(requests.get(
    'https://api.kik.com/v1/config',
    auth=('nonamesleft6273', 'ce4b0feb-5287-4c6f-ad1c-344e958e2a09')
))