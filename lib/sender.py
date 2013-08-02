#coding=utf-8
#!/bin/python
"""
=================================================================
 @FileName:   Sender
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
import bdqueue 

def start( filename):
	for line in open(filename):
		cuid = line.strip('\n\t')
		bdqueue.addTask( "datexx" ,cuid )

def log(message,logName):
    logger.info(message)

def _init_():
	logger.setLevel(logging.INFO)
	rh=logging.handlers.TimedRotatingFileHandler('log/'+filename,'D')
	fm=logging.Formatter("%(asctime)s  %(levelname)s - %(message)s","%Y-%m-%d %H:%M:%S")
   	rh.setFormatter(fm)
	logger.addHandler(rh)

if __name__ == '__main__':
	try:
		filename = sys.argv[1]
		logger = logging.getLogger()
		_init_()
		if( os.path.exists( filename ) == False ):
			raise SendException('file not exists' + filename)
		start( filename )
	except Exception,err:
		print "Exception: " , err
		
