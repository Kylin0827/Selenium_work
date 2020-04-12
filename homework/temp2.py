
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(r"d:\tools\webdrivers\chromedriver.exe")
driver.get('http://www.weather.com.cn/html/province/jiangsu.shtml')


forecast=driver.find_element_by_id('forecastID')
content=forecast.get_attribute('outerHTML')
# print(content)

from bs4 import BeautifulSoup

soup=BeautifulSoup(content,'html5lib')
dls=soup.find_all('dl')

lowest  =  None
lowestCitys= []

for dl in dls:
    city=dl.dt.a.string
    temp1=dl.dd.span.string.replace('℃','')
    temp2 = dl.dd.b.string.replace('℃','')
    low_temp=min(int(temp1),int(temp2))
    print(city,low_temp)
    #如果最低温度没有设置，或者当前温度小于最低温度，就把最低温度替换成当前温度
    if lowest==None or lowest>low_temp:
        lowest=low_temp
        lowestCitys=[city]
    #如果最低温度等于当前温度，只需要添加城市即可
    elif lowest==low_temp:
        lowestCitys.append(city)

print(f'最低温度城市有{lowestCitys}，最低温度为{lowest}')





driver.quit()