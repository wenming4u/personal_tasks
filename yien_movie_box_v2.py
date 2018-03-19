# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 10:32:13 2018

@author: wenming.guo
"""


__author__ = 'William'
__date__ = '2018/3/17 15:12'


from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import datetime


text_file = 'D:\work\综合\城市\city_box{0}{1}.txt'.format(datetime.datetime.now().month,datetime.datetime.now().day)

city_id_list = open('D:\work\综合\城市\city_list.txt','r').readlines()


def parse(mydriver,city_name,n):
    city_name=city_name
    n=n
    box_office_strong = mydriver.find_element_by_xpath('//*[@id="Info_SummaryNum"]/strong').text
    box_office_sub = mydriver.find_element_by_xpath('//*[@id="Info_SummaryNum"]/sub').text
    city_list = city_name + '\t'+ str(n) + '\t' + str(box_office_strong) + '\t' + box_office_sub
    print (city_list)
    f = open(text_file,'a')
    f.write(city_list)
    f.write("\n")
    f.close()

mydriver = webdriver.Chrome(executable_path="D:\ProgramData\Anaconda3\webdriver\chromedriver.exe")

# mydriver.quit()

mydriver.get('http://ebotapp.entgroup.cn/Browser')
mydriver.maximize_window()
mydriver.switch_to.frame('iframeBrowser')


# entry_1=mydriver.find_element_by_xpath('//*[@id="SwiperWarp"]/div[2]/span[last()]')

entry_1=mydriver.find_element_by_xpath("//*[@id='SwiperWarp']/div[2]/span[@class='swiper-pagination-bullet'][4]")
# ActionChains(webdriver).click(on_element=entry_1).perform()
entry_1.click()
time.sleep(1)
# entry_2=mydriver.find_element_by_xpath("//*[@id='begin_Btn']/span[contains(text(),'swiper-pagination-bullet swiper-pagination-bullet-active')]")
entry_2=mydriver.find_element_by_xpath("//*[@id='begin_Btn']/span[text()='V2.0 温暖来袭']")
# entry_2=mydriver.find_element_by_xpath("//*[@class='login-btn download-btn download-btn-up']/span[1]")
entry_2.click()
time.sleep(5)

# 选日期
entry_3=mydriver.find_element_by_xpath('//*[@id="selDate_Btn"]/label/span')
entry_3.click()
time.sleep(1)
entry_4=mydriver.find_element_by_xpath('//*[@id="selDate_Menu"]/li[3]/span')
entry_4.click()
time.sleep(1)
entry_5=mydriver.find_element_by_xpath('//*[@id="scroll_ListMonth"]/dl/dd[3]')
entry_5.click()
time.sleep(5)

# 选指标
entry_6=mydriver.find_element_by_xpath('//*[@id="selIndex_Btn"]')
entry_6.click()
time.sleep(1)
entry_7=mydriver.find_element_by_xpath('//*[@id="selFilmIndex_List_Movie_Index_Month_"]/div/ul/li[4]/span')
entry_7.click()
time.sleep(1)
entry_8=mydriver.find_element_by_xpath('//*[@id="selFilmIndex_YesBtn"]')
entry_8.click()
time.sleep(5)

# 选城市
city_selector=mydriver.find_element_by_xpath('//*[@id="selOption_Btn"]/label/span')
city_selector.click()
time.sleep(1)
    
n=0
#all_city = '//ul[@data-tag = "city"]/li[@data-tag = "{0}"]/span[1]'.format(1)


for i in city_id_list:
    by_city=mydriver.find_element_by_xpath('//*[@id="selFilmOption_Menu"]/li[2]/span')
    by_city.click()
    time.sleep(1)

    selector = '//ul[@data-tag = "city"]/li[@data-tag = "{0}"]/span'.format(i.strip())
    try:
        city_list=mydriver.find_element_by_xpath(xpath=selector)
        city_list.click()
        time.sleep(0.5)
        city_name = city_list.text
        print (city_name)
        city_list_confirm=mydriver.find_element_by_xpath('//*[@id="selFilmOption_YesBtn"]/span')
        city_list_confirm.click()
        time.sleep(2)
        parse(mydriver,city_name,i)
    except Exception as e:
        print (e)
        go_back=mydriver.find_element_by_xpath('//*[@id="selFilmOption_OutBtn"]/i')
        go_back.click()
        time.sleep(1)
        continue
    city_selector=mydriver.find_element_by_xpath('//*[@id="selOption_Btn"]/label/span')
    city_selector.click()
    time.sleep(1)

