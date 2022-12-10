from selenium import webdriver

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time


# Replace below path with the absolute path
# to chromedriver in your computer
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.implicitly_wait(10)

#open spotify
driver.get('https://open.spotify.com/collection/tracks')

#sign in with Facebook
driver.find_element_by_css_selector('.btn-black.btn--no-margin.btn--full-width').click()
driver.find_element_by_css_selector('.btn.btn-block.btn-facebook.ng-binding').click()

#sign in

#username
driver.find_element_by_id('email').send_keys('varunn.is19@bmsce.ac.in')
#password
driver.find_element_by_id('pass').send_keys('V9900303090a@')
driver.find_element_by_id('loginbutton').click()

#open all liked tracks
driver.get('https://open.spotify.com/collection/tracks')

#scroll to the bottom of the page
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(0.5)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

#get all tracks titles
songs = []
titles = driver.find_elements_by_xpath('//div[@class="tracklist-name ellipsis-one-line"]')
artists = driver.find_elements_by_xpath('//div[@class="second-line"]')

for title, artist in zip(titles, artists):
    t = title.text
    a = artist.text.split('\n')[0]
    songs.append(t + ' ' + a)

exp = ' EXPLICIT'

for s1 in songs:
    if exp in s1:
        ind = songs.index(s1)
        s2 = s1.split(exp)[0]
        songs[ind] = s2
    else:
        pass