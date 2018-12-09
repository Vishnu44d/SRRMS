from SRRMSv2.config import key
from flask import request

def validate_key(user_key):
    if user_key == key:
        return 1
    return 0
