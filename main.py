import chrome
import linkedin


if __name__ == '__main__':

    chrome = chrome.Chrome()
    chrome.get_url('https://linkedin.com/mynetwork/invite-connect/connections/')
    linkedin.run(chrome)
    chrome.web.close()
