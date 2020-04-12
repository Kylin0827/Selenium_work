from selenium import webdriver
import time


def get_weathermsg():
    driver = webdriver.Chrome(r"d:\tools\webdrivers\chromedriver.exe")

    driver.get('http://www.weather.com.cn/html/province/jiangsu.shtml')

    #取出所有城市的天气信息
    forecaset=driver.find_element_by_id('forecastID')
    print(forecaset.text)

    #加回车符方便下面切割结果一致
    forecaset1=forecaset.text+'\n'
    #再分析最低温度的城市有哪些
    #分离城市和温度信息
    weather_msg=forecaset1.split('℃\n')
    driver.quit()
    return weather_msg

def get_lowsetemp(weather_msg):
    lowset_temp=None
    cities=[]

    for msg in weather_msg[:-1]:
        city_name=msg.split('\n')[0]
        temp=msg.split('\n')[1]
        low_temp=min([int(one) for one in temp.split('℃/')])
        print(low_temp)

        #当前低温小于已经获取的最低温度 或者 第一次还没有获取最低温度
        if lowset_temp==None or low_temp<lowset_temp:
            lowset_temp=low_temp
            cities=[city_name]
        elif low_temp==lowset_temp:
            cities.append(city_name)

    print(f'最低温度是{lowset_temp}℃,城市有{"，".join(cities)}')


if __name__ == '__main__':
    weather_msg=get_weathermsg()
    get_lowsetemp(weather_msg)


