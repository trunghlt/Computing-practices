#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
""" 

"""
import logging

log = logging.getLogger(__name__)

def main(verbose, argv):
    """ Do something :)

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
    config_path = pjoin(expanduser('~'), '.your_project_name')
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

