import chrome
import linkedin


if __name__ == '__main__':

    chrome = chrome.Chrome()
    linkedin.run(chrome)
    chrome.web.close()
