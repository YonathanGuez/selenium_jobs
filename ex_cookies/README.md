# Cookies

## How to use Cookies with Selenium:
we must open a page before to set cookies
```
driver.get("http://www.example.com")
```
We can now add a cookie in the browser
```
driver.add_cookie({'name' : 'foo', 'value' : 'bar'})
```
We can get all cookies or simple one 
```
driver.get_cookies()
driver.get_cookie('name')
```
We can delete all Cookies
```
driver.delete_all_cookies()
```
## ex_cookies
In this example example_use_cookies.py we build two functions

Load a Jsonfile into my browser :
```
loadjsoncookie(jsoncookie, browser)
```
Export my cookies into a new jsonfile :
```
exportjsoncookie(filejson, browser)
```
   