import timeit
import logging


logger = logging.getLogger(__name__)
f_handler = logging.FileHandler('file.log')
#logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
f_format = logging.Formatter('%(asctime)s - %(funcName)5s() - %(levelname)s - %(message)s')
f_handler.setFormatter(f_format)
logger.addHandler(f_handler)
logger.setLevel(logging.DEBUG)
#logger.info('Admin logged out')

