from selenium import webdriver
import csv
from array import *
import pandas as pd
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
 
#Loading the webdriver from location
driver = webdriver.Chrome(executable_path='//home/muffy/chromedriver/chromedriver')
 
#Opening website on webdriver
driver.get("https://web.whatsapp.com/") 
 
#Loading the CSV file
f="/home/muffy/Documents/contacts.csv"
 
#Reading the CSV file and storing values in 'data'
with open(f, newline='') as x:
    reader = csv.reader(x)
    data = list(reader)
 
#Declaring an empty list
l=len(data)
names=[0]*l
 
#initialising loop variable
i=0
 
#Loop for removing "[","]" and "'" from data
for x in data:
  names[i]=str(x)[2:-2]
  i += 1
 
#Enter the message to be sent
msg = input('Enter your message : ')
msg += "\nThis is a system generated mssg!"
 
#Final driver code that finds the names and then sends the message
for name in names:
  driver.find_element_by_xpath('//span[@title = "{}"]'.format(name)).click()
  driver.find_element_by_xpath('//div[@dir="ltr"][@data-tab="6"][@spellcheck="true"]').send_keys(msg, Keys.ENTER)