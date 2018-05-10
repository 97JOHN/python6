from bs4 import BeautifulSoup
with open('C:/Users/asus\Desktop/new_index.html', 'r')as wb_data:
    Soup = BeautifulSoup(wb_data, 'lxml')
    images = Soup.select('body > div.main-content > ul > li > img')
    titles = Soup.select('body > div.main-content > ul > li > div.article-info > h3 > a')
    descs = Soup.select('body > div.main-content > ul > li > div.article-info > p.description')
    rates = Soup.select('body > div.main-content > ul > li > div.rate > span')
    cates = Soup.select('body > div.main-content > ul > li > div.article-info > p.meta-info > span')
for title, image, desc, rate, cate in zip(titles, images, descs, rates, cates):
    data={
        'title':title.get_text(),
        'rate' :rate.get_text(),
        'desc' :desc.get_text(),
        'cate' :list(cate.stripped_strings),
        'image':image.get('src')
    }


for i in data:
    if float(i['rate'])>3:
        print(i['title'],i['cate'])

 #   print(title.get_text())


'''
body > div.main-content > ul > li:nth-child(1) > div.article-info > h3 > a
body > div.main-content > ul > li:nth-child(1) > div.article-info > p.meta-info > span:nth-child(2)
body > div.main-content > ul > li:nth-child(1) > div.article-info > p.description
body > div.main-content > ul > li:nth-child(1) > div.rate > span
body > div.main-content > ul > li:nth-child(1) > img
'''