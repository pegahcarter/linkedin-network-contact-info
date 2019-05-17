import os
import time
from selenium import webdriver
import pandas as pd

class Chrome:

    load_interval = 0.1
    scroll_element = 'section/ul/li/div'
    network_count = 1

    def __init__(self):
        username, password = pd.read_csv('login.csv').values[0]
        self.username = username
        self.password = password
        self._connect()

    def _connect(self):
        self.web = webdriver.Chrome(os.getcwd() + '/chromedriver')
        self._login()

    def _login(self):
        self.get('https://linkedin.com/login')
        self.send_keys('input[@id="username"]', self.username)
        self.send_keys('input[@id="password"]', self.password)
        self.click('button[@aria-label="Sign in"]')

    def scroll_to_bottom(self):
        
        pass


    def wait_for_element(self, element):
        for interval in range(0, 5, load_interval):
            time.sleep(interval)
            results = self.web.find_elements_by_xpath('//' + element)

    def execute_js(self, string):
        self.web.execute_script(string)

    def refresh(self):
        self.web.close()
        self._connect()

    def load_element(self, element):
        return self.wait_for_element(element)


    def get(self, url):
        time.sleep(0.1)
        self.web.get(url)

    def load(self, element=None):
        results = self.web.find_elements_by_xpath('//' + element)
        if len(results) == 1:
            return results[0]
        else:
            return results
        time.sleep(0.2)
        return self.load(element)

    def send_keys(self, element, string):
        textbox = self.load(element)
        textbox.send_keys(string)

    def click(self, element):
        clickable_element = self.load(element)
        clickable_element.click()
