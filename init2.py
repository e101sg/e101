# -*- coding: utf-8 -*-
import selenium.webdriver as webdriver
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.keys import Keys
from time import sleep

print ('this is test')
browser = webdriver.Firefox()

browser.get('http://www.proprofs.com/survey/stats/?title=tm54n&shr-id=a22c0d0970ca238804d1c5e8cc270a4c&oeq=946003f97ccc52d5d3b54ac0ec31bbfc')

# Save the window opener (current window, do not mistaken with tab... not the same)
main_window = browser.current_window_handle


# Put focus on current window which will, in fact, put focus on the current visible tab
#browser.switch_to_window(main_window)
#driver.manage().window().maximize()
browser.maximize_window()

# do whatever you have to do on this page, we will just got to sleep for now
sleep(20)

# Close current tab
# browser.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 'W')

# Put focus on current window which will be the window opener
#browser.switch_to_window(main_window)
print ('last step')
browser.close() #closes new tab