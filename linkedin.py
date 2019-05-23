import pandas as pd
import chrome
import os
import time
import unicode

def run(chrome):

    while True:
        before_scroll = chrome.load_element('section/ul/li/div/a')
        chrome.execute_js('window.scrollBy(0,4000)')
        connections = chrome.load_element('section/ul/li/div/a', element_to_compare=before_scroll)
        if before_scroll == connections:
            break

    mynetwork = []
    for connection in connections:
        profile_link = connection.get_attribute('href')
        name = connection.find_element_by_xpath('div/img').get_attribute('alt')
        mynetwork.append({
            'Name': name.decode('utf-8', 'ignore'),
            'Profile Link': profile_link
        })

    for person in mynetwork:
        # if mynetwork.index(person) % 100 == 0:
        #     chrome.refresh()
        chrome.get_url(person['Profile Link'] + 'detail/contact-info')
        bio = chrome.load_element('div[@role="main"]/div[1]/div/section/div[2]/div[2]/div[1]')
        occupation = bio.find_element_by_xpath('h2').text.decode('utf-8', 'ignore')
        try:
            title, _ = occupation.split(' at ')
        except:
            title = None

        person['Occupation'] = occupation
        person['Title'] = title

        location = bio.find_element_by_xpath('ul[2]/li[1]').text.decode('utf-8', 'ignore')
        try:
            city, state = location.split(', ')
        except:
            city, state = None, None

        person['Location'] = location
        person['City'] = city
        person['State'] = state

        contact_info = chrome.load_element('section[contains(@class, "pv-contact-info__contact-type")]')
        for section in contact_info[1:]:
            description = section.text.split('\n')
            title = description.pop(0)
            person[title] = '; '.join(description).decode('utf-8', 'ignore')


    chrome.web.close()

    # Company, Name, Title
    pd.DataFrame(mynetwork).to_csv('mynetwork.csv', index=False)
