from selenium import webdriver
import time

browser=webdriver.Firefox()
browser.get('https://mail.google.com')
elem=browser.find_element_by_css_selector('#Email')
elem.send_keys('apjneeraj')
elem2=browser.find_element_by_css_selector('#next')
elem2.click()
time.sleep(3)
elem_pass=browser.find_element_by_css_selector('#Passwd')
elem_pass.send_keys('delete^!!^')
submit=browser.find_element_by_css_selector('#signIn')
submit.click()
verif=browser.find_element_by_css_selector
verif=browser.find_element#totpPin
verif=browser.find_element_by_css_selector('#totpPin')
verif.send_keys('492551')
done=browser.find_element_by_css_selector('#submit')
done.click()