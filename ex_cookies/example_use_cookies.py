# coding: utf-8
import json
from selenium import webdriver

def loadjsoncookie(jsoncookie, browser):
    with open(jsoncookie, 'r') as bloc:
        distros_dict = json.load(bloc)
    for i in range(0, len(distros_dict)):
        browser.add_cookie(distros_dict[i])

def exportjsoncookie(filejson, browser):
    print(browser.get_cookies())
    my_details = browser.get_cookies()
    with open(filejson, 'w') as json_file:
        json.dump(my_details, json_file, sort_keys=True, indent=4)

if __name__=="__main__":
    browser = webdriver.Chrome(executable_path='C:/chromedriver/chromedriver.exe')
    browser.get("http://www.example.com")
    loadjsoncookie("cookies.json",browser)
    exportjsoncookie("cookies.json",browser)
    #  Deletes all cookies
    browser.delete_all_cookies()
    browser.quit()