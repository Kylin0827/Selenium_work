from selenium import webdriver
import time

driver = webdriver.Chrome(r"d:\tools\webdrivers\chromedriver.exe")

driver.get('http://www.weather.com.cn/html/province/jiangsu.shtml')

#获取最高和最低气温

forecastBox=driver.find_element_by_id('forecastID')

dls=forecastBox.find_elements_by_tag_name('dl')
#最低温度城市列表
lowtemp_cities=[]
lowtemp=None
for dl in dls:
    tmp=dl.text.split('\n')
    city=tmp[0]
    min_temp=min(int(t.replace('℃','')) for t in tmp[1].split('/'))
    # city=dl.find_element_by_tag_name('dt').text
    # span=dl.find_element_by_tag_name('dd').find_element_by_tag_name('span').text
    # b=dl.find_element_by_tag_name('dd').find_element_by_tag_name('b').text
    #
    # min_temp=min(int(span.replace('℃','')),int(b.replace('℃','')))

    if lowtemp==None or lowtemp>min_temp:#如果最低温度没有取或者已经获取的最低温度小于当前城市最低温度，就进行替换
        lowtemp_cities=[city]
        lowtemp=min_temp

    elif lowtemp==min_temp :#如果最低温度相同
        lowtemp_cities.append(city)

print(f'最低温度的城市是{lowtemp_cities}温度为{lowtemp}℃')








driver.quit()