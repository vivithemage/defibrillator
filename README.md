# 502-defibrillator

## Overview

If an nginx server returns a non 200 code, this does it's best to bring it back to life.

LEMP stacks can sometimes return non 200 values such as 502 errors and this can occur for a variety of reasons. The purpose of this is to essentially try to get rid of the error and bring the server back to life until someone can investigate the issue further.

It works by installing a crontab that runs a script to check the server status. If a non 200 code is
returned, nginx, mysql and php-fpm are restarted.

## Usage

Install the necessary dependencies:

```shell
pip install -r requirements.txt
```

To install the crontab, replace the url with your own and run:

```shell
python src/install_cron.py https://www.example.com
```

It's important this returns a 200 code. So if you put http://example.com and it comes up with a 301
redirect to www.example.com it's going to deem that as down and reboot the server.


## Future enhancements

Initially the plan is to just to monitor the site and reboot nginx and php-fpm if it falls over. Some potential future enhancements would be to fix nginx/php-fpm configs automatically but it's just monitor and reboot for the moment.
