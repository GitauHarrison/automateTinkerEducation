# ! python3
# slack_login.py - it asks for user input in the input fields before logging in

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import datetime

chrome_options = webdriver.ChromeOptions(); 
chrome_options.add_experimental_option("excludeSwitches", ['enable-automation']);
browser = webdriver.Chrome(options=chrome_options); 
#browser = webdriver.Firefox()
browser.maximize_window()


def slack_login():
    browser.get('https://slack.com/signin#/')
    workspace_elem = browser.find_element_by_name('domain')
    workspace_elem.click()
    workspace = input('What is your workspace? ')
    workspace_elem.send_keys(workspace)
    continue_elem = browser.find_element_by_id('submit_team_domain')
    continue_elem.send_keys(Keys.ENTER)
    sleep(1.5)

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

    

    # Post my commute time
    def commute_time():
        sleep(2)
        commute_channel_elem = browser.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[1]/div/nav/div/div[1]/div/div/div[1]/div/div/div[16]')
        commute_channel_elem.click()
        sleep(1.5)
        post_elem = browser.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[3]/div/div[2]/footer/div/div/div[1]/div[1]/div[1]')        
        post_elem.click()
        arrival = datetime.datetime.now().strftime('%I:%M:%S %p')
        post_elem.send_keys(arrival + ' Work started')        
        post_elem.send_keys(Keys.ENTER)
        sleep(3)

        lunch_time_now = datetime.datetime.now().strftime('%I:%M:%S %p')
        post_elem = browser.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[3]/div/div[2]/footer/div/div/div[1]/div[1]/div[1]')        
        post_elem.click()
        post_elem.send_keys(' Left for lunch at ', lunch_time_now)
        post_elem.send_keys(Keys.ENTER)
        sleep(3)

        return_from_lunch_break = datetime.datetime.now().strftime('%I:%M:%S %p')
        post_elem = browser.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[3]/div/div[2]/footer/div/div/div[1]/div[1]/div[1]')        
        post_elem.click()
        post_elem.send_keys('Back from lunch at ', return_from_lunch_break)
        post_elem.send_keys(Keys.ENTER)
        sleep(3)

        departure = datetime.datetime.now().strftime('%I:%M:%S %p')
        post_elem = browser.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[3]/div/div[2]/footer/div/div/div[1]/div[1]/div[1]')        
        post_elem.click()
        post_elem.send_keys('Left at ', return_from_lunch_break)
        post_elem.send_keys(Keys.ENTER)
        sleep(3)

        def my_commute_loop():
            delta = datetime.timedelta(seconds = 1)
            now = datetime.datetime.now()

            lunch_delta = datetime.timedelta(minutes = 3)
            lunch_time = now + lunch_delta
            lunch_time_now = lunch_time.strftime('%I:%M:%S %p')

            back_from_lunch_delta = datetime.timedelta(minutes = 5)
            back_from_lunch = now + back_from_lunch_delta
            back_from_lunch_time = back_from_lunch.strftime('%I:%M:%S %p')

            departure_delta = datetime.timedelta(minutes = 7)
            departure = now + departure_delta
            departure_time = departure.strftime('%I:%M:%S %p')

            while now < (departure + datetime.timedelta(seconds = 1)):  
                #print('Now: ', now.strftime('%I:%M:%S %p'))                                          
                if now == lunch_time:
                    post_elem.send_keys(' Left for lunch at ', lunch_time_now)
                    post_elem.send_keys(Keys.ENTER)
                    sleep(60)
                elif now == back_from_lunch:
                    post_elem.send_keys('Back from lunch at ', back_from_lunch_time)
                    post_elem.send_keys(Keys.ENTER)
                    sleep(60)            
                elif now == departure:
                    post_elem.send_keys('Left at ', departure_time)
                    post_elem.send_keys(Keys.ENTER) 
                    sleep(60)
                    #slack_logout()               
                now += delta
        #my_commute_loop()
    commute_time()

    browser.execute_script('window.open('');')
    browser.switch_to_window(browser.window_handles[1])
    gmail_login()
    sleep(3)
    trello_login()
    sleep(5)
    trello_logout()
    sleep(3)
    gmail_logout()
    sleep(3)
    browser.switch_to_window(browser.window_handles[0])
    slack_logout()

def slack_logout():
    side_bar_header_info_elem = browser.find_element_by_class_name('p-ia__sidebar_header__button')
    side_bar_header_info_elem.click()
    sleep(1.5)
    sign_out_elem = browser.find_element_by_xpath('/html/body/div[6]/div/div/div/div/div/div/div[15]/button')
    sleep(1.5)
    browser.save_screenshot('slack_logout.png')
    sign_out_elem.click()    
    sleep(1.5)
    browser.close()

def gmail_login():
    # Enter your email
    browser.get('https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin')
    email_input_elem = browser.find_element_by_class_name('whsOnd')
    email_input_elem.click()
    email_input_elem.clear()
    email = input('What is your email? ')
    email_input_elem.send_keys(email)
    email_next_button_elem = browser.find_element_by_id('identifierNext')
    email_next_button_elem.send_keys(Keys.ENTER)
    sleep(2)    

    # Fill in your password
    password_input_elem = browser.find_element_by_class_name('whsOnd')
    password_input_elem.click()
    password_input_elem.clear()
    password = input('What is your password? ')
    password_input_elem.send_keys(password)
    password_next_button_elem = browser.find_element_by_id('passwordNext')
    password_next_button_elem.send_keys(Keys.ENTER)
    sleep(1)
    
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

    # sign in to trello
    #browser.execute_script('window.open('');')
    #browser.switch_to_window(browser.window_handles[2])
    #trello_login()
    #sleep(5)

    #trello_logout()
    #sleep(5)
    #browser.execute_script('window.open('');')
    #browser.switch_to_window(browser.window_handles[1])
    #gmail_logout()

    #browser.execute_script('window.open('');')
    #browser.switch_to_window(browser.window_handles[0])
    #slack_logout()

def trello_login():
    browser.execute_script('window.open('');')
    browser.switch_to_window(browser.window_handles[2])

    browser.get('https://trello.com/login')
    google_auth_button = browser.find_element_by_id('google-link')
    google_auth_button.click()
    sleep(3)

    teacher_training_board_elem = browser.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div[2]/main/div[3]/div/div[2]/div/div/div/div/div[2]/div/div/div[1]/div/div[2]/ul/li')
    teacher_training_board_elem.click()

def trello_logout():
    profile_elem = browser.find_element_by_class_name('_24AWINHReYjNBf')
    profile_elem.click()
    sleep(2)
    logout_elem = browser.find_element_by_class_name('_2jR0BZMM5cBReR')
    sleep(1.5)
    browser.save_screenshot('trello_logout.png')
    logout_elem.click()
    sleep(3)
    browser.close()

def gmail_logout():
    #browser.execute_script('window.open('');')
    browser.switch_to_window(browser.window_handles[1])
    profile_elem = browser.find_element_by_class_name('gb_ia')
    profile_elem.click()
    sleep(1.5)
    sign_out_elem = browser.find_element_by_link_text('Sign out')
    sign_out_elem.click()
    sleep(1.5)
    browser.save_screenshot('gmail_logout.png')
    browser.close()

slack_login()
#gmail_login()