import logging

logs_dir = 'logs'
stream_logs_level = logging.ERROR
file_logs_level = logging.DEBUG

# create logger with 'spam_application'
logger = logging.getLogger('my_app')
logger.setLevel(logging.DEBUG)
# create file handler which logs even debug messages
fh = logging.FileHandler(f'{logs_dir}/my_app.log')
fh.setLevel(file_logs_level)
# create console handler with a higher log level
ch = logging.StreamHandler()
ch.setLevel(stream_logs_level)
# create formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)
# add the handlers to the logger
logger.addHandler(fh)
logger.addHandler(ch)

logger.debug('debug message')
logger.info('info message')
logger.warning('warning message')
logger.error('error message')
logger.fatal('fatal message')