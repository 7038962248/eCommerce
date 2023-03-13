import logging

class LogGen:
    @staticmethod
    def loggen():
        logging.basicConfig(filename=".\\Logs\\automation.log",
                            format='%(asctime)s: %(levelname)s: %(message)s:', datefmt='%m/%d/%Y')

        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger


#1st create logger : -->  logger = logging.getLogger(‘demologger’)
                   #  ->  logger.setLevel(logging.INFO)

# 2 .creating handler :
#         For Stream Handler,
#         consoleHandler = logging.StreamHandler()
#         consoleHandler.setLevel(logging.INFO)
#
#         For File Handler,
#         fileHandler = logging.FileHandler(‘test.log’)
#         fileHandler.setLevel(logging.INFO)

#     3.   formatter = logging.Formatter(‘%(asctime)s – %(name)s – %(levelname)s:%(message)s’, datefmt=’%d/%m/%Y %I:%M:%S %p’)

 # 4. Adding format to handler
                 #  ----->       consoleHandler.setFormatter(formatter)

# 5 . adding handler object to  the logger
                 #  --- > logger.addHandler(fileHandler)
                  # ---- > logger.addHandler(streamHandler)

# 6 . writing the log massage
#       --->  logger.debug(‘debug message’)
#       --->  logger.info(‘info message’)
#       --->  logger.warn(‘warn message’)
#       --->  logger.error(‘error message’)
#       --->  logger.critical(‘critical message’)