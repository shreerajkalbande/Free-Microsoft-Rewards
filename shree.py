import random
from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By

lis = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
EMAILFIELD = (By.ID, "i0116")
PASSWORDFIELD = (By.ID, "i0118")
NEXTBUTTON = (By.ID, "idSIButton9")
DECLINEBUTTON = (By.ID, "declineButton")
CHAT = (By.ID, "chat_header_link")
SEARCH = (By.ID, "b-scopeListItem-web")
FINAL = (By.ID, "sb_form_q")
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Create and configure the Chrome webdriver
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=22&id=264960&wreply=https%3a%2f%2fwww.bing.com%2fsecure%2fPassport.aspx%3fedge_suppress_profile_switch%3d1%26requrl%3dhttps%253a%252f%252fwww.bing.com%253a443%252frewards%252fsignin%253fru%253d%25252frewards%25252fdashboard%2526vt%253dSignin%2526ra%253d%26sig%3d1F6DD7F086C5692437CFC3CE87C3686B%26nopa%3d2&wp=MBI_SSL&lc=1033&CSRFToken=8d0d1757-7e53-4a61-acdf-c00fd8ec2dd4&cobrandid=c333cba8-c15c-4458-b082-7c8ce81bee85&nopa=2&lw=1&fl=easi2")

# wait for email field and enter email
WebDriverWait(driver, 10).until(EC.element_to_be_clickable(EMAILFIELD)).send_keys("YOUR MICROSOFT EMAIL")

# Click Next
WebDriverWait(driver, 10).until(EC.element_to_be_clickable(NEXTBUTTON)).click()

# wait for password field and enter password
WebDriverWait(driver, 10).until(EC.element_to_be_clickable(PASSWORDFIELD)).send_keys("PASSWORD")

# Click Login - same id?
WebDriverWait(driver, 10).until(EC.element_to_be_clickable(NEXTBUTTON)).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable(DECLINEBUTTON)).click()
WebDriverWait(driver, 6000).until(EC.element_to_be_clickable(CHAT)).click()
WebDriverWait(driver, 8000).until(EC.element_to_be_clickable(SEARCH)).click()
k = 0
m = WebDriverWait(driver, 50).until(EC.element_to_be_clickable(FINAL))
for g in range(1,10):
    m.send_keys(Keys.BACKSPACE)
    m = WebDriverWait(driver, 75).until(EC.element_to_be_clickable(FINAL))
while(1):
    t = lis[random.randint(1,25)]
    m.send_keys(t)
    m.send_keys(Keys.ENTER)
    m = WebDriverWait(driver, 50).until(EC.element_to_be_clickable(FINAL))
