import winwifi
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import os
options=Options()
print("Attempting to Connect...")
try:
    winwifi.WinWiFi.connect("TESTING")
    print("TESTING Connected")
except:
    print("Cannot Connect to TESTING,Making login attempt...")
    pass
try:
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')

    driver=webdriver.Chrome(options=options)
    os.system("cls")

    driver.minimize_window()
    driver.get("http://www.msftconnecttest.com/redirect")
    os.system("cls")
    print("Browser Launched...")

    try:
        # Replace the <username> with username_roll and <password> with password

        driver.find_element(By.XPATH, "//input[@name='user.username']").send_keys("<username>")
        driver.find_element(By.XPATH, "//input[@name='user.password']").send_keys("<password>")
        driver.find_element(By.XPATH, "//input[@type='submit']").send_keys(Keys.RETURN)
        print("Credential Submitted...")
        driver.find_element(By.XPATH, "//input[@type='submit']").send_keys(Keys.RETURN)
    except:
        pass
except:
    pass
try:
    print("Attempting to Connect After Logging...")
    try:
        winwifi.WinWiFi.disconnect()
    except:
        pass
    try:
        winwifi.WinWiFi.connect("TESTING")
        print("\n*** TESTING Connected Successfully ***\nExitting...")
    except:
        pass
    driver.close()
    exit()
except:
    pass

