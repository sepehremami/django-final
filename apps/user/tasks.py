import random 
import string
from celery import shared_task
from django.core.cache import cache
from config import settings
from kavenegar import *




@shared_task 
def send_otp_code(phone):
    otp_code = "".join(random.choices(string.digits, k=6))

    cache.set(phone, otp_code, timeout=300)
    params = {
        'receptor': phone, 
        'template':'',
        'token': otp_code,
        'type': 'sms',
    }
    try:
        # api call
        print(otp_code)
    except Exception as e:
        print (e)