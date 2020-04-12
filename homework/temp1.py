
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(r"d:\tools\webdrivers\chromedriver.exe")
driver.get('http://www.weather.com.cn/html/province/jiangsu.shtml')


forecast=driver.find_element_by_id('forecastID')
content=forecast.text

citysWeather = content.split('℃\n')

# print(citysWeather)

lowest  =  None
lowestCitys= []
for one in citysWeather:
    city=one.split('\n')[0]
    temps=one.split('\n')[1].split('℃/')
    # print(temps)
    low_temp=min([int(t.replace('℃','')) for t in temps])
    # print(low_temp)
    if lowest==None or lowest>low_temp:
        lowest=low_temp
        lowestCitys=[city]
    elif lowest==low_temp:
        lowestCitys.append(city)


print(f'最低温度城市有{lowestCitys}，最低温度为{lowest}')





driver.quit()