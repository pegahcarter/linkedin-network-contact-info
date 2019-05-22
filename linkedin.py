import pandas as pd
import chrome
import os
import time


chrome = chrome.Chrome()
chrome.get_url('https://linkedin.com/mynetwork/invite-connect/connections/')


while True:
    connections = chrome.load_element('section/ul/li/div/a')
    time.sleep(1)
    chrome.execute_js('window.scrollBy(0,4000)')
    if connections == chrome.load_element('section/ul/li/div/a'):
        break



mynetwork = []
for connection in connections:
    profile_link = connection.get_attribute('href')
    name = connection.find_element_by_xpath('div/img').get_attribute('alt')
    mynetwork.append({
        'Name': name,
        'Profile Link': profile_link
    })

# mynetwork = pd.DataFrame(mynetwork)
# mynetwork['Location'] = None


for person in mynetwork:
    # if mynetwork.index(person) % 100 == 0:
    #     chrome.refresh()
    chrome.get_url(person['Profile Link'] + 'detail/contact-info')
    bio = chrome.load_element('div[@role="main"]/div[1]/div/section/div[2]/div[2]/div[1]')
    occupation = bio.find_element_by_xpath('h2').text
    try:
        title, _ = occupation.split(' at ')
    except:
        title = None

    location = bio.find_element_by_xpath('ul[2]/li[1]').text
    try:
        city, state = location.split(', ')
    except:
        city, state = None, None

    contact_info = chrome.load_element('section[contains(@class, "pv-contact-info__contact-type")]')
    for section in contact_info[1:]:

        description = section.find_element_by_xpath('header').text
        description = description.split('\n')
        title = description.pop(0)

    person[title] = description


chrome.web.close()
# Company, Name, Title
backup = mynetwork

pd.DataFrame(mynetwork).to_csv('data2.csv', index=False)
