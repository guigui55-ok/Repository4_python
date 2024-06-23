

DEBUG = True
import sample_logger
logger = sample_logger.SampleLogger()

def _debug_print(value):
    if DEBUG:
        print(value)

def execute_test_b():
    b = 20
    _debug_print(b)
    logger.info(b)
    return b