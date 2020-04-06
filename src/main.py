import sys
import os
import time
import requests

class Defib:
  def __init__(self, url):
    self.url = url

  def is_live(self):
    try:
      r = requests.head(self.url)
      print(r.status_code) 
      return r.status_code == 200

    except requests.ConnectionError:
      return False

  def restart(self, service):
    os.system("sudo service " + service + " stop")
    os.system("sudo service " + service + " start")
    
  def restart_all(self):
    self.restart("nginx")
    self.restart("mysqld")
    self.restart("php7.0-fpm")

    time.sleep(60)

  def check(self):
    if not argv[1]:
      print("Please provide url to check.")
      exit()


  def run(self):
    if self.is_live():
      print("Online")
    else:
      self.restart_all()
      print("Offline, restarting nginx, php-fpm and mysqld")


defib = Defib(sys.argv[1])

defib.run()
