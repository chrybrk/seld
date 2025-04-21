from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from time import sleep
import requests 

image_query = input("Query: ")
if (image_query == ""):
    print("What the cake? No input? :<")
    exit(1)

max_download_range = 10
_max_download_range = input("Max download image range (default 10): ")
if _max_download_range != "":
    max_download_range = int(_max_download_range)

save_path = input("Save path: ")
if (save_path == ""):
    print("What the cake? No input? :<")
    exit(1)

iteration = int(input("Max iterations: "))

print("[INFO]: opening driver")
driver = webdriver.Firefox()
driver.get("https://www.duckduckgo.com/")
sleep(5)

print("[INFO]: getting search box...")
element_search_box = driver.find_element(By.ID, "searchbox_input")
element_search_box.send_keys(image_query, Keys.ENTER)
sleep(5)

print("[INFO]: finding nav bar...")
elements_nav_bar = driver.find_elements(By.CLASS_NAME, "kFFXe30DOpq5j1hbWU1q");
driver.get(elements_nav_bar[1].get_attribute("href"))
sleep(5)

links = []
while iteration >= 0:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    sleep(1)

    image_container = driver.find_elements(By.CLASS_NAME, "SZ76bwIlqO8BBoqOLqYV")
    for image in image_container:
        image_tag = image.find_element(By.CSS_SELECTOR, "img")
        image_src = image_tag.get_attribute("src")
        links.append(image_src)

    if len(links) >= max_download_range:
        break

    iteration -= 1

print("[INFO]: downloading images")
for i in range(len(links)):
    data = requests.get(links[i]).content
    with open(save_path + str(i)+".png", "wb") as f:
        f.write(data)

print("[INFO]: done. exiting now.")
driver.close()
