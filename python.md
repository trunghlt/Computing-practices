Python practices:
=================

## [PEP8](http://www.python.org/dev/peps/pep-0008/) & [Google practices](http://google-styleguide.googlecode.com/svn/trunk/pyguide.html)

## [Boilerplate](python/boilerplate.py)

## [Log configuration template](python/log.cfg)

## Pylint
  Copy [pylintrc](https://github.com/trunghlt/Computing-practices/blob/master/python/pylintrc) to ~/.pylintrc or /etc/pylintrc for loose configuration of pylint.
  Details:

    Messages currently disabled:
    W0614: Unused import %s from wildcard import
    
    This is not that bad and we depend on other 3rd party components heavily using it (pylons).
    W0611: Unused import %s
    
    Cascade from the previous item.
    C0301: Line too long (%s/%s)
    
    Last thing we will have a look to? ;)
    R0903: Too few public methods (%s/%s)
    
    Sqlalchemy data model is almost only members definition, doesn't really make any sense. Also, what's really wrong with data container objects?
    W0401: Wildcard import %s
    This is not that bad and we depend on other 3rd party components heavily using it (pylons).

  Credit to Gullaume Gardey for the config file.
  
## [Turning Vim into a modern Python IDE](http://sontek.net/turning-vim-into-a-modern-python-ide)
  
## locale:

### Problem: All locale settings in cron jobs are set to "POSIX" rather than user's default in Ubuntu.
  - Solution: What you can do instead is create (if not already present) the file /etc/environment and add the following line:
LANG=en_US.UTF-8 
  - Tested environment: haven't tested yet
  - In python:
  
    > import locale

    > locale.setlocale("en_US", "UTF-8")

  - [More info](http://www.logikdev.com/2010/02/02/locale-settings-for-your-cron-job/)

  