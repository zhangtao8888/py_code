import  urllib.request

url = "http://www.baidu.com"
response = urllib.request.urlopen(url)
print(response.getcode())
print(response.geturl())
print(response.getheaders())