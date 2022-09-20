import json

def json_stringify(data):
    payload = json.dumps(data)
    return payload, str(len(payload))