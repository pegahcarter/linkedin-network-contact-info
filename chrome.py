import os
import time
from selenium import webdriver
import pandas as pd

class Chrome:

    def __init__(self):
        username, password = pd.read_csv('login.csv').values[0]
        self.username = username
        self.password = password
        self._connect()

    def _connect(self):
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        self.web = webdriver.Chrome(os.getcwd() + '/chromedriver')
        # self.web = webdriver.Chrome(os.getcwd() + '/chromedriver', options=options)
        self._login()

    def _login(self):
        self.get_url('https://linkedin.com/login')
        self.send_keys('input[@id="username"]', self.username)
        self.send_keys('input[@id="password"]', self.password)
        self.click('button[@aria-label="Sign in"]')
        self.get_url('https://linkedin.com/mynetwork/invite-connect/connections/')
        self.scroll_to_bottom()

    def execute_js(self, string):
        self.web.execute_script(string)

    def refresh(self):
        self.web.close()
        self._connect()

    def get_url(self, url):
        self.web.get(url)

    def load_element(self, element, element_to_compare=None):
        for i in range(100):
            time.sleep(.1)
            results = self.web.find_elements_by_xpath('//' + element)
            if element is None:
                continue
            elif len(results) == 1:
                return results[0]
            elif results != element_to_compare:
                return results

        return results

    def send_keys(self, element, string):
        textbox = self.load_element(element)
        textbox.send_keys(string)

    def click(self, element):
        clickable_element = self.load_element(element)
        clickable_element.click()
