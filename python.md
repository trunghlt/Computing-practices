Python practices:
=================

## Boilerplate:
    #!/usr/bin/env python
    # -*- coding: utf-8 -*-
    import logging
  
    log = logging.getLogger(__name__)
  
    def main(verbose, argv):
        """
        Do something :)
        """
        log.debug("argv: {0}".format(argv))
        # ...
  
        return 0
  
    if __name__ == "__main__":
    
        import sys
        from os.path import expanduser, join as pjoin, splitext
        from ConfigParser import SafeConfigParser
        import logging.config
        from optparse import OptionParser
    
        # Configuration items
        config_path = pjoin(expanduser('~'), '.project')
        cfg = SafeConfigParser()
        cfg.read(pjoin(config_path, 'config'))
    
        # Logging configuration
        script_name, _ = splitext(__file__)
        logging.config.fileConfig(pjoin(config_path,
                                        'log',
                                        '%s.cfg' % script_name))
        # Basic config
        # logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')
    
        # Parse the command line for options/configurations
        # Usage message can be changed: OptionParser(usage='Usage: %prog [options] param1 params2')
        parser = OptionParser()
        parser.add_option('--verbose', dest='verbose', action='store_true')
        # ... add more options
    
        options, args = parser.parse_args()
    
        if len(args) != 1:
            parser.error('Invalid number of arguments')
    
        # example of usage
        if options.verbose:
            logging.info('Verbose mode activated')
    
        ret = main(options.verbose, args)
    
        sys.exit(ret)

## Log configuration template:
    [loggers]
    keys=root,project
    
    [handlers]
    keys=syslog,email,console,file
    
    [formatters]
    keys=default
    
    [handler_console]
    class=StreamHandler
    level=NOTSET
    formatter=default
    args=(sys.stdout,)
    
    [handler_syslog]
    class=logging.handlers.SysLogHandler
    level=DEBUG
    formatter=default
    args=('/dev/log', handlers.SysLogHandler.LOG_USER)
    
    [handler_email]
    class=logging.handlers.SMTPHandler
    level=ERROR
    formatter=default
    args=('localhost', '', [ 'SOMEONE@project.com' ], "Houston, we have a problem... no, just kidding!")
    
    [handler_file]
    class=FileHandler
    level=DEBUG
    formatter=default
    args=('debug.log',)
    
    [formatter_default]
    format='NAME_OF_YOUR_SCRIPT[%(filename)s:%(lineno)d]- %(asctime)s - %(levelname)s - %(message)s'
    
    [logger_root]
    level=DEBUG
    handlers=console,file
    
    [logger_project]
    level=DEBUG
    qualname=semetric
    handlers=console,file
    propagate=0

## locale:

### Problem: All locale settings in cron jobs are set to "POSIX" rather than user's default in Ubuntu.
  - Solution: What you can do instead is create (if not already present) the file /etc/environment and add the following line:
LANG=en_US.UTF-8 
  - Tested environment: haven't tested yet
  - [More info](http://www.logikdev.com/2010/02/02/locale-settings-for-your-cron-job/)

  