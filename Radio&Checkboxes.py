from selenium import webdriver
import time


driver=webdriver.Chrome(executable_path="C:\\Users\\MANIKANTA\\Downloads\\new\\chromedriver_win32 (2)\\chromedriver.exe")
driver.get("https://opensource-demo.orangehrmlive.com/")

driver.find_element_by_id("txtUsername").send_keys("Admin")
driver.find_element_by_id("txtPassword").send_keys("admin123")
driver.find_element_by_class_name("button").click()
driver.maximize_window()
driver.find_element_by_xpath("//*[@id='menu_admin_viewAdminModule']/b").click()
driver.find_element_by_id("menu_admin_Job").click()
driver.find_element_by_id("menu_admin_employmentStatus").click()
driver.find_element_by_name("btnAdd").click()
driver.find_element_by_id("empStatus_name").send_keys("Manikanta")
driver.find_element_by_id("btnSave").click()
driver.save_screenshot("C:\\Users\\MANIKANTA\\Pictures\\ScreenShots\\mom.jpg")
driver.find_element_by_id("ohrmList_chkSelectRecord_4").click()
driver.find_element_by_id("btnDelete").click()
driver.save_screenshot("C:\\Users\\MANIKANTA\\Pictures\\ScreenShots\\popup.jpg")

# Radio buttons:

driver.get("http://test.rubywatir.com/")
time.sleep(3)
driver.find_element_by_xpath("//*[@id='recent4']/ul/li[3]/a").click()
time.sleep(2)
driver.find_element_by_xpath("//*[@id='content']/div/div/div[2]/p/input[4]").click()

#to check wheather option we selected is happened or not
can=driver.find_element_by_xpath("//*[@id='content']/div/div/div[2]/p/input[4]").is_enabled()
print(can)

# Checkboxes:

driver.get("http://test.rubywatir.com/")
time.sleep(3)
driver.find_element_by_xpath("//*[@id='recent4']/ul/li[2]/a").click()
driver.find_element_by_xpath("//*[@id='content']/div/div/div[2]/form/input[3]").click()

#to check wheather option we selected is happened or not

yes=driver.find_element_by_xpath("//*[@id='content']/div/div/div[2]/form/input[3]").is_enabled()
print(yes)




