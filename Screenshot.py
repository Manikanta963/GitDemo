from selenium import webdriver
import time

driver=webdriver.Chrome(executable_path="C:\\Users\\MANIKANTA\\Downloads\\new\\chromedriver_win32 (2)\\chromedriver.exe")
driver.get("https://www.google.com/")
driver.maximize_window()
# driver.save_screenshot("C:\\Users\\MANIKANTA\\Pictures\\ScreenShots\\mani.jpg")
driver.get_screenshot_as_file("C:\\Users\\MANIKANTA\\Pictures\\ScreenShots\\man.png")
time.sleep(3)

driver.close()


