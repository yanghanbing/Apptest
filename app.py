from time import strftime, localtime
from time import sleep
from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from appium.webdriver.common.touch_action import TouchAction
time=strftime('%y%m%d%H%M%S',localtime())
phone={
    'appPackage':'com.coolapk.market',
    'appActivity':'.view.main.MainActivity',
    'noReset':True,
    'platformName':'Android',
    'platformVersion':'11',
    'deviceName':'xiaomi',
    'automationName':'UIAutomator2',
    "autoAcceptAlerts": True
}
driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub',phone)
#点击元素
driver.find_element('xpath','//*[@text="关注"]').click()
driver.find_element('id','com.coolapk.market:id/bottom_navigation_item_title').click()
driver.find_element('id','com.coolapk.market:id/post_button').click()
sleep(3)
driver.find_element('id','com.coolapk.market:id/item_view_1').click()
#输入内容
#driver.find_element('id','com.coolapk.market:id/edit_text').clear()
sleep(3)
driver.find_element('id','com.coolapk.market:id/edit_text').send_keys('这是一条自动化动态')

#点击
driver.find_element('id','com.coolapk.market:id/image_view').click()
#滑动
driver.swipe(start_x=780,start_y=500,end_x=780,end_y=1030,duration=500)
#点击图片坐标
driver.tap([(1000,700)],200)
#点击确认
sleep(3)
driver.find_elements_by_class_name('android.widget.ImageView')[2].click()
#文本定位
driver.find_element_by_android_uiautomator('new UiSelector().text("确定")').click()
#driver.find_element('id','com.coolapk.market:id/close_view').click()
#点击发布
driver.find_element('id','com.coolapk.market:id/submit_view').click()
sleep(3)
#动态等待
WebDriverWait(driver,15).until(expected_conditions.presence_of_element_located(('id','com.coolapk.market:id/bottom_navigation_item_title')))
driver.find_element_by_android_uiautomator('new UiSelector().text("我")').click()
sleep(3)
text=driver.find_element('id','com.coolapk.market:id/text1').text
print(text)
assert text == '20'
#截图
#driver.save_screenshot(r'C:\Users\Administrator\Desktop\截图'+time+'.png')
driver.get_screenshot_as_file(r'C:\Users\Administrator\Desktop\截图'+time+'.png')