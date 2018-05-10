import urllib.request
r= urllib.request.urlopen('https://www.hao123.com/')
html=r.read()
print(html)


#urllib在python3中已经替换为 urllib.request
#import urllib 转化为 import urllib.request
# urllib.urlopen转化为 urllib.request.urlopen