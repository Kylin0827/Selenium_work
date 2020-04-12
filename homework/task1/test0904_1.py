from selenium import webdriver

#先获取数据
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()

driver.get('http://www.weather.com.cn/html/province/jiangsu.shtml')

#ele=driver.find_element_by_id('forecastID')
ele=driver.find_element('id','forecastID')
#print(ele.text)
from bs4 import BeautifulSoup

tmp_msg=ele.get_attribute('outerHTML')
driver.quit()

# print(tmp_msg)
soup=BeautifulSoup(tmp_msg,'html5lib')



cityWeather=soup.find_all('dl')
#根据获取数据做进一步分析

#南京
#22℃/27

#循环遍历城市温度，把城市和最低温度取出来
#依次比较当前的最低温度，如果发现更低的温度，就进行替换，并且替换城市名称
lowest=''
lowestcity=[]

for dl in cityWeather:

    # one=one.replace('℃','')
    # tmp=one.split('\n')
    cityname=dl.dt.a.string
    tmp1=dl.dd.find_all('a')[1].span.string
    tmp2=dl.dd.find_all('a')[2].b.string
    lowweather=min(tmp1,tmp2)

    #当前温度小于最低温度
    if lowest=='' or lowest>lowweather:
        lowest=lowweather
        lowestcity=[cityname]
    #最低温度相等
    elif lowest==lowweather:
        lowestcity.append(cityname)

print(f'最低温度的城市有：{lowestcity}温度为：{lowest} ')
