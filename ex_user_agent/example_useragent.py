from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def test1():
    print("test1 : With modification of my user agent")
    opts = Options()
    user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_4) AppleWebKit/536.30.1 (KHTML, like Gecko) Version/6.0.5 Safari/536.30.1"
    # user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'
    opts.add_argument("user-agent=" + user_agent)
    opts.add_argument('headless')
    browser = webdriver.Chrome(chrome_options=opts, executable_path='C:/chromedriver/chromedriver.exe')
    browser.get("http://www.example.com")
    ug_verif = browser.execute_script("return navigator.userAgent;")
    print("test1", ug_verif)
    browser.quit()
    return ug_verif

def test2():
    print("test2 : Without user agent")
    opts = Options()
    opts.add_argument('headless')
    browser = webdriver.Chrome(chrome_options=opts, executable_path='C:/chromedriver/chromedriver.exe')
    browser.get("http://www.example.com")
    ug_verif = browser.execute_script("return navigator.userAgent;")
    print("test2", ug_verif)
    browser.quit()
    return ug_verif

if __name__=="__main__":
    t1 = set(test1().split(" "))
    t2 = set(test2().split(" "))
    print(t1 ^ t2)
