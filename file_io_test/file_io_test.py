import os
import file_io_util.file_io
import logger_init

def main():
    logger = logger_init.initialize_logger()
    file_name = 'test.txt'
    directory = os.getcwd()
    path = directory + '\\' + file_name    
    logger.info('path = '+ path)

    cio = file_io_util.file_io.file_io(
        logger,path
    )
    data = ''
    if (os.path.isfile(path)):
        logger.info('file path is exists')
        data = cio.read(path)
        logger.info('read data:\n' + data)
        logger.info('---------------------------------')
    else:
        logger.info('file path is not found')
        data = 'test write_append'
        cio.write_append(data,path)

if __name__ == '__main__':
    main()