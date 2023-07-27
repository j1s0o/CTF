# ImaginaryCtf 2023

## Blank

Bài này khi đọc source ta sẽ thấy nó sẽ truy xuất sqlite3 để đăng nhập và gán req.session.username = username

<figure><img src=".gitbook/assets/image (62).png" alt=""><figcaption></figcaption></figure>

Và nếu như username là admin thì sẽ xem được flag

<figure><img src=".gitbook/assets/image (63).png" alt=""><figcaption></figcaption></figure>

Đầu tiên ta sẽ xem trong dockerfile và thấy nó không có tiến hành thêm vào database cái gì hết nên ta thấy admin chắc cũng sẽ không có trong đó vậy ta sẽ tìm cách làm sao để bypass với username = admin & password = ...

Khi tiến hành debug code thì ta sẽ thấy các câu lệnh để bỏ qua đơn giản không hiệu quả và nếu muốn code chạy xuống đoạn gán session thì truy vấn sql phải thành công

Vậy nên ta sẽ bypass bằng cách sử dụng <mark style="color:red;">**sqlite\_master**</mark> vì  nó chứa thông tin của cơ sở dữ liệu nên có thể truy vấn được

Payload

```sql
username=admin&password=" UNION SELECT null, null, null FROM sqlite_master -- -
```

<figure><img src=".gitbook/assets/image (64).png" alt=""><figcaption></figcaption></figure>

## **Idoriot**

Khi ta kiểm tra register thì ta sẽ thấy lúc ta đăng ký nó sẽ có 1 input user\_id được ẩn đi chỉ cần thay user\_id = 1 lúc đăng ký thì nó sẽ thành account của admin thôi

<figure><img src=".gitbook/assets/image (65).png" alt=""><figcaption></figcaption></figure>

## roks

Bài này khi đọc code trong file.php thì ta sẽ thấy&#x20;

<figure><img src=".gitbook/assets/image (66).png" alt=""><figcaption></figcaption></figure>

Nó sẽ tiến hành urldecode param file 1 lần ở $filename và 1 lần nữa ở $filePath mà trong câu điều kiện đầu tiên thì nó sẽ filter các ký tự là / và . để tránh lfi vậy nên ta sẽ sử urlencode 3 lần để lúc nó decode lần đầu thì vẫn chưa có 2 ký tự bị cấm nên chúng ta có thể bypass được điều kiện trên rồi

```
. => %25252E
/ => %25252F
```

Mà ta đọc trong dockerfile thì thấy flag.png được lưu ở / nên ta sẽ path traversal vô đó để xem thôi

Payload

```
%25252E%25252E%25252F%25252E%25252E%25252F%25252E%25252E%25252F%25252E%25252E%25252Fflag%25252Epng
```

<figure><img src=".gitbook/assets/image (67).png" alt=""><figcaption></figcaption></figure>

## Perfect Picture

Bài này khá đơn giản chỉ là bypass các điều kiện để có 1 tấm ảnh hoàn hảo thôi

<figure><img src=".gitbook/assets/image (68).png" alt=""><figcaption></figcaption></figure>

Tại vì nó đã mở sẵn cho mình flag.txt rồi nên khi gửi đúng điều kiện thì nó sẽ return cho mình flag các điều kiện như trên ta sẽ dùng code python để tạo ra 1 tấm ảnh phù hợp

```python
from PIL import Image

# Create an image with the required dimensions (690x420)
bypass_image = Image.new('RGBA', (690, 420), (255, 255, 255, 255))

# Set the required pixels to bypass the checks
bypass_image.putpixel((412, 309), (52, 146, 235, 123))
bypass_image.putpixel((12, 209), (42, 16, 125, 231))
bypass_image.putpixel((264, 143), (122, 136, 25, 213))

# Save the bypass image
bypass_image.save('bypass_image.png')

# Set metadata using ExifTool
import subprocess

metadata_commands = [
    'exiftool', '-PNG:Description=jctf{not_the_flag}',
    '-PNG:Title=kool_pic', '-PNG:Author=anon', 'bypass_image.png'
]

subprocess.run(metadata_commands)

print("Bypass image created and metadata set.")

```

Upload tấm ảnh đó lên là lấy được flag

<figure><img src=".gitbook/assets/image (69).png" alt=""><figcaption></figcaption></figure>

