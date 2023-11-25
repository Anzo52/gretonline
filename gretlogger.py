import logging

def setup_logger(name, level=logging.INFO):
    """Create and configure a logger."""

    # Create a logger
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Create a console handler and set the level
    ch = logging.StreamHandler()
    ch.setLevel(level)

    # Create formatter and add it to the handler
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)

    # Add the handler to the logger
    logger.addHandler(ch)

    return logger