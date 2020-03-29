from selenium import webdriver
driver=webdriver.Chrome(r'D:\chromedriver\chromedriver.exe')
driver.implicitly_wait(10)
driver.get('https://m.weibo.cn/')
driver.maximize_window()
driver.find_element_by_css_selector('div.m-text-cut').click()
hot=driver.find_element_by_class_name('card.m-panel.card16.m-col-2')
# 微博热搜榜
hot.find_elements_by_class_name('m-item-box')[-1].click()
# 热搜
hot_search=driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[1]/div[2]')
hot_search_line=hot_search.find_elements_by_class_name('card.m-panel.card4')
for one in hot_search_line:
    icon=one.find_elements_by_class_name('m-link-icon')
    if icon:
        info = one.find_element_by_class_name('main-text.m-text-cut').text
        type=icon[0].find_element_by_tag_name('img').get_attribute('src')
        if 'hot'in type:
            print(f'热:{info}')
        elif 'new' in type:
            print(f'新:{info}')
        elif 'fei' in type:
            print(f'沸:{info}')

driver.quit()