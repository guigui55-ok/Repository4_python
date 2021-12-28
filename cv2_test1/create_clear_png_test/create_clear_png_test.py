
import traceback
import import_init


def main():
    try:        
        logger = import_init.initialize_logger_new()

        return
    except:
        traceback.print_exc()