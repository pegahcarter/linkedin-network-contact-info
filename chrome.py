import os
from time import sleep
from selenium import webdriver


class Chrome:

    options = webdriver.ChromeOptions()
    options.add_argument('headless')

    def __init__(self):
        self._connect()

    def _connect(self):
        self.web = webdriver.Chrome(
            os.getcwd() + '/chromedriver',
            options=self.options
        )

    def refresh(self):
        self.web.close()
        self._connect()

    def get(self, url):
        self.web.get(url)

    def load(self, element):
        results = self.web.find_elements_by_xpath('//' + element)
        if results:
            if len(results) == 1:
                return results[0]
            else:
                return results
        else:
            sleep(0.1)
            return self.load(element)
