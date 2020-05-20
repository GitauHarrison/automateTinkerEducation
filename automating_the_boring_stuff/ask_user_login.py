# ! python3
# slack_login.py - it asks for user input in the input fields before logging in

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import datetime

chrome_options = webdriver.ChromeOptions(); 
chrome_options.add_experimental_option("excludeSwitches", ['enable-automation']);
browser = webdriver.Chrome(options=chrome_options); 

browser.maximize_window()


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

    for repeat in range(3):
        sign_in_email_elem = browser.find_element_by_name('email')
        sign_in_email_elem.click()
        sign_in_email_elem.clear()
        email = input('What is your email address? ')
        sign_in_email_elem.send_keys(email)

        sign_in_password_elem = browser.find_element_by_name('password')
        sign_in_password_elem.click()
        sign_in_password_elem.clear()
        password = input('What is your password? ')
        sign_in_password_elem.send_keys(password)

        sign_in_button_elem = browser.find_element_by_id('signin_btn')
        sign_in_button_elem.send_keys(Keys.ENTER)
        sleep(1.5)

        break

    # Post my commute time
    def commute_time():
        commute_channel_elem = browser.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[2]/div/nav/div/div[1]/div/div/div[1]/div/div/div[17]/div/a')
        commute_channel_elem.click()
        sleep(1.5)
        post_elem = browser.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[3]/div/div[2]/footer/div/div/div[1]/div[1]/div[1]')
        arrival = datetime.datetime.now().strftime('%I:%M:%S %p')
        post_elem.click()
        post_elem.send_keys(arrival + ' Work started')
        sleep(1.5)
        post_elem.send_keys(Keys.ENTER)

    commute_time()

def slack_logout():
    #browser.switch_to_window(browser.window_handles[1])
    post_elem = browser.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[3]/div/div[2]/footer/div/div/div[1]/div[1]/div[1]')
    departure = datetime.datetime.now().strftime('%I:%M:%S %p')
    post_elem.click()
    post_elem.send_keys(departure + ' Completed work')
    sleep(1.5)
    post_elem.send_keys(Keys.ENTER)

    side_bar_header_info_elem = browser.find_element_by_class_name('p-ia__sidebar_header__button')
    side_bar_header_info_elem.click()
    sleep(1.5)
    sign_out_elem = browser.find_element_by_xpath('/html/body/div[6]/div/div/div/div/div/div/div[15]/button')
    sleep(1.5)
    browser.save_screenshot('slack_logout.png')
    sign_out_elem.click()    
    sleep(1.5)
    browser.close()

slack_login()
sleep(10)
slack_logout()