import time
from selenium import webdriver

browser = webdriver.Chrome()
link = raw_input("Enter site")
browser.get()
time.sleep(0.2)
button_click = browser.find_element_by_xpath("//*[contains(text(), 'text here)]")
#username = browser.find_element_by_xpath
count = 1
while button_click:
    button_click = browser.find_element_by_xpath("//*[contains(text(), 'text here)]")
    #fileW = open("filepath", "a")
    #fileW.write(browser.current_url + "\n") 
    #fileW.write
    button_click.click()
    count += 1
    print(count)
    time.sleep(0.2)

print('total count = ' + count)