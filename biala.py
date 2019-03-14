import time

from bs4 import BeautifulSoup
from selenium import webdriver


driver = webdriver.Firefox()
url = 'http://185.40.115.250/'
driver.get(url)

# go to schedules
element = driver.find_element_by_xpath('//*[@id="tab2Nav"]')
element.click()

# schedule for line A is selected from default
schedule_1 = []
select = driver.find_element_by_xpath('//*[@id="dvTab2Directions"]/table/tbody/tr/td[2]/div')
select.click()
li_elem = select.find_elements_by_tag_name('li')
for li in li_elem:
    direction = li.find_element_by_class_name('text').text
    print(direction)
    li.click()
    source = driver.page_source
    soup = BeautifulSoup(source, 'html.parser')
    schedule_table = soup.find('table', {'class': 'route-track-table'})

    for row in schedule_table.find_all('tr'):
        col = row.find_all('td', {'class': 'td2'})
        schedule_1.append(col[0].text.strip())

    print(schedule_1)
    del schedule_1[:]
    select.click()

