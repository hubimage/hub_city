from hub_city.app import logger


def log_error(msg):
    return logger.lg.get_log.fatal(msg)


def log_fatal(msg):
    return logger.lg.get_log.fatal(msg)


def log_warn(msg):
    return logger.lg.get_log.warn(msg)

