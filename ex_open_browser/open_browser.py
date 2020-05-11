from selenium import webdriver

if __name__=="__main__":
    browser = webdriver.Chrome(executable_path="C:/chromedriver/chromedriver.exe")
    browser.get("http://www.example.com")
    browser.quit()