#coding:utf-8
import logging
import logging.config
import logging.handlers

logging.config.fileConfig("logger.conf")

if __name__=="__main__":
    logger1=logging.getLogger('exmoles')#如果填写logger的name 在配置文件中没有，则调用logger_root
    logger2=logging.getLogger('log02')#调用logger_log02
    #logger1.error("error")
    logger2.error("error messages")