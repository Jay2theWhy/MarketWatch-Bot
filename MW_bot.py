from selenium import webdriver
from time import sleep
from login_info import username, password

class MW_bot:
    def __init__(self):
        self.driver = webdriver.Chrome()
    
    def login(self):
        self.driver.get('https://sso.accounts.dowjones.com/login?state=g6Fo2SBleG1tbHpGVG55Wm9xdFczM0FoT3RBamw1MWRxMXExTaN0aWTZIDdmY1Y5aGdMMGRRQUZsME1UNVJIRW5Md0EzY3VOT1Eto2NpZNkgNWhzc0VBZE15MG1KVElDbkpOdkM5VFhFdzNWYTdqZk8&client=5hssEAdMy0mJTICnJNvC9TXEw3Va7jfO&protocol=oauth2&scope=openid%20idp_id%20given_name%20family_name%20email%20djid%20prts&response_type=code&redirect_uri=https%3A%2F%2Faccounts.marketwatch.com%2Fauth%2Fsso%2Flogin&nonce=6903a150-8354-4330-9a31-97e50041293b&ui_locales=en-us-x-mw-3-8&ns=prod%2Faccounts-mw&savelogin=on#!/signin')
        sleep(0.5)

        userid_in = self.driver.find_element_by_xpath('//*[@id="username"]')
        password_in = self.driver.find_element_by_xpath('//*[@id="password"]')
        submit_button = self.driver.find_element_by_xpath('//*[@id="basic-login"]/div[1]/form/div/div[6]/div[1]/button')

        userid_in.send_keys(username)
        password_in.send_keys(password)
        submit_button.click()

bot = MW_bot()
bot.login()