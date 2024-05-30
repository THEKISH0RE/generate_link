import base64
import json

def revert_base64(base64_payload):
    decoded_payload = base64.b64decode(base64_payload.encode('utf-8'))
    payload_str = decoded_payload.decode('utf-8')
    payload = json.loads(payload_str)
    return payload
