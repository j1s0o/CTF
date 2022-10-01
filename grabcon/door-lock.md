---
description: 'web: http://34.135.171.18'
---

# Door Lock

Đầu tiên ta tạo tài khoản đăng nhập

![](../.gitbook/assets/image%20%281%29.png)

![](../.gitbook/assets/image%20%282%29.png)

```text
http://34.135.171.18/profile/index.php?id=1433
```

Bài này ta sẽ đi bruce force id

Sử dụng burp suit để thực hiện

![](../.gitbook/assets/image%20%285%29.png)

![](../.gitbook/assets/image%20%284%29.png)

![](../.gitbook/assets/image%20%2813%29.png)

Ta thấy id = 1766 là khác với các id khác nên set id = 1766 để lấy flag

![](../.gitbook/assets/image%20%2815%29.png)

![](../.gitbook/assets/image%20%283%29.png)

Flag: GrabCON{E4sy\__1D0R\__}

