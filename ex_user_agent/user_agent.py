from selenium import webdriver
from selenium.webdriver.chrome.options import Options

if __name__=="__main__":
    # we want to change the user agent
    opts = Options()
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_4) AppleWebKit/536.30.1 (KHTML, like Gecko) Version/6.0.5 Safari/536.30.1'
    opts.add_argument("user-agent="+user_agent)
    browser = webdriver.Chrome(options=opts ,executable_path="C://chromedriver/chromedriver.exe")
    browser.get("http://www.example.com")
    check_useragent = browser.execute_script("return navigator.userAgent;")
    print("test user agent", check_useragent)
    browser.quit()
