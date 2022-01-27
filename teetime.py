import Account #create separate file for username/password for golf course
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#Initialize Chrome Driver
driver=webdriver.Chrome(executable_path='chromedriver')
fitRows=[]
xPathInit='//*[@id="searchMatrix"]/div[2]/table/tbody/tr['
xPathEnd=']/td[3]'

#Open the browser
driver.get('https://sanjosemuni.quick18.com/teetimes/searchmatrix')
driver.maximize_window()
dateSelect=driver.find_element(By.ID, 'SearchForm_Date')
dateSelect.click()
dateSelect.clear()
dateSelect.send_keys('2/2/2022') #change this input to a variable i can type in
dateSelect.submit()
time.sleep(2)

#slots=driver.find_element(By.XPATH, '//*[@id="searchMatrix"]/div[2]/table/tbody/tr[5]/td[1]') #finds time in row 1 column 1
#picks=driver.find_element(By.XPATH, '//*[@id="searchMatrix"]/div[2]/table/tbody/tr[5]/td[3]') #finds the select button on row 1 column 3 for the correct time
#table = driver.find_element(By.XPATH, '//*[@id="searchMatrix"]/div[2]/table')

finalXpath=xPathInit + str(2) + xPathEnd #creating XPath to the confirm button on the correct time. Just need to pass the correct row number instead of str(2)
picks=driver.find_element(By.XPATH, finalXpath)

button=picks.find_element(By.CLASS_NAME, 'ok')
button.click()
time.sleep(1)

numPlayers=driver.find_element(By.ID, 'Players2')
numPlayers.click()
button=driver.find_element(By.CLASS_NAME, 'ok')
button.click() #gets us to sign in page
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

###
#To Do:
#1. Need to select the right row and check the time.