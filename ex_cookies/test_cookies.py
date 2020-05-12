from selenium import webdriver

if __name__=="__main__":
    browser = webdriver.Chrome(executable_path="C:/chromedriver/chromedriver.exe")
    browser.get("http://www.example.com")
    # now we will create a cookie
    # this is a data of my basic cookie
    cookie = {"name": "ex", "path": "/", "value": "value" }
    # we will set our cookie into th browser
    browser.add_cookie(cookie)
    # now we know se code work but we want to check the
    # cookie into our browser
    print(browser.get_cookies())
    # we close the browser after
    browser.quit()