from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from inputsCopy import *


class AttendanceBot:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 10)


    def login(self,username,password):
        self.driver.get('https://mail.google.com')

        #fill out username and press next
        self.wait.until(EC.element_to_be_clickable((By.ID, 'identifierNext')))
        self.driver.find_element_by_id('identifierId').send_keys(username)
        self.driver.find_element_by_id("identifierNext").click()

        #fill out password and press next
        self.wait.until(EC.element_to_be_clickable((By.ID, 'passwordNext')))
        self.driver.find_element_by_name('password').send_keys(password)
        self.driver.find_element_by_id("passwordNext").click()
   
    def openForm(self):

        #click closest attendance email
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[text()='lnaidich']//parent::span[1]//parent::div[1]//parent::td[1]")))
        self.driver.find_element_by_xpath("//*[text()='lnaidich']//parent::span[1]//parent::div[1]//parent::td[1]").click()
        
        #open in google forms
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Fill out in Google Forms']")))
        self.driver.find_element_by_xpath("//a[text()='Fill out in Google Forms']").click()

        #switch to new window
        self.driver.switch_to_window(self.driver.window_handles[1])

    def fillOutForm(self,first,last,grade):

        #fill out first name
        self.wait.until(EC.element_to_be_clickable((By.NAME, 'entry.255548752')))
        self.driver.find_element_by_name('entry.255548752').send_keys(first)

        #fill out second name
        self.driver.find_element_by_name('entry.214735743').send_keys(last)

        #click right grade
        self.driver.find_element_by_css_selector("[data-value='"+str(grade)+"']").click()

        #hit submit button
        self.driver.find_element_by_xpath("//*[text()='Submit']").click()


test = AttendanceBot()
test.login(email, password)
test.openForm()
test.fillOutForm(firstName ,lastName,gradeLevel)







