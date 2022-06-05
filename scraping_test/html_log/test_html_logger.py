
import pathlib,sys
path = str(pathlib.Path(__file__).parent.parent)
sys.path.append(path)
import import_init

from html_logger import HtmlLogger
from common_utility.log_util.logging_util import MyLogger,LoggerUtility

def html_log_test():
    import pathlib,os
    log_dir = str(pathlib.Path(__file__).parent.joinpath('test_log'))
    css_path = os.path.join(log_dir, 'log.css')
    css_path = 'log.css'
    if not os.path.exists(log_dir): os.mkdir(log_dir)
    log_path = os.path.join(log_dir,'testlog.log')
    logger = HtmlLogger('test_html_logger',log_dir)
    logger.reset_log_file()
    logger.info('test info')
    logger.set_css_path(css_path)
    logger.finish_to_create_html()
    return

if __name__ == '__main__':
    html_log_test()
