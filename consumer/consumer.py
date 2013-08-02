#coding=utf-8
#!/bin/python
"""
=================================================================
 @FileName:   Consumer 
 @author  :   houbolin<houbl@foxmail.com>
 @descrption: 添加任务到队列中
 @
=================================================================
"""
import beanstalkc
import logging
import logging.handlers
import os
import sys
import confManage

def log(message,logName):
    logger.info(message)

def start():
	beanstalk = beanstalkc.Connection(confManage.host(),confManage.port() )
	beanstalk = beanstalkc.use();
	job = ''
	"""
		produce在set消息时,必须指定消息体和consumer，队列名
		consumer负责解析消息		
	"""
	while(job is not None):
		job = beanstalk.reserve( RESERVE_TIMEOUT )
		print job.body

def _init_():
	logger.setLevel(logging.INFO)
	rh=logging.handlers.TimedRotatingFileHandler('consumer.log','D')
	fm=logging.Formatter("%(asctime)s  %(levelname)s - %(message)s","%Y-%m-%d %H:%M:%S")
   	rh.setFormatter(fm)
	logger.addHandler(rh)

if __name__ == '__main__':
	try:
		logger = logging.getLogger()
		_init_()
		start()
	except Exception,err:
		print "Exception: " , err
		
