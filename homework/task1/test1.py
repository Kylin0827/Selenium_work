from selenium import webdriver

driver=webdriver.Chrome()

driver.get('http://www.weather.com.cn/html/province/jiangsu.shtml')

ele=driver.find_element_by_id('forecastID')

city_temps=ele.text.split('℃\n')

lowest=None
lowest_city=[]
for temp in city_temps:
    temp=temp.replace('℃','')
    # print(temp)
    #城市名
    city_name= temp.split('\n')[0]
    #温度
    weather=temp.split('\n')[1]
    #低温
    lowtemp=min([int(one) for one in weather.split('/')])

    if lowest==None or lowtemp<lowest:
        lowest=lowtemp
        lowest_city=[city_name]
    elif lowest==lowtemp:
        lowest_city.append(city_name)



print(f'温度最低的城市有{" ".join(lowest_city)}，是{lowest}度')




driver.quit()