import traceback
import sys

def sample_function():
    return 1 / 0  # ゼロ除算エラーを意図的に発生させる

try:
    print()
    print('*****')
    sample_function()
except Exception:
    exc_type, exc_value, exc_traceback = sys.exc_info()
    from pathlib import Path
    traceback_details = {
        'filename': Path(exc_traceback.tb_frame.f_code.co_filename).name,
        'lineno': exc_traceback.tb_lineno,
        'name': exc_traceback.tb_frame.f_code.co_name,
        'type': exc_type.__name__,
        'message': str(exc_value),
    }
    error_msg = ("Error occurred in file: {filename}, function: {name}, at line: {lineno}. "
                 "Error type: {type}, message: {message}").format(**traceback_details)
    print(error_msg)
    error_msg_b = 'Error occurred in file: {filename}'.format(**traceback_details)
    error_msg_b += ', function: {name}, at line: {lineno}. '.format(**traceback_details)
    error_msg_b += 'Error type: {type}, message: {message} '.format(**traceback_details)