from selenium import webdriver

driver=webdriver.Chrome()

driver.get('http://www.weather.com.cn/html/province/jiangsu.shtml')

ele=driver.find_element_by_id('forecastID')

city_temps=ele.get_attribute('innerHTML')

from bs4 import BeautifulSoup
soup=BeautifulSoup(city_temps,'html5lib')

dls=soup.find_all('dl')

lowest=None
lowest_city=[]
for dl in dls:

    city_name=dl.dt.a.string
    t1=dl.span.string
    t2=dl.b.string
    lowtemp=min(t1,t2)

    if lowest==None or lowtemp<lowest:
        lowest=lowtemp
        lowest_city=[city_name]
    elif lowest==lowtemp:
        lowest_city.append(city_name)


print(f'温度最低的城市有{" ".join(lowest_city)}，是{lowest}度')




driver.quit()