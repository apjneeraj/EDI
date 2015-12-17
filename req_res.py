import requests, bs4

def AmazonPrice(ProdcutUrl):
    res=requests.get(ProdcutUrl)
    res.raise_for_status()
    #print(res.text[:100])
    soup=bs4.BeautifulSoup(res.text,'html.parser')

    price=soup.select('#block-system-main > div > div > div > div > div > div.field.field-name-field--rank-1.field-type-asin.field-label-above > div.field-items > div > div > b:nth-of-type(3)')
    #return price
    return price[0].text.strip()


#print(res.text)



'''
bestofFive=open("bestofFive",'wb')
for chunk in res.iter_content(1000):
    bestofFive.write(chunk)

bestofFive.close()
'''

price=AmazonPrice("http://www.best5list.com/best-hd-camcorders-under-200")
print('price of item is %s' %(price))

