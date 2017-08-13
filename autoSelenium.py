# python+selenium 自动化
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import time
import os

# 打开浏览器
browser = webdriver.Ie()
# 打开网址
browser.get('http://192.168.0.123/')
# 等待1s加载元素
time.sleep(1)
# 找到元素
UserName = browser.find_element_by_id("loginUserName") 
# 模拟输入
UserName.send_keys(u"admin")  
# 找到元素
PassWord = browser.find_element_by_id("loginPassword")
# 模拟输入
PassWord.send_keys(u"12345678q")  
# 找到登陆按钮
Btn = browser.find_element_by_class_name("loginbtn")
# 模拟点击事件
Btn.click()
# 等待2s加载元素
time.sleep(2)
# 获取窗体句柄
# browser.switch_to_window(browser.window_handles[1])
# 进入iframe
browser.switch_to.frame("ContentFrame")
# 找到iframe内的元素并点击
browser.find_element_by_id("play").click()
browser.find_element_by_id("fullscreen").click()
# 关闭
os.system('taskkill /F /IM IEDriverServer.exe')
# 输出
# print (browser.title)

# 找到元素
# WebDriverWait(browser,timeout=10).until(EC.presence_of_element_located((By.ID,'email')),message=u'元素加载超时!')

# wd.find_element_by_id("login").click() #点击登录
# 
# try:
# except NoSuchElementException as e:
    # print e.message