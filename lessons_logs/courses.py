import logging
from logging import handlers
from datetime import time
#print Level oreder
print(f'Debug : {logging.DEBUG}\n info : {logging.INFO}\n Warn : {logging.WARN}\n Error : {logging.ERROR}\n Critical :{logging.CRITICAL}')

#default level
print(f' Default logger :{logging.getLogger()}\t default level : {logging.getLogger().getEffectiveLevel()}')
#set new level
logging.getLogger().setLevel(logging.DEBUG)
#creat new logger
dev_logger=logging.getLogger('team dev')
#creat file handler
file_logs=logging.FileHandler('app.log')
# creat time rotate file handler
file_rotate=handlers.TimedRotatingFileHandler('dev.log',when='w1',interval=1,backupCount=7,atTime=time(1,0,0))

file_rotate.suffix='%Y_%m_%d'

formatter=logging.Formatter(fmt='%(asctime)s - %(name)s - %(levelname)s - %(module)s - %(message)s')
#apply formatter to file
file_logs.setFormatter(formatter)
file_rotate.setFormatter(formatter)
#attache file to logger
dev_logger.addHandler(file_logs)
dev_logger.addHandler(file_rotate)
for i in range(10):
    dev_logger.warning(f'from dev team {i}')
logging.error('Error msg')
logging.info('info msg')