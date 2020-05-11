# User Agent

## How to use User Agent with Selenium:
We need a Library option:
```
from selenium.webdriver.chrome.options import Options
```
Call Option:
```
opts = Options()
```
Add user Agent ex:
```
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'
opts.add_argument("user-agent=" + user_agent)
```
I call my browser with my new option
```
browser = webdriver.Chrome(chrome_options=opts, executable_path='C:/chromedriver/chromedriver.exe')
```
Check my User agent in chromedrive :
```
ug_verif = browser.execute_script("return navigator.userAgent;")
```

## ex_useragent

This example do a difference with user agent set and without user agent
Result is test1:
```
test1 Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36
```
Result is test2:
```
test2 Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/81.0.4044.138 Safari/537.36
{'Chrome/78.0.3904.97', 'HeadlessChrome/81.0.4044.138'}
```

Difference : 
```
{'Chrome/78.0.3904.97', 'HeadlessChrome/81.0.4044.138'}
```

### Explanation :
1) I have one version in 78.0 and the second in 81.0

2) Headless is because of the function :
```
 opts.add_argument('headless')
```
this function run my Chrome without to publish my browser on the front 
it s run this in background 