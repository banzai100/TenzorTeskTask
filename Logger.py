import logging

logging.basicConfig(level=logging.INFO, filename="test.log", encoding="utf-8", filemode="w",
                    format='%(asctime)s - %(levelname)s - %(message)s')


class Logger:
    @staticmethod
    def info(message):
        logging.info(message)

    @staticmethod
    def error(message):
        logging.error(message)
