Python practices:
=================

## [Boilerplate](python/boilerplate.py)

## [Log configuration template](python/log.cfg)

## locale:

### Problem: All locale settings in cron jobs are set to "POSIX" rather than user's default in Ubuntu.
  - Solution: What you can do instead is create (if not already present) the file /etc/environment and add the following line:
LANG=en_US.UTF-8 
  - Tested environment: haven't tested yet
  - [More info](http://www.logikdev.com/2010/02/02/locale-settings-for-your-cron-job/)

  