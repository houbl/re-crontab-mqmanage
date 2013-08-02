#coding=utf-8
#!/bin/python
"""
=================================================================
 @FileName:   Conf 
 @author  :   houbolin<houbl@foxmail.com>
 @descrption: 队列配置服务 
 @
=================================================================
"""
from __future__ import division
import logging
import os
import sys
import psutil
import ConfigParser

RESERVE_TIMEOUT = 1
CONF_NAME = '../conf/consumer.ini'
DEFAULT_HOST = 'localhost'
DEFAULT_PORT = 14711	

def currentQuene():
	cf = ConfigParser.ConfigParser()
	cf.read( CONF_NAME )
	consumerConfig = cf.options("consumer")
	currentQuene = cf.get("consumer","currentQueue")
	if currentQueue is not None:
		return currentQueue
	
	return 'default'

def host():
	return DEFAULT_HOST

def port():
	return DEFAULT_PORT

def getConsumerCount():
	"""
		拿到系统当前CPU和内存使用情况
		根据配置计算当前能够启动多少个consumer
		具体算法是: 
		CPU 利用率50以上,每一个percent可以分配10(经验值)个进程,直到50停止分配
		且内存使用率也在50以上,鉴于benstalk使用CPU较高,所以以CPU为主
		另外,在CPU范围内的最大值会和配置文件的最大值做交集,以二者最小值为准
	"""
	#读取conf配置
	cf = ConfigParser.ConfigParser()
	cf.read( CONF_NAME )
	consumerConfig = cf.options("consumer")
	max_consumer = cf.get("consumer","max_consumer")
	min_consumer = cf.get("consumer","min_consumer")
	cpu_idle = cf.get("consumer","cpu_idle")
	mem_idle = cf.get("consumer","mem_idle")
	cpu 	= psutil.cpu_percent(1)
	phymem 	= psutil.phymem_usage()  
	buffers = getattr( psutil, 'phymem_buffers', lambda: 0)()  
	cached	= getattr( psutil , 'cached_phymem', lambda: 0)()  
	used 	= phymem.total - (phymem.free + buffers + cached) 
	
	#算法待完成
	#FIXME
	return max_consumer

if __name__ == '__main__':
	try:
		getConsumerCount()
	except Exception,err:
		print "Exception: " , err
		
