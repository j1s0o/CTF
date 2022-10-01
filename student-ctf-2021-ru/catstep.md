# CatStep

Brute force to server

```python
import requests
import string
url = "https://cat-step.disasm.me"
char = string.ascii_lowercase +'_0123456789' + string.ascii_uppercase   
session = requests.session()
data_1 = "///////////////////////////"
result = ""
start = 0
end = 1
stop = 0
st = 10
en = 12
    
for i in char:
    print(i)
    r = session.post(url , data = {"flag" : 'spbctf{' + i + data_1 + '}' })
    r1 = int(r.text[st:en])
    if r1 == 27:
        result += i
        print(result , r.text)
        data_1 = data_1.replace('/' , '' , 1)
        cc = 26
        while stop < 27:            
            for j in char:
                print(result , j , data_1)
                r = session.post(url , data = {"flag" : 'spbctf{' + result + j + data_1 + '}' })
                r2 = int(r.text[st:en])
                if r2 == cc and cc > 10:
                    cc = cc-1
                    print(cc)
                    data_1 = data_1.replace('/' , '' , 1)
                    result += j
                    stop = len(result)
                    print ('flag' , result , r.text)
                    break
                if r2 == cc and cc <= 10:
                    data_1 = data_1.replace('/' , '' , 1)
                    st = 10
                    en = 11
                    cc -=1
                    result += j
                    stop = len(result)
                    print ('flag' , result)
                    break
                
                

print ('spbctf{' , result  , '}')

```

