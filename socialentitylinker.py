import json,requests,re,sys

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
  with open("socialentitylinks.txt", "r") as file:
    urls = file.readlines()
    print(urls)
    for link in urls:
      print(link)
      try:
        r = requests.get(link.replace("\n", '')).status_code
      except KeyboardInterrupt:
        sys.exit()
      except:
        r = "time out"
      print(link + " => Ping ==> "+re.search('http:\/\/.*?\/', link).group(0).replace("/", "").replace("http:","") + " status: "+str(r))
except:
  print("\n\n => exit\n")
