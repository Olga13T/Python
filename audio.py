import requests
import urllib.request

if __name__ == '__main__':

    REQUEST_STATUS_CODE = 200
    req = requests.get(
        'https://musify.club/track/dl/855887/aloan-invisible.mp3', stream=True)
    if req.status_code == REQUEST_STATUS_CODE:
        with open('invisible.mp3', 'wb') as audio:
            audio.write(req.content)
