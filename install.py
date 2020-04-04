import os
import sys

#if not sys.argv[1]:
  #print ("Please enter the url to check")

#write out current crontab
os.system("crontab -l > current_cron.txt")

cwd = os.getcwd()

cron_command = "source " + str(cwd) + "/env/bin/activate;"
cron_command = cron_command + "python3 " + str(cwd) + "/src/main.py " + sys.argv[1] + ";"

print(cron_command)
#echo new cron into cron file
#os.system("echo \"" + cron_command +  "\" >> current_cron.txt")

#install new cron file
#os.system("crontab current_cron.txt")

# Now delete it
os.system("rm current_cron.txt")
