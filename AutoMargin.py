#   type these two lines into console to start the debugger session
#   cd C:\Program Files\Google\Chrome\Application
#   chrome.exe --remote-debugging-port=8989 --user-data-dir="C:\Users\lawrence.butler\Documents\Chrome Data"

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support import expected_conditions as EC
import time
import math
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
n=1

s=Service("C:\Users\lawrence.butler\Downloads\chromedriver_win32\chromedriver.exe")
opt=Options()
opt.add_experimental_option("debuggerAddress","localhost:8989")
driver=webdriver.Chrome(service=s,options=opt)
action=ActionChains(driver)
#driver.implicitly_wait(5)


client_stats=driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div/div/div/div[3]/div[2]/div[1]/table/thead/tr/th[3]/div/div/a[1]")
client_stats.click()
# campaign_number=driver.find_element(By.XPATH,'/html/body/div[1]/span/div/div[4]/div[4]/div[1]/div[9]/span')
# No=int(campaign_number.text)
# print(No)
# def set_margin(X):
#     global n
#     yday_imps=float(str((driver.find_element(By.XPATH,'/html/body/div[1]/span/div/div[3]/div[6]/div/div/div[1]/div['+str(X)+']/div/div/div/div[1]/div[2]/div/div[2]/div[1]/span')).text).replace(",",""))
#     if yday_imps>0:
#         clicks_button=driver.find_element(By.XPATH,'/html/body/div[1]/span/div/div[3]/div[6]/div/div/div[1]/div['+str(X)+']/div/div/div/div[1]/div[1]/div[1]/button[2]').text
#         campaign=driver.find_element(By.XPATH,'/html/body/div[1]/span/div/div[3]/div[6]/div/div/div[1]/div['+str(X)+']/div/header/h6/div/div[1]/a')
#         driver.execute_script("arguments[0].scrollIntoView();", campaign)
#         campaign.click()
#         driver.switch_to.window(driver.window_handles[1])
#         numbers_above_save = driver.find_element(By.XPATH,'//*[@id="client-stat-details"]/div[5]/div[1]/div[2]/div[2]/div[2]/label')
#         driver.execute_script("arguments[0].scrollIntoView();", numbers_above_save)
#         time.sleep(0.5)
#         if clicks_button != "Complete Views":
#             cpm = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div/div[11]/div[3]/div/div/div/div[1]/div/div[4]/div/div/form/fieldset/div[1]/div/table[3]/tbody/tr/td/div/div[3]/table/tbody/tr[2]/td/div/button')
#             cpm.click()
#             time.sleep(2)
#             cpm.click()
#         else:
#             cpcv=driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div/div[11]/div[3]/div/div/div/div[1]/div/div[4]/div/div/form/fieldset/div[1]/div/table[4]/tbody/tr/td/div/div[3]/table/tbody/tr[2]/td/div/button')
#             cpcv.click()
#             time.sleep(2)
#             cpcv.click()
#         save=driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div/div[11]/div[3]/div/div/div/div[1]/div/div[2]/div/div/form/fieldset/div[2]/button[2]')
#         save.click()
#         sure=driver.find_element(By.XPATH,'/html/body/div[8]/div[7]/div/button')
#         time.sleep(2)
#         sure.click()
#         time.sleep(1)
#         driver.close()
#         driver.switch_to.window(driver.window_handles[0])
#         n+=1
#
# for y in range (1,No,1):
#     set_margin(y)
#     print(y)