from selenium import webdriver
from selenium.webdriver.support.ui import Select


driver=webdriver.Chrome(executable_path="C:\\Users\\MANIKANTA\\Downloads\\new\\chromedriver_win32 (2)\\chromedriver.exe")
driver.get("http://demo.automationtesting.in/Register.html")


mani=driver.find_element_by_id("Skills")
k=Select(mani)

# k.select_by_visible_text('CSS')
k.select_by_index('16')
driver.maximize_window()
print(len(k.options))
s=k.options
for v in s:
    print(v.text)
print(driver.current_url)
driver.quit()