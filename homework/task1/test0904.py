from selenium import webdriver

#先获取数据
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()

driver.get('http://www.weather.com.cn/html/province/jiangsu.shtml')

#ele=driver.find_element_by_id('forecastID')
ele=driver.find_element('id','forecastID')
#print(ele.text)
tmp_msg=ele.text

driver.quit()

cityWeather=tmp_msg.split('℃\n')
#根据获取数据做进一步分析

#南京
#22℃/27

#循环遍历城市温度，把城市和最低温度取出来
#依次比较当前的最低温度，如果发现更低的温度，就进行替换，并且替换城市名称
lowest=''
lowestcity=[]

for one in cityWeather:
    one=one.replace('℃','')
    tmp=one.split('\n')
    cityname=tmp[0]
    print(tmp[1].split('/'))
    lowweather=min(tmp[1].split('/'))

    #当前温度小于最低温度
    if lowest=='' or lowest>lowweather:
        lowest=lowweather
        lowestcity=[cityname]
    #最低温度相等
    elif lowest==lowweather:
        lowestcity.append(cityname)

print(f'最低温度的城市有：{lowestcity}温度为：{lowest} °C')