import logging

import logging

class CustomFormatter(logging.Formatter):

    grey = "\x1b[38;20m"
    yellow = "\x1b[33;20m"
    red = "\x1b[31;20m"
    bold_red = "\x1b[31;1m"
    reset = "\x1b[0m"
    format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s (%(filename)s:%(lineno)d)"

    FORMATS = {
        logging.DEBUG: grey,
        logging.INFO: grey,
        logging.WARNING: yellow,
        logging.ERROR: red,
        logging.CRITICAL: bold_red
    }

    def format(self, record):
        log_color = self.FORMATS.get(record.levelno)
        log_fmt = log_color + self._fmt + self.reset
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)

logger = logging.getLogger("json_schema_filter")
logger.setLevel(logging.INFO)

handler = logging.StreamHandler()
handler.setLevel(logging.INFO)
handler.setFormatter(CustomFormatter(fmt="[%(name)s] %(levelname)s: %(message)s"))

logger.addHandler(handler)