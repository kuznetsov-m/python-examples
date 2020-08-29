from selenium import webdriver

address = 'https://google.com'

# chromedriver src: https://sites.google.com/a/chromium.org/chromedriver/downloads
driver = webdriver.Chrome('bin/84/chromedriver')
driver.header_overrides = {
    # 'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36',
}
driver.get(address)

with open('page.html', 'a') as f:
    f.write(driver.page_source)