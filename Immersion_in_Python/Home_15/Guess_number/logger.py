import logging

FORMAT = '{asctime} - {levelname} - {funcName} - {msg}'
logging.basicConfig(filename='guess_logger.log',
                    level=logging.INFO,
                    encoding='utf-8',
                    style='{',
                    format=FORMAT)
logger = logging.getLogger(__name__)

