import module_b

import sample_logger
logger = sample_logger.SampleLogger()

logger.info('module_a')

# module_b のDEBUGはここで変更できる
module_b.DEBUG = True
module_b.DEBUG = False

# module_a から module_b へ値を代入できる
module_b.logger = logger
module_b.logger.debug = False
module_b.execute_test_b()

# 上記の変更は保持される
logger.debug = True
logger.info('module_a 2')