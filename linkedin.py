import pandas as pd
import chrome
import os
import time


chrome = chrome.Chrome()
chrome.get_url('https://linkedin.com/mynetwork/invite-connect/connections/')


while True:
    connections = chrome.load_element('section/ul/li/div')
    time.sleep(1)
    chrome.execute_js('window.scrollBy(0,4000)')
    if connections == chrome.load_element('section/ul/li/div'):
        break


mynetwork = []



for connection in connections:
    # connection = connections[0]
    row = connection.text.split('\n')
    name = row[0]
    for i in range(len(row)):
        if 'occupation' in row[i]:
            occupation = row[i+1]
    try:
        title, company = occupation.split(' at ')
    except:
        title = None
        company = occupation

    profile_link = connection.find_element_by_xpath('a').get_attribute('href')
    mynetwork.append({
        'Name': name,
        'Title': title,
        'Company': company,
        'Profile Link': profile_link
    })

# NOTE: do I need to use this commented-out code in the future?
# pd.DataFrame(mynetwork).to_csv('data.csv', index=False)
for person in mynetwork:
    # if mynetwork.index(person) % 100 == 0:
    #     chrome.refresh()
    chrome.get_url(person['Profile Link'] + 'detail/contact-info')
    location = chrome.load_element('div[@id="profile-wrapper"]/div[1]/div[1]/div[1]/div[2]/section/div[3]/div[1]/h3')
    person['Location'] = location.text
    contact_info = chrome.load_element('artdeco-modal-content/section/div/div[1]/div/section')[1:]
    for section in contact_info:
        description = section.text.split('\n')
        title = description.pop(0)
        person[title] = description


chrome.web.close()
# Company, Name, Title
pd.DataFrame(mynetwork).to_csv('data2.csv', index=False)
