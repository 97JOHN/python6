import re
import sys
import urllib.request
import urllib
import os
import importlib



importlib.reload(sys)
#sys.setdefaultencoding("utf-8")

#a = 1
url_name = []
def get(pageindex):
    url = 'http://www.budejie.com/video/' + str(pageindex)
    # var1.set('已经获取到第%s页的视频视频'%(a))
    print(url)
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
    req = urllib.request.Request(url=url, headers=headers)
    html = urllib.request.urlopen(req).read()  #urllib.urlopen() 要改成 urllib.request.urlopen
    url_reg = r'data-mp4="(.*?)"'
    html = html.decode('utf-8')  # python3 ##python版本的原因，要加这句话
    url_items = re.findall(url_reg, html)
    name_reg = re.compile('<div class="j-r-list-c-desc".*?<a href=".*?>(.*?)</a>.*?</div>', re.S)

    name_items = re.findall(name_reg, html)
    for i, k in zip(name_items, url_items):
        url_name.append([i, k])

#传入文件名和video地址
def saveVideo(filename,videoUrl):
    print ('Saving : %s ...'%filename)
    urllib.urlretrieve(videoUrl,'D:\\video\\%s.mp4'%filename)


####main exec ####
for pageindex in range(1,3):
    get(pageindex)

for index,item in enumerate(url_name):
    saveVideo(index,item[1])