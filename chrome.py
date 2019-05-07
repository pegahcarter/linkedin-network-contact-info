import os
from time import sleep
from selenium import webdriver
import pandas as pd

class Chrome:

    options = webdriver.ChromeOptions()
    options.add_argument('headless')

    def __init__(self):
        username, password = pd.read_csv('login.csv').values[0]
        self.username = username
        self.password = password
        self._connect()

    def _connect(self):
        self.web = webdriver.Chrome(
            os.getcwd() + '/chromedriver',
            options=self.options
        )
        self._login()

    def _login(self):
        self.get('https://linkedin.com/login')
        self.send_keys('input[@id="username"]', self.username)
        self.send_keys('input[@id="password"]', self.password)
        self.click('button[@aria-label="Sign in"]')

    def refresh(self):
        self.web.close()
        self._connect()

    def get(self, url):
        sleep(0.1)
        self.web.get(url)

    def load(self, element):
        results = self.web.find_elements_by_xpath('//' + element)
        if results:
            if len(results) == 1:
                return results[0]
            else:
                return results
        else:
            sleep(0.2)
            return self.load(element)

    def send_keys(self, element, string):
        textbox = self.load(element)
        textbox.send_keys(string)

    def click(self, element):
        clickable_element = self.load(element)
        clickable_element.click()
