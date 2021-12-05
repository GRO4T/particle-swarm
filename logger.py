import logging


def configure_logging():
    logging.basicConfig(filename="default.log",
                        format='%(asctime)s %(levelname)s %(message)s')
