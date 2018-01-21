import logging

#create logger
logger=logging.getLogger('simple_example')
#logger=logging.basicConfig(filename='example.log',filemode='w')
logger.setLevel(logging.DEBUG)


#create console handler and set level to debug

ch=logging.StreamHandler()
ch.setLevel(logging.DEBUG)

#create formatter
formatter=logging.Formatter('%(asctime)s-%(name)s-%(levelname)s-%(message)s')

#create log file
fh=logging.FileHandler('simple_logging_module.log','w')
#add formatter to ch
ch.setFormatter(formatter)

#add ch and fh to logger
logger.addHandler(ch)
logger.addHandler(fh)
# application
logger.debug('debug')
logger.info('info')
logger.error('error')