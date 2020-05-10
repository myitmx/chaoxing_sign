import os
from fastapi import FastAPI
from cloud_sign import *


app = FastAPI()


@app.post('/sign')
@app.get('/sign')
def sign(*, username: str, password: str, schoolid=None, sckey=None, longitude=None, latitude=None, address=None):
    USER_INFO['username'] = username
    USER_INFO['password'] = password
    USER_INFO['schoolid'] = schoolid
    return interface(USER_INFO, sckey, longitude, latitude, address)