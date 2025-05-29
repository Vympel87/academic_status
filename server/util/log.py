import sys
import logging
from dotenv import load_dotenv
import os

def log_begin():
    load_dotenv()

    log_format = os.getenv("LOGGING_FORMAT")

    # Buat logger root
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.INFO)

    # Handler stdout untuk INFO dan WARNING
    out_handler = logging.StreamHandler(sys.stdout)
    out_handler.setLevel(logging.INFO)
    out_handler.addFilter(lambda record: record.levelno < logging.ERROR)
    out_handler.setFormatter(logging.Formatter(log_format))
    root_logger.addHandler(out_handler)

    # Handler stderr untuk ERROR ke atas
    err_handler = logging.StreamHandler(sys.stderr)
    err_handler.setLevel(logging.ERROR)
    err_handler.setFormatter(logging.Formatter(log_format))
    root_logger.addHandler(err_handler)

    # Redam log noisy
    logging.getLogger("httpx").setLevel(logging.ERROR)
    logging.getLogger("uvicorn.error").name = "uvicorn"
