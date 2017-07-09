import logging


def make_logger(output: str) -> logging.Logger:
    """
    Make logger.
    :param output: select output
    :return logger:
    """
    formatter = logging.Formatter("%(asctime)s;%(levelname)s;%(message)s",
                                  "%Y-%m-%d %H:%M:%S")
    logger = logging.getLogger('war-wmts')
    logger.setLevel(logging.DEBUG)

    if output == 'stdout':
        sh = logging.StreamHandler()
        sh.setFormatter(formatter)
        logger.addHandler(sh)
    else:
        fh = logging.FileHandler(output)
        fh.setFormatter(formatter)
        logger.addHandler(fh)

    return logger

