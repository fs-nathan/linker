import json,requests,re,sys

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
from selenium_stealth import stealth


# get proxies
options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_argument("--headless")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
driver = webdriver.Chrome(options=options)
driver.get("https://sslproxies.org/")

ips = [my_elem.get_attribute("innerHTML") for my_elem in WebDriverWait(driver, 5).until(EC.visibility_of_all_elements_located((By.XPATH, "//table[@class='table table-striped table-bordered']/tbody/tr/td[1]")))]
ports = [my_elem.get_attribute("innerHTML") for my_elem in WebDriverWait(driver, 5).until(EC.visibility_of_all_elements_located((By.XPATH, "//table[@class='table table-striped table-bordered']/tbody/tr/td[2]")))]
driver.quit()
proxies = []
for i in range(0, len(ips)):
    proxies.append(ips[i]+':'+ports[i])
proxies_len = len(proxies)
# print(proxies)
try:
  print("""
            _ ____             _    _ _       _             
           | |  _ \           | |  | (_)     | |            
 _   _ _ __| | |_) | __ _  ___| | _| |_ _ __ | | _____ _ __ 
| | | | '__| |  _ < / _` |/ __| |/ / | | '_ \| |/ / _ \ '__|
| |_| | |  | | |_) | (_| | (__|   <| | | | | |   <  __/ |   
 \__,_|_|  |_|____/ \__,_|\___|_|\_\_|_|_| |_|_|\_\___|_|   
                                              H4-cklinker - wmdark.com     
  """)
  with open("netsoltrademark_backlinks.txt", "r") as file:
    urls = file.readlines()


    for i in range(len(urls)):
      link = urls[i]
      start_time = time.time()
      string = link.replace("\n", '')
      array = string.split(' | ')
      index = array[0]
      url = array[1]
      try:
        selected_proxy = proxies[i % proxies_len]
        print("-----------------------------------------" + index)
        print("Proxy selected: {}".format(selected_proxy))
        print(url)
        proxy_config = {
           'http': 'http://' + selected_proxy,
           'https': 'http://' + selected_proxy,
        }
        r = requests.get(url).status_code
        print("status: ", str(r))
        elapsed = "%s seconds" % (time.time() - start_time)
        print("Done in " + elapsed)
        print("-----------------------------------------")
      except KeyboardInterrupt:
        sys.exit()
      except Exception as error:
        print('Error: ', error)
except Exception as error:
  print('Error: ', error)

