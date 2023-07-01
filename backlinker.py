import json,requests,re,sys

from past.builtins import raw_input

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
  with open("urlbacklinks.json", "r") as file:
    data = json.loads(file.read())
    domainsfile = open("domains.txt", "r")
    domains = domainsfile.readlines()
    for backlink in data:
      for domain in domains:
        url = backlink['url'].replace("h4link.duckdns.org", domain.replace('\n', ''))
        try:
          r = requests.get(url).status_code
        except KeyboardInterrupt:
          sys.exit()
        except Exception as error:
          print('Error: ', error)
        except:
          r = "time out"
        print(domain.replace('\n', '') + " => Backlink Eklendi ==> "+re.search('http:\/\/.*?\/', url).group(0).replace("/", "").replace("http:","") + " status: "+str(r))
except Exception as error:
  print('Error: ', error)
except:
  print("\n\n => exit\n")
