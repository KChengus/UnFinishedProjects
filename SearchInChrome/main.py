import webbrowser

from selenium import webdriver
from time import sleep

op = webdriver.ChromeOptions()
op.add_argument('headless')
driver = webdriver.Chrome(options=op)

classForWebsite = "yuRUbf"
input = input("Sök på: ").split(" ")
driver.get("https://www.google.com/search?q=" + "+".join(input))
sleep(2)
driver.find_element_by_xpath("//*[@id=\"L2AGLb\"]/div").click()
webpagesDiv = driver.find_elements_by_class_name(classForWebsite)
urlsForSearch = list()
for webpageDiv in webpagesDiv:
    urlForSearch = webpageDiv.find_element_by_tag_name("a").get_attribute("href")
    webbrowser.open(urlForSearch , new=2)
