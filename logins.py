# ! python3
# logins.py - automatically logs you in to GMail, slack, trello

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

browser = webdriver.Chrome()
#browser.maximize_window()

def gmail_login():
    browser.get('https://www.google.com/gmail/about/#')
    sign_in_elem = browser.find_element_by_link_text('Sign in')
    sign_in_elem.click()

    #browser.execute_script('window.open('');')
    browser.switch_to_window(browser.window_handles[1])
    sleep(3)

    # Enter your email
    email_input_elem = browser.find_element_by_class_name('whsOnd')
    email_input_elem.click()
    email_input_elem.clear()
    email_input_elem.send_keys('my-email')
    sleep(2)
    email_next_button_elem = browser.find_element_by_id('identifierNext')
    email_next_button_elem.send_keys(Keys.ENTER)
    sleep(2)
    #email_input_elem.submit()

    # Fill in your password
    password_input_elem = browser.find_element_by_class_name('whsOnd')
    password_input_elem.click()
    password_input_elem.clear()
    sleep(1.5)
    password_input_elem.send_keys('my-password')
    sleep(3)
    password_next_button_elem = browser.find_element_by_id('passwordNext')
    password_next_button_elem.send_keys(Keys.ENTER)
    sleep(6)

    browser.switch_to_window(browser.window_handles[0])
    browser.close()
    browser.switch_to_window(browser.window_handles[0])

    # Switch to GDrive
    profile_elem = browser.find_element_by_class_name('gb_Sf')
    sleep(1.5)
    profile_elem.click()
    sleep(3)
    #drive_elem = browser.find_element_by_class_name('kFwPee')
    drive_elem = browser.find_element_by_link_text('Drive')
    drive_elem.click()
    sleep(5)

    browser.switch_to_window(browser.window_handles[2])

def gmail_logout():
    #browser.execute_script('window.open('');')
    browser.switch_to_window(browser.window_handles[1])
    profile_elem = browser.find_element_by_class_name('gb_ia')
    sleep(1.5)
    profile_elem.click()
    sign_out_elem = browser.find_element_by_link_text('Sign out')
    sign_out_elem.click()
    sleep(3)
    browser.save_screenshot()
    browser.close()

if __name__ == '__main__':
    gmail_login()
    gmail_logout()
