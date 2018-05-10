from bs4 import BeautifulSoup
import requests

'''
url='https://www.tripadvisor.cn/Attractions-g60763-Activities-New_York_City_New_York.html'
wb_data = requests.get(url)
soup = BeautifulSoup(wb_data.text,'lxml')
titles = soup.select('div.item.name > a')
imags = soup.select('img[width="200"]')
cates = soup.select('#taplc_attraction_coverpage_attraction_0 > div > div > div > div.shelf_item_container > div > div.poi > div > div')

for title, imag, cate in zip(titles, imags, cates):
    data = {
        'title':title.get_text(),
        'imag':imag.get('src'),
        'cate':list(cate.stripped_strings),
    }
    print(data)
'''

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    'Cookie':'ServerPool=X; TATravelInfo=V2*A.2*MG.-1*HP.2*FL.3*RS.1; TART=%1%enc%3Az9JzCrbnDyGPNeebddVSQEa2pVJ%2BPF%2F3mZqJ0nwboF6vtC%2BwrP8qa70u1dPAvkXa0zjAP28rOIQ%3D; TAUnique=%1%enc%3ARu4i8UpMjcZkeG4sdujnXR%2Fmlx%2FvR3EZ9nrtMlB%2BEqriJ6g91gwMNg%3D%3D; TASSK=enc%3AAEPUeOhB6mCglIN%2F2QguT4yNxuTmKJE%2Ba1y2irAHypFbgZKg9Aom1crsN4GuuxazzVqf3%2BAgsnSo4F1V6O3ASLZqjzQi27wF1dUi9JTe6vlf2enydlUhOvQYwZlQXsrwBQ%3D%3D; VRMCID=%1%V1*id.16631*llp.%2F-a_ttcampaign%5C.MTYpc-a_ttgroup%5C.title-m16631*e.1526012914751; _smt_uid=5aebe17b.30efc005; CommercePopunder=SuppressAll*1525408222961; SecureLogin2=3.4%3AAM65sUNSqpYt3yw1%2Fr4JJbvb4sfHAytg6MxiMSkORip0W%2FVO7PqvRtUhwBbLXA9Ir1iMLkMDVIRK7iUHaHfMB1DeL0L5kuNNb%2BA0bkRWprharUIMysmHArdNhsokj3K1jdYAQdKa0i4Dg6yLUWwAGxHpPmDzb%2FAqneHyElQLZQ3Qb61TSQC2Fjs9y9Mj4FMUrxF2v74pnBySfOlXYzEYqic%3D; TAAuth3=3%3A6c96235a410de45b7cc6aa924f00334a%3AAFTRf5Nt4NCxMhInvfu7CgwMeU%2FwBp7YCo95pjb5HGWsDy1MS21B9WOzv0wbtYBotJn%2BPTEsZeHMAePlA%2F9GFQRh551oXFfp8Shus9NWjpjLdlLOqExGUoTytCBFrnPuvTyJBq8BzjiYBaBc16H7%2FjPQm87eJ5IA8woh6R9dMV3FJTmz39i7TQiOdgx8UcLDQg%3D%3D; CM=%1%PremiumMobSess%2C%2C-1%7Ct4b-pc%2C%2C-1%7CSPHRSess%2C%2C-1%7CRestAds%2FRPers%2C%2C-1%7CRCPers%2C%2C-1%7CWShadeSeen%2C%2C-1%7CTheForkMCCPers%2C%2C-1%7CHomeASess%2C2%2C-1%7CPremiumSURPers%2C%2C-1%7CPremiumMCSess%2C%2C-1%7CRestPartSess%2C%2C-1%7CRestPremRSess%2C%2C-1%7CCCSess%2C%2C-1%7CPremRetPers%2C%2C-1%7CViatorMCPers%2C%2C-1%7Csesssticker%2C%2C-1%7Ct4b-sc%2C%2C-1%7CRestAdsPers%2C%2C-1%7CMC_IB_UPSELL_IB_LOGOS2%2C%2C-1%7Cb2bmcpers%2C%2C-1%7CMC_IB_UPSELL_IB_LOGOS%2C%2C-1%7CPremMCBtmSess%2C%2C-1%7CPremiumSURSess%2C%2C-1%7CLaFourchette+Banners%2C%2C-1%7Csess_rev%2C%2C-1%7Csessamex%2C%2C-1%7CPremiumRRSess%2C%2C-1%7CSPMCSess%2C%2C-1%7CTheForkORSess%2C%2C-1%7CTheForkRRSess%2C%2C-1%7Cpers_rev%2C%2C-1%7CRBAPers%2C%2C-1%7CRestAds%2FRSess%2C%2C-1%7CHomeAPers%2C%2C-1%7CPremiumMobPers%2C%2C-1%7CSPHRPers%2C%2C-1%7CRCSess%2C%2C-1%7CLaFourchette+MC+Banners%2C%2C-1%7CRestAdsCCSess%2C%2C-1%7CRestPartPers%2C%2C-1%7CRestPremRPers%2C%2C-1%7Csh%2C%2C-1%7Cpssamex%2C%2C-1%7CTheForkMCCSess%2C%2C-1%7CCCPers%2C%2C-1%7Cb2bmcsess%2C%2C-1%7CSPMCPers%2C%2C-1%7CPremRetSess%2C%2C-1%7CViatorMCSess%2C%2C-1%7CPremiumMCPers%2C%2C-1%7CPremiumRRPers%2C%2C-1%7CRestAdsCCPers%2C%2C-1%7CTheForkORPers%2C%2C-1%7CPremMCBtmPers%2C%2C-1%7CTheForkRRPers%2C%2C-1%7CRestAdsSess%2C%2C-1%7CRBASess%2C%2C-1%7CSPORPers%2C%2C-1%7Cperssticker%2C%2C-1%7C; TAReturnTo=%1%%2FAttraction_Review-g60763-d105125-Reviews-The_Metropolitan_Museum_of_Art-New_York_City_New_York.html; roybatty=TNI1625!AL%2F9bSukB6ANSq%2FlKFo7IVxii8%2F9PQZ0Y7jGCHA7gZlh5ss%2Bj4LBNNiP4S%2ByOuKFuINfV0CrrJQdY2vWxPhmcl7T%2Byt7iIzTSph%2F4WHhK1qxmOhDwDZcoJgDIwWempvLmCAacagptriSsiMxUs1dXJrsjQa8pzJzCf1mqWeg6ufO%2C1; _ga=GA1.2.399977611.1525408121; _gid=GA1.2.2051740697.1525408121; ki_t=1525408134998%3B1525408134998%3B1525412055263%3B1%3B11; ki_r=; TASession=%1%V2ID.312A4659B73FEFBA78E620A75125231D*SQ.55*MC.16631*LP.%2F-a_ttcampaign%5C.MTYpc-a_ttgroup%5C.title-m16631*PR.427%7C*LS.DemandLoadAjax*GR.22*TCPAR.26*TBR.74*EXEX.19*ABTR.50*PHTB.14*FS.58*CPU.51*HS.recommended*ES.popularity*AS.popularity*DS.5*SAS.popularity*FPS.oldFirst*TS.AC8C9C41241E9051824B8F62C0EE11CD*LF.zhCN*FA.1*DF.0*IR.3*OD.zh*MS.-1*RMS.-1*FLO.60763*TRA.true*LD.105125; TAUD=LA-1525408114737-1*RDD-1-2018_05_04*LG-3938212-2.1.F.*LD-3938213-.....'
    }

url_saves = 'https://www.tripadvisor.cn/Saves/1133355'
wb_data = requests.get(url_saves, headers=headers)
soup = BeautifulSoup(wb_data.text, 'lxml')
titles = soup.select('#trip-item-collection-container > div:nth-of-type(1) > div > div.saves-location-details.ui_media > div.media-content > div > div.location_parent')
imags = soup.select('#trip-item-collection-container > div:nth-child(1) > div > div.saves-location-details.ui_media > div.media-left > a')
metas = soup.select('div.poi_type_tags')

print(titles, imags, metas)
'''

for title, imag, meta in zip(titles, imags, metas):
    data = {
        'title':title.get_text(),
        'imag':imag.get('src'),
        "meta":list(meta.stripped_strings),
    }
    print(data)
'''