import time

from xmlxl import app, celery
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)

@celery.task
def test_task(n1, n2):
    time.sleep(10)
    logger.info("Adding two numbers")
    return n1 + n2
    
# Linux commands to run:
# celery -A xmlxl.celery_test:celery worker --loglevel=INFO -f LOGFILE --logfile=LOGFILE
# flask run --host=0.0.0.0
# sudo rabbitmq-server -detched
# systemctl status rabbitmq-server.service

