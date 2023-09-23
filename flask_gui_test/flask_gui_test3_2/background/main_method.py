
if __name__ == '__main__':
    
    import sys
    from pathlib import Path
    path_str = str(Path(__file__).parent.parent)
    print(path_str)
    sys.path.append(path_str)
from flask_simple_logger import FlaskSimpleLogger


class ConstBackground:
    MODE_TEST = 1
    KEY_MODE_IMPUT = 'mode_input'
    KEY_LOGGER = 'logger'
    KEY_RESULT = 'result'

def add_annotation_type_logger(value)->FlaskSimpleLogger:
    logger:FlaskSimpleLogger = value
    return value

def execute_main(option_dict:dict):
    """
    """
    # logger:FlaskSimpleLogger = option_dict[ConstBackground.KEY_LOGGER]
    logger = add_annotation_type_logger(option_dict[ConstBackground.KEY_LOGGER])
    mode_input = option_dict[ConstBackground.KEY_MODE_IMPUT]
    ###
    if mode_input == ConstBackground.MODE_TEST:
        option_dict = execute_test(logger, option_dict)
        logger.add(f"モード {mode_input} が正常に実行されました。")
    else:
        logger.add(f"エラー：モード {mode_input} が見つかりませんでした。")
    ###
    option_dict.update({ConstBackground.KEY_LOGGER : logger})
    return option_dict



def execute_test(logger, option_dict:dict):
    import os
    logger = add_annotation_type_logger(logger)
    folder_input = option_dict['folder_input']

    try:
        logger.add(f"\nフォルダパス：{folder_input}")
        folder_name = os.path.basename(folder_input)
        logger.add(f"\nフォルダ名：{folder_name}")
        option_dict.update({ConstBackground.KEY_RESULT : folder_name})
    except Exception as e:
        logger.add(f"\nエラー：{str(e)}")
    
    option_dict.update({ConstBackground.KEY_LOGGER : logger})
    return option_dict