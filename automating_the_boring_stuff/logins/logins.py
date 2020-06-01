# ! python3
# logins.py - automatically logs you in to GMail, slack, trello
# It does not ask for user input

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import datetime

chrome_options = webdriver.ChromeOptions(); 
chrome_options.add_experimental_option("excludeSwitches", ['enable-automation']);
browser = webdriver.Chrome(options=chrome_options); 
browser.maximize_window()

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
    email_input_elem.send_keys('my_email')
    email_next_button_elem = browser.find_element_by_id('identifierNext')
    email_next_button_elem.send_keys(Keys.ENTER)
    sleep(2)
    #email_input_elem.submit()

    # Fill in your password
    password_input_elem = browser.find_element_by_class_name('whsOnd')
    password_input_elem.click()
    password_input_elem.clear()
    password_input_elem.send_keys('my_password')
    password_next_button_elem = browser.find_element_by_id('passwordNext')
    password_next_button_elem.send_keys(Keys.ENTER)
    sleep(1)

    browser.switch_to_window(browser.window_handles[0])
    browser.close()
    browser.switch_to_window(browser.window_handles[0])
    
    # Switch to GDrive
    def gdrive():
        profile_elem = browser.find_element_by_class_name('gb_Sf')
        sleep(1.5)
        profile_elem.click()
        sleep(3)
        drive_elem = browser.find_element_by_xpath('/html/body/div/c-wiz/div/div/c-wiz/div/div/ul[1]/li[4]/a')
        drive_elem = browser.find_element_by_link_text('Drive')
        drive_elem.click()
        sleep(2)
    #gdrive()

    browser.switch_to_window(browser.window_handles[0])
    sign_out_time = 9 * 60 * 60
    sleep(sign_out_time + 60)
    gmail_logout()    

def gmail_logout():
    #browser.execute_script('window.open('');')
    browser.switch_to_window(browser.window_handles[0])
    profile_elem = browser.find_element_by_class_name('gb_ia')
    profile_elem.click()
    sleep(1.5)
    sign_out_elem = browser.find_element_by_link_text('Sign out')
    sign_out_elem.click()
    sleep(1.5)
    browser.save_screenshot('gmail_logout.png')
    browser.close()

def slack_login():
    browser.execute_script('window.open('');')
    browser.switch_to_window(browser.window_handles[1])

    browser.get('https://slack.com/signin#/')
    workspace_elem = browser.find_element_by_name('domain')
    workspace_elem.click()
    workspace_elem.send_keys('my_workspace')
    continue_elem = browser.find_element_by_id('submit_team_domain')
    continue_elem.send_keys(Keys.ENTER)
    sleep(1)

    sign_in_email_elem = browser.find_element_by_name('email')
    sign_in_email_elem.click()
    sign_in_email_elem.send_keys('my_email')

    sign_in_password_elem = browser.find_element_by_name('password')
    sign_in_password_elem.click()
    sign_in_password_elem.send_keys('my_password')

    sign_in_button_elem = browser.find_element_by_id('signin_btn')
    sign_in_button_elem.click()
    sleep(3)

    # Post my commute time
    def post_commute_time():

        to_lunch_break = 4 * 60 * 60
        from_lunch_break = 58 * 60
        to_departure = 4 * 60 * 60

        commute_channel_elem = browser.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[2]/div/nav/div/div[1]/div/div/div[1]/div/div/div[7]/a/span')
        commute_channel_elem.click()
        sleep(2)
        post_elem = browser.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[3]/div/div[2]/footer/div/div/div[1]/div[1]/div[1]')
        arrival = datetime.datetime.now().strftime('%I:%M:%S %p')
        post_elem.click()
        post_elem.send_keys(arrival + ' Work started')
        post_elem.send_keys(Keys.ENTER)
        sleep(to_lunch_break + 60)

        lunch_time_now = datetime.datetime.now().strftime('%I:%M:%S %p')
        post_elem = browser.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[3]/div/div[2]/footer/div/div/div[1]/div[1]/div[1]')        
        post_elem.click()
        post_elem.send_keys(' Left for lunch at ', lunch_time_now)
        post_elem.send_keys(Keys.ENTER)
        sleep(from_lunch_break)

        return_from_lunch_break = datetime.datetime.now().strftime('%I:%M:%S %p')
        post_elem = browser.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[3]/div/div[2]/footer/div/div/div[1]/div[1]/div[1]')        
        post_elem.click()
        post_elem.send_keys('Back from lunch at ', return_from_lunch_break)
        post_elem.send_keys(Keys.ENTER)
        sleep(to_departure + 60)

        departure = datetime.datetime.now().strftime('%I:%M:%S %p')
        post_elem = browser.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[3]/div/div[2]/footer/div/div/div[1]/div[1]/div[1]')        
        post_elem.click()
        post_elem.send_keys('Left at ', return_from_lunch_break)
        post_elem.send_keys(Keys.ENTER)
        sleep(3)
        slack_logout()

    post_commute_time()


def slack_logout():
    browser.switch_to_window(browser.window_handles[1])
    side_bar_header_info_elem = browser.find_element_by_class_name('p-ia__sidebar_header__button')
    side_bar_header_info_elem.click()
    sleep(1.5)
    sign_out_elem = browser.find_element_by_xpath('/html/body/div[6]/div/div/div/div/div/div/div[15]/button')
    sign_out_elem.click()
    sleep(5)
    browser.save_screenshot('slack_logout.png')
    browser.close()


def trello_login():
    browser.execute_script('window.open('');')
    browser.switch_to_window(browser.window_handles[2])

    browser.get('https://trello.com/login')
    google_auth_button = browser.find_element_by_id('google-link')
    google_auth_button.click()
    sleep(3)

    teacher_training_board_elem = browser.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div[2]/main/div[3]/div/div[2]/div/div/div/div/div[2]/div/div/div[1]/div/div[2]/ul/li')
    teacher_training_board_elem.click()

    sign_out_time = 9 * 60 * 60
    sleep(sign_out_time + 60)
    trello_logout()

def trello_logout():
    sign_out_time = 9 * 60 * 60
    profile_elem = browser.find_element_by_class_name('_24AWINHReYjNBf')
    profile_elem.click()
    sleep(1.5)
    logout_elem = browser.find_element_by_class_name('_2jR0BZMM5cBReR')
    sleep(2)
    browser.save_screenshot('trello_logout.png')
    logout_elem.click()
    sleep(1)
    browser.close()



if __name__ == '__main__':
    gmail_login()
    slack_login()
    trello_login()
