# Importing required libraries

# pip install selenium

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Setting up the webdriver
driver = webdriver.Chrome()
driver.maximize_window()


# Navigating to the Amazon.ca homepage
driver.get("https://www.youtube.com/")
time.sleep(3)

# Finding the search bar and entering text
# search_bar = driver.find_element_by_id("id","twotabsearchtextbox") old syntax
search_bar = driver.find_element("xpath","/html/body/ytd-app/div[1]/div/ytd-masthead/div[4]/div[2]/ytd-searchbox/form/div[1]/div[1]/input")
search_bar.send_keys("Oppenheimer")

# Submitting the search query
search_bar.send_keys(Keys.RETURN)

# Waiting for the search results page to load
time.sleep(5)

# Verifying that the search results page has loaded
assert "Oppenheimer" in driver.title

# Search results
trailer_link = driver.find_element("xpath","/html/body/ytd-app/div[1]/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer[2]/div[3]/ytd-video-renderer[1]/div[1]/div/div[1]/div/h3/a/yt-formatted-string")
trailer_link.click()

time.sleep(3)

# Maximize the video
maximize_button = driver.find_element("xpath","/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[1]/div[2]/div/div/ytd-player/div/div/div[27]/div[2]/div[2]/button[10]")
maximize_button.click()

# Waiting for update
time.sleep(5)

# Clicking on Pause button
pause_button= driver.find_element("xpath","//*[@id='movie_player']/div[27]/div[2]/div[1]/button")
pause_button.click()
time.sleep(2)

# Clicking on Play button
play_button= driver.find_element("xpath","//*[@id='movie_player']/div[27]/div[2]/div[1]/button")
play_button.click()
time.sleep(10)

mute_button= driver.find_element("xpath","/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy//span/button")
mute_button.click()
time.sleep(5)



driver.close()
