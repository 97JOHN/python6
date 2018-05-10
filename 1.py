from bs4 import BeautifulSoup
with open('C:/Users/asus\Desktop/index.html', 'r')as wb_data:
    Soup = BeautifulSoup(wb_data, 'lxml')
    print(Soup)