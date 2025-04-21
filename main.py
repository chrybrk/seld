from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
import requests 

image_query = input("Query: ")
if (image_query == ""):
    print("What the cake? No input? :<")
    exit(1)

max_download_range = 10
max_download_range = int(input("Max download image range (default 10): "))

save_path = input("Save path: ")
if (save_path == ""):
    print("What the cake? No input? :<")
    exit(1)

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

print("[INFO]: capturing all the images")
image_container = driver.find_elements(By.CLASS_NAME, "SZ76bwIlqO8BBoqOLqYV")

print("[INFO]: downloading images")
counter = 0
while counter < len(image_container) and counter <= max_download_range:
    div = image_container[counter]
    image_tag = div.find_element(By.CSS_SELECTOR, "img")
    image_src = image_tag.get_attribute("src")
    data = requests.get(image_src).content
    with open(save_path + str(counter)+".png", "wb") as f:
        f.write(data)
    counter += 1

print("[INFO]: done. exiting now.")
driver.close()
