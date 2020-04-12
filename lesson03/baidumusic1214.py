from selenium import webdriver

driver = webdriver.Chrome()

#访问百度音乐，找出排名上升的歌曲
driver.get('http://music.taihe.com/top/new')

#处理弹窗
# eles=driver.find_elements_by_XXXX()#利用复数形式查找元素
# if eles:
#     eles[0].click()



#找到包含所有歌曲的元素
# ele=driver.find_element_by_id('songListWrapper')
# lis=ele.find_elements_by_tag_name('li')
#通过css找到所有的Li元素
lis=driver.find_elements_by_css_selector('#songListWrapper li')

for li  in lis:
    #找到i元素取class属性
    # class_value=li.find_element_by_class_name('status').find_element_by_tag_name('i').get_attribute('class')

    class_value=li.find_element_by_css_selector('.status i').get_attribute('class')

    if class_value=='up':
        song_title=li.find_element_by_class_name('song-title').text
        singer=li.find_element_by_class_name('singer').text
        print(f'{singer}:{song_title}')

driver.quit()