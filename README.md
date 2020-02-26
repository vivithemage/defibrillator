# 502-defibrillator

If a server has a 502 error, this does it's best to bring it back to life.

LEMP stacks can sometimes return 502 errors and this can occur for a variety of reasons. The purpose of this is to essentially try to get rid of the error and bring the server back to life until someone can investigate the issue further.

Initially the plan is to just to monitor the site and reboot nginx and php-fpm if it falls over. Some potential future enhancements would be to fix nginx/php-fpm configs automatically but it's just monitor and reboot for the moment.

###Coming soon!
