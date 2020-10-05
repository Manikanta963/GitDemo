from selenium import webdriver
from selenium.webdriver import ActionChains
import time

driver=webdriver.Chrome(executable_path="C:\\Users\\MANIKANTA\\Downloads\\new\\chromedriver_win32 (2)\\chromedriver.exe")
driver.get("http://demo.automationtesting.in/Register.html")

m=driver.find_element_by_xpath("//*[@id='header']/nav/div/div[2]/ul/li[6]/a")
a=driver.find_element_by_xpath("//*[@id='header']/nav/div/div[2]/ul/li[6]/ul/li[1]/a")
v=ActionChains(driver)

v.move_to_element(m).move_to_element(a).perform()

driver.find_element_by_xpath("//*[@id='header']/nav/div/div[2]/ul/li[6]/ul/li[1]/ul/li[1]/a").click()
print(driver.current_url)
driver.maximize_window()
time.sleep(2)


#drag and drop:

source=driver.find_element_by_id("angular")
target=driver.find_element_by_id("droparea")

a=ActionChains(driver)
a.drag_and_drop(source,target).click().perform()
