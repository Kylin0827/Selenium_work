from selenium import webdriver

driver = webdriver.Chrome()

#访问百度音乐，找出排名上升的歌曲
driver.get('http://music.taihe.com/top/new')

#确定目标元素
# ele=driver.find_element_by_id('songListWrapper')
# lis=ele.find_elements_by_tag_name('li')
lis=driver.find_elements_by_css_selector('#songListWrapper li')
# print(len(lis))
# iss=ele.find_elements_by_tag_name('i')
# print(len(iss))
for li in lis:
    i=li.find_element_by_tag_name('i')
    if i.get_attribute('class')=='up':
    #如果是我们就把歌曲信息打印出来
        songtitle=li.find_element_by_class_name('song-title ').text
        singer=li.find_element_by_class_name('singer').text

    #并且打印出歌曲名和歌手
        print(f'{songtitle}\t:{singer}')


driver.quit()