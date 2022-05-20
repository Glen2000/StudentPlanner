

#===============================================================#
# Import modules

import sys
from tkinter import simpledialog

import sys

import matplotlib
import requests
from bs4 import BeautifulSoup
import re
import tkinter as tk
from tkinter import simpledialog
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime, date

#===============================================================#
ROOT = tk.Tk()
ROOT.withdraw()



#===============================================================#


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
import time

DRIVER_PATH = '/path/to/chromedriver'
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
from seleniumwire import webdriver

driver.get("https://brightspace.tudublin.ie/d2l/home")
from selenium.webdriver import ActionChains

import getpass  # so you don't show your password in the sourcecode

# the input dialog
studentID = simpledialog.askstring(title="ID",
                            prompt="Student ID: ")

studentID_ = studentID


# the input dialog
pwd = simpledialog.askstring(title="Password",
                            prompt="Password: ")

pwd_ = pwd

#studentID = input("Username: ")
USERNAME = studentID_ + "@mytudublin.ie"
PASSWORD = pwd_ #getpass.getpass()

login = driver.find_element_by_xpath("//input").send_keys(USERNAME)
password = driver.find_element_by_xpath("//input[@type='password']").send_keys(PASSWORD)
# submit = driver.find_element_by_xpath("//input[@value='input']").click()

# getting the button by class name
button = driver.find_element_by_class_name("inline-block")

# clicking on the button
button.click()

time.sleep(3)  # Sleep for 20 seconds

# getting the button by class name
button2 = driver.find_element_by_class_name("inline-block")

# clicking on the button
button2.click()

time.sleep(3)  # Sleep for 20 seconds

# getting the button by class name
button3 = driver.find_element_by_class_name("table-row")

# clicking on the button
button3.click()

#===============================================================#