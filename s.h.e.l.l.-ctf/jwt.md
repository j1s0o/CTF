# Jwt

URL: [http://3.142.122.1:9334/](http://3.142.122.1:9334/)  
First we see in source code have **AdminNames**

URL : [http://3.142.122.1:9334/adminNames](http://3.142.122.1:9334/adminNames)

![image](https://user-images.githubusercontent.com/73061198/121111212-ab253c00-c838-11eb-91d8-01bf039aa43d.png)

use burp /login we have token

![image](https://user-images.githubusercontent.com/73061198/121111268-c2fcc000-c838-11eb-875f-1508d2a00cd9.png)

we use jwt.io

![image](https://user-images.githubusercontent.com/73061198/121111361-ea538d00-c838-11eb-8a38-d8160b342fe0.png)

Next we use cyberchef to decode **snyfr = false** \(ROT13\) **din\_djarin11=qva\_qwneva11**

/admin we see success : false =&gt; **admin : gehr**

![image](https://user-images.githubusercontent.com/73061198/121111537-3e5e7180-c839-11eb-8c40-dd8029ba7431.png)

"message":"Maybe send the token via Headers ... for Authorization?

we use /getFile?file=../.env and we will find the secret key

![image](https://user-images.githubusercontent.com/73061198/121111635-72399700-c839-11eb-9787-fb3c469e1577.png)

![image](https://user-images.githubusercontent.com/73061198/121111704-91382900-c839-11eb-822d-7e658effcd80.png)

Final, we have the token

![image](https://user-images.githubusercontent.com/73061198/121111767-a8771680-c839-11eb-984f-9df63ddb7769.png)

flag : FURYY{G0x3af\_q0\_z4gg3e\_4r91ns4506s384q460s0s0p6r9r5sr4n}

flag: SHELL{T0k3ns\_d0\_m4tt3r\_4e91af4506f384d460f0f0c6e9e5fe4a}

