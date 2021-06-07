import pyautogui
import time
from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome('chromedriver.exe')
driver.get('https://www.keyhero.com/free-typing-test/')


def press(key):
    pyautogui.keyDown(key)
    pyautogui.keyUp(key)


press('esc')

time.sleep(1)

soup = BeautifulSoup(driver.page_source, 'html.parser')
start = soup.find('span', {'class': 'quote-current'}).text
test = soup.find('span', {'class': 'quote-right'}).text
test = start + " " + test
print(test)

pyautogui.typewrite(test)

time.sleep(10)

driver.quit()
