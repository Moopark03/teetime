import Account #create separate file for username/password for golf course
import Utility
from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime
import time

#Initialize Chrome Driver
driver=webdriver.Chrome(executable_path='chromedriver')
xPathInit='//*[@id="searchMatrix"]/div[2]/table/tbody/tr['
xPathEnd=']/td[3]'

#Open the browser
driver.get('https://sanjosemuni.quick18.com/teetimes/searchmatrix')
driver.maximize_window()
dateSelect=driver.find_element(By.ID, 'SearchForm_Date')
dateSelect.click()
dateSelect.clear()
dateSelect.send_keys(Utility.DATE) #Automated 7 days ahead from the date the script runs
dateSelect.submit()
time.sleep(2)


table=driver.find_element(By.XPATH, '//*[@id="searchMatrix"]/div[2]/table/tbody')
index = 1
earlyTime = datetime.strptime(Utility.earlyTime, "%I:%M%p")
latestTime = datetime.strptime(Utility.latestTime, "%I:%M%p")

for row in table.find_elements(By.XPATH, './tr'): #ELEMENTS vs ELEMENT
     teeTime=row.find_element(By.CLASS_NAME, 'mtrxTeeTimes')
     players=row.find_element(By.CLASS_NAME, 'matrixPlayers')
     if(Utility.checkTime(teeTime.text, players.text, earlyTime, latestTime)):
          #print(index)
          break
     else:
          index += 1

finalXpath=xPathInit + str(index) + xPathEnd #creating XPath to the confirm button on the correct time.
picks=driver.find_element(By.XPATH, finalXpath)

button=picks.find_element(By.CLASS_NAME, 'ok')
button.click()
time.sleep(1)

numPlayers=driver.find_element(By.ID, 'Players2')
numPlayers.click()
button=driver.find_element(By.CLASS_NAME, 'ok')
button.click()
time.sleep(1)


emailField=driver.find_element(By.ID, 'EmailAddress')
passwordField=driver.find_element(By.ID, 'Password')
emailField.send_keys(Account.EMAIL)
passwordField.send_keys(Account.PASSWORD)
button=driver.find_element(By.CLASS_NAME, 'ok')
button.click()
time.sleep(1)

button=driver.find_element(By.CLASS_NAME, 'ok')
button.click()