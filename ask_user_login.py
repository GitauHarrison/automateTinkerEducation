# ! python3
# slack_login.py - it asks for user input in the input fields before logging in

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

browser = webdriver.Chrome()

def slack_login():
    browser.execute_script('window.open('');')
    browser.switch_to_window(browser.window_handles[1])

    browser.get('https://slack.com/signin#/')
    workspace_elem = browser.find_element_by_name('domain')
    workspace_elem.click()
    workspace_elem.send_keys('tinkeredu')
    continue_elem = browser.find_element_by_id('submit_team_domain')
    continue_elem.send_keys(Keys.ENTER)
    sleep(3)

    sign_in_email_elem = browser.find_element_by_name('email')
    sign_in_email_elem.click()
    email = input('What is your email address?')
    sign_in_email_elem.send_keys(email)

    sign_in_password_elem = browser.find_element_by_name('password')
    sign_in_password_elem.click()
    password = input('What is your password? ')
    sign_in_password_elem.send_keys(password)

    sign_in_button_elem = browser.find_element_by_id('signin_btn')
    sign_in_button_elem.send_keys(Keys.ENTER)
    sleep(2)

    # Post my commute time
    
slack_login()