import json,requests,re,sys

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium_stealth import stealth


options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_argument("--headless")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
driver = webdriver.Chrome(
    options=options)

stealth(driver,
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
        )

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
    for link in urls:
      start_time = time.time()
      string = link.replace("\n", '')
      array = string.split(' | ')
      url = array[1]
      try:
        r = requests.get(url).status_code
        print("-----------------------------------------")
        print(url)
        print("Status: " + str(r))
        driver.get(url)
        # driver.save_screenshot(str(time.time()) + ".png")
        elapsed = "%s seconds" % (time.time() - start_time)
        print("Done in " + elapsed)
        print("-----------------------------------------")
      except Exception as error:
        print('Error: ', error)
      except:
        r = "time out"
except Exception as error:
  print('Error: ', error)
except:
  print("\n\n => exit\n")
