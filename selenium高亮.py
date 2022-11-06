from selenium import webdriver
from time import sleep

def find(driver,by,loc):
    '''by代表定位方式，loc代表元素定位表达式'''
    STYLE = "background: yellow; border: 2px solid red;"  # 高亮的样式
    element = driver.find_element(by,loc)
    driver.execute_script("arguments[0].setAttribute('style', arguments[1]);",element, STYLE)
    return element


driver = webdriver.Chrome()
driver.get("https://www.baidu.com/")

find(driver,"id","kw").send_keys("python")
sleep(3)
find(driver,"id","su").click()
sleep(3)

driver.quit()