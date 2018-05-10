from bs4 import BeautifulSoup
with open('D:\新建文件夹\新建文件夹\Python实战：四周实现爬虫系统\课程资料\Plan-for-combating-master\week1\1_2\1_2code_of_video\web/new_index.html','r')as wb_data:
    Soup=BeautifulSoup(web_data,'lxml')
    print(Soup)