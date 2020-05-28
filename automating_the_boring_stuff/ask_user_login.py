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
    #browser.execute_script('window.open('');')
    #browser.switch_to_window(browser.window_handles[1])

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
        sleep(2)
        commute_channel_elem = browser.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[2]/div/nav/div/div[1]/div/div/div[1]/div/div/div[17]/div/a')
        commute_channel_elem.click()
        sleep(1.5)
        post_elem = browser.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[3]/div/div[2]/footer/div/div/div[1]/div[1]/div[1]')        
        post_elem.click()
        arrival = datetime.datetime.now().strftime('%I:%M:%S %p')
        post_elem.send_keys(arrival + ' Work started')        
        post_elem.send_keys(Keys.ENTER)

        def my_loop():
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
                    sleep(5)
                elif now == back_from_lunch:
                    post_elem.send_keys('Back from lunch at ', back_from_lunch_time)
                    post_elem.send_keys(Keys.ENTER)
                    sleep(5)            
                elif now == departure:
                    post_elem.send_keys('Left at ', departure_time)
                    post_elem.send_keys(Keys.ENTER) 
                    sleep(2)
                    slack_logout()               
                now += delta
        my_loop()
    commute_time()

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

slack_login()