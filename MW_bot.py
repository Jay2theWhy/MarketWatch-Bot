from selenium import webdriver
from time import sleep
from login_info import username, password

class MW_bot:
    def __init__(self):
        self.driver = webdriver.Chrome()
    
    def login(self, game_name):
        game_name = game_name.lower()
        game_name = game_name.replace(' ', '-')
        self.driver.get('https://www.marketwatch.com/game/' + game_name)

        # get to the log in screen
        login_button = self.driver.find_element_by_xpath('/html/body/section/div[1]/header/div/div/a[2]/span')
        login_button.click()

        # input username and password then click submit
        userid_in = self.driver.find_element_by_xpath('//*[@id="username"]')
        password_in = self.driver.find_element_by_xpath('//*[@id="password"]')
        submit_button = self.driver.find_element_by_xpath('//*[@id="basic-login"]/div[1]/form/div/div[6]/div[1]/button')

        userid_in.send_keys(username)
        password_in.send_keys(password)
        submit_button.click()
    
    def select_stock(self, stock_sym):
        input_bar = self.driver.find_element_by_xpath('/html/body/div[2]/div[3]/div[1]/div[1]/div/div[1]/input')
        input_bar.send_keys(stock_sym)

        sleep(2)
        trade_button = self.driver.find_element_by_xpath('/html/body/div[2]/div[3]/div[1]/div[1]/div/div[2]/table/tbody/tr/td[4]/button')
        trade_button.click()

bot = MW_bot()
bot.login('NO CORONA')
sleep(2)
bot.select_stock('nugt')