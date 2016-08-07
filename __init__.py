# -*- coding: utf-8 -*-
import selenium.webdriver as webdriver
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.keys import Keys
from time import sleep

print ('this is test')
browser = webdriver.Firefox()
browser.get('http://www.proprofs.com/survey/stats/?title=tm54n')
#browser.execute_script('''window.open("http://bings.com","_blank");''')
#first_result = ui.WebDriverWait(browser, 15).until(lambda browser: browser.find_element_by_class_name('rc'))
#first_link = first_result.find_element_by_tag_name('a')

# Save the window opener (current window, do not mistaken with tab... not the same)
main_window = browser.current_window_handle

# Open the link in a new tab by sending key strokes on the element
# Use: Keys.CONTROL + Keys.SHIFT + Keys.RETURN to open tab on top of the stack
#first_link.send_keys(Keys.CONTROL + Keys.RETURN)

# Switch tab to the new tab, which we will assume is the next one on the right
#browser.find_element_by_tag_name('body').send_keys(Keys.CONTROL + t)

# Put focus on current window which will, in fact, put focus on the current visible tab
browser.switch_to_window(main_window)

# do whatever you have to do on this page, we will just got to sleep for now
sleep(2)

# Close current tab
browser.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 'W')
#curWindowHndl = browser.current_window_handle
#elem.send_keys(Keys.CONTROL + Keys.ENTER) #open link in new tab keyboard shortcut
#sleep(5) #wait until new tab finishes loading
#browser.switch_to_window(browser.window_handles[1]) #assuming new tab is at index 1
#browser.close() #closes new tab
#browser.switch_to_window(curWindowHndl)

# Put focus on current window which will be the window opener
browser.switch_to_window(main_window)
print ('last step')
browser.close() #closes new tab