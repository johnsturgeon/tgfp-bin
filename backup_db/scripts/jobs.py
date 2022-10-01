""" Starting point, this is loaded first by the scheduler """
import logging
import os
import schedule
import sentry_sdk
from . import back_up_db

sentry_sdk.init(
    dsn=os.getenv('SENTRY_DSN_TGFP_BIN'),
    traces_sample_rate=1.0
)
logging.basicConfig(level=logging.INFO)


def load():
    """ Load the schedule """
    logging.info("Loading the db backup schedule")
    schedule.every(30).minutes.do(back_up_db)
