from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time

def pressTab():
    ActionChains(driver).key_down(Keys.TAB).key_up(Keys.TAB).perform()

def pressEnter():
    ActionChains(driver).key_down(Keys.RETURN).key_up(Keys.RETURN).perform()

def deletePosts():
    driver.get('https://www.reddit.com/user/'+ name +'/posts/')
    while True:
        try:
            driver.find_element_by_css_selector("[aria-label='more options']").click()
        except:
            print('\033[92m' + "[DONE] Deleting posts" + '\x1b[0m')
            questionUser()
            break
        else:
            for i in range (5):
                pressTab()
            pressEnter()
            driver.find_element_by_xpath("//*[text()='delete post']").click()
            driver.refresh()
            time.sleep(1)

def deleteComments():
    driver.get('https://old.reddit.com/user/'+ name +'/comments/')
    while True:
        try:
            driver.find_element_by_xpath("//*[text()='delete']").click()
        except:
            print ('\033[92m' + "[DONE] Deleting comments" + '\x1b[0m')
            questionUser()
            break
        else:
            pressTab()
            pressEnter()
            driver.refresh()
            time.sleep(1)

def deleteAccount():
    driver.get('https://www.reddit.com/settings')
    time.sleep(3)
    driver.find_element_by_xpath("//*[text()='I Agree']").click()
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)
    driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/div/div/div[2]/div[1]/div[9]/button").click()
    for i in range (3):
        pressTab()
    ActionChains(driver).send_keys(name).perform()

    pressTab()
    ActionChains(driver).send_keys(password).perform()

    pressTab()
    pressEnter()

    for i in range (2):
        pressTab()
    pressEnter()

    for i in range (2):
        pressTab()
    pressEnter()
    print ('\033[92m' + "[DONE] Deleting account" + '\x1b[0m')
    time.sleep(5)
    print ('Exiting WebDriver in 3...')
    time.sleep(1)
    print ('Exiting WebDriver in 2...')
    time.sleep(1)
    print ('Exiting WebDriver in 1...')
    time.sleep(1)
    driver.quit()


def questionUser():
    pick = input("What do you want to delete? (posts/comments/account): ")
    if pick == 'posts':
        deletePosts()

    if pick == 'comments':
        deleteComments()

    if pick == 'account':
        deleteAccount()
driver = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver')  # Optional argument, if not specified will search path.
# or '/usr/lib/chromium-browser/chromedriver' if you use chromium-chromedriver

# GET DATA FROM USER

name = input("Name: ")
password = input("Password: ")

# 

# LOG IN TO REDDIT 
driver.get("https://www.reddit.com/login/")
driver.find_element_by_id('loginUsername').send_keys(name)
driver.find_element_by_id('loginPassword').send_keys(password)
driver.find_element_by_xpath('/html/body/div/div/div[2]/div/form/div[1]/fieldset[5]/button').click()
time.sleep(10)
#

questionUser()

