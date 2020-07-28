import logging.config
import os

import yaml


def setup_logging(default_path='config/logging.yaml', default_level=logging.INFO):
    """
    Setup yaml logging configuration
    """
    if os.path.exists(default_path):
        with open(default_path, 'rt') as file:
            config = yaml.safe_load(file.read())
        logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=default_level)
