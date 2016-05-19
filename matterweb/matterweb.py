
import json
import requests


def notify(url, **kwargs):
    push(url, kwargs)


def push(url, payload):
    response = requests.post(url=url, data=json.dumps(payload), headers={
        "Content-Type": "application/json"
    })
    if response.status_code == 200:
        return True
    return False

