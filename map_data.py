import time
import re
import os
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from dotenv import load_dotenv, find_dotenv
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

# options = Options()
# options.add_argument("--headless")
# options.add_argument("--no-sandbox")
# options.add_argument("--disable-dev-shm-usage")

load_dotenv(find_dotenv())

def authenticate_me(user, pwd):
    CHROME_URL = r"E:\chromedriver-win64\chromedriver.exe"
    URL = "https://twitter.com/home"
    driver = Chrome(service=Service(CHROME_URL))
    driver.get(URL)

    time.sleep(5)

    EMAIL_XPATH = "/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input"
    NEXT_XPATH = "/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]"
    SECURE_PATH = "/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input"
    PASSWORD_PATH = "/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input"
    FURTHER = "/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div"
    LOGIN_XPATH = "/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div"
    email_input = driver.find_element(By.XPATH, EMAIL_XPATH)
    email_input.send_keys(user)
    next_button = driver.find_element(By.XPATH, NEXT_XPATH)
    next_button.click()
    time.sleep(3)

    try:
        password_input = driver.find_element(By.XPATH, PASSWORD_PATH)
        password_input.send_keys(pwd)

        login_button = driver.find_element(By.XPATH, LOGIN_XPATH)
        login_button.click()

        time.sleep(5)
        search_elem_xpath = "/html/body/div[1]/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/div/label/div[2]/div/input"
        search_elem = driver.find_element(By.XPATH, search_elem_xpath)
        print("Found")
        search_elem.click()
        time.sleep(4)
        search_elem.send_keys("FGCreativeMaps")
        time.sleep(4)
        that_profile_xpath = "/html/body/div[1]/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[2]/div/div[4]/div"
        click_profile = driver.find_element(By.XPATH, that_profile_xpath)
        click_profile.click()

        descriptions = []

        DESC_XPATH = "/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div/section/div/div/div[2]/div/div/article/div/div/div[2]/div[2]/div[2]/div/span[2]"

    # time.sleep(12)
    # CLOSE_NOTIF_XPATH = "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[1]/div/div/div/div[1]/div/div"
    #
    # no_notif = driver.find_element(By.XPATH, CLOSE_NOTIF_XPATH)
    # no_notif.click()

        time.sleep(10)

        while True:
            actions = ActionChains(driver)
            actions.scroll_by_amount(delta_x=1000, delta_y=1500).perform()
            DESC_XPATH = f"/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div/section/div/div"
            map_posts = driver.find_element(By.XPATH, DESC_XPATH)
            codes = map_posts.text.splitlines()[7]
            level_name = map_posts.text.splitlines()[4]
            print(f"{level_name} - {codes}")
            time.sleep(2)

    except:
        secure = driver.find_element(By.XPATH, SECURE_PATH)
        secure.send_keys("Nibelic")

        next = driver.find_element(By.XPATH, FURTHER)
        next.click()

        time.sleep(2)
        password_input = driver.find_element(By.XPATH, PASSWORD_PATH)
        password_input.send_keys("avrK_2004")

        login_button = driver.find_element(By.XPATH, LOGIN_XPATH)
        login_button.click()

    time.sleep(15)



def add_new_info( reference, username, password):
    with open("../.env", "w") as file:
        file.write(f"{reference}={username}:{password}")
    print("File modified successfully")

def get_my_info(myID):
    savedDetails = os.environ.get(str(myID))
    if savedDetails is None:
        return {}
    else:
        return {
            "username": savedDetails.split(":")[0],
            "password": savedDetails.split(":")[1]
        }

def get_creative_map():
    CHROME_URL = r"E:\chromedriver-win64\chromedriver.exe"
    URL = "https://twitter.com/FGCreativeMaps"
    driver = Chrome(service=Service(CHROME_URL))
    driver.get(URL)
    time.sleep(5)
    actions = ActionChains(driver)
    while True:
        actions.scroll_by_amount(delta_x=1000, delta_y=1500).perform()
        DESC_XPATH = f"/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div/section/div/div"
        map_posts = driver.find_element(By.XPATH, DESC_XPATH)
        codes = map_posts.text.splitlines()[7]
        level_name = map_posts.text.splitlines()[4]
        level_code_pattern = r"\d{4}-\d{4}-\d{4}"
        level_code = re.search(level_code_pattern, map_posts.text)
        if level_code:
            print("Found ", level_code.group())
        print(f"{level_name} - {codes}")

        time.sleep(2)


username = os.environ.get("NAME")
password = os.environ.get("PASSWORD")

authenticate_me(username, password)