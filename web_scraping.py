from selenium import webdriver
from bs4 import BeautifulSoup
import time

#url = "https://www.flipkart.com"
#browser(url)
#print(browser)

driver = webdriver.Chrome(r"C:\Users\HP\Downloads\chromedriver_win32 (2)\chromedriver.exe")
driver.get("https://www.flipkart.com")
time.sleep(3)
driver.maximize_window()
window_before = driver.window_handles[0]

time.sleep(2)
driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[2]/div/form/div[1]/input').send_keys('sweetybiswas2927@gmail.com')
time.sleep(2)
driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[2]/div/form/div[2]/input').send_keys('sweety110')
time.sleep(2)

driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[2]/div/form/div[4]/button').click()



time.sleep(3)
driver.find_element_by_xpath('//*[@id="container"]/div/div[1]/div[1]/div[2]/div[2]/form/div/div/input').send_keys('APPLE iPhone 12 (Black, 64 GB)')
time.sleep(2)
#time.sleep(20)
driver.find_element_by_xpath('//*[@id="container"]/div/div[1]/div[1]/div[2]/div[2]/form/div/button').click()
# driver.find_element_by_id('container').click()

time.sleep(5)
driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div[1]/div[2]/div[2]/div/div/div/a/div[2]/div[1]/div[1]').click()
# //*[@id="container"]/div/div[3]/div[1]/div[2]/div[2]/div/div/div/a/div[2]/div[1]/div[1]



time.sleep(5)
print(driver.window_handles)
window_after = driver.window_handles[1]
driver.switch_to.window(window_after)
print('>>>>>>>>>>>>>>>>>>>>>>>>>>>> ')
time.sleep(2)
print(driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div[1]/div[2]/div[3]/div/div[1]/h1/span').text)
driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div[1]/div[1]/div[2]/div/ul/li[1]/button').click()
time.sleep(2)






import pymysql
  
#Create the connection object   
myconn = pymysql.connect(host = "localhost", user = "root",passwd = "sweety110", database='lms', autocommit = True, charset = 'utf8mb4', cursorclass = pymysql.cursors.DictCursor)

cursor = myconn.cursor() 



cursor.execute("CREATE TABLE flipkart (ModelNumber VARCHAR(255),ModelName VARCHAR(255),Color VARCHAR(255))")
               