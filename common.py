# coding=utf-8

import os
import sys
import logging
from datetime import datetime

g_SchedulerVersion = "Rel.2018030801"
#global logger

try:
    #Set resultPath DevicID_TimeStamp
    local_path = os.path.abspath(os.path.dirname(sys.argv[0]))
    g_resultPath = os.path.join(local_path, "Result", "{}".format(str(datetime.now().strftime('%Y%m%d%H%M%S'))))
    if not os.path.exists(g_resultPath): os.makedirs(g_resultPath)

    #Set logging debug config
    logging.basicConfig(
        format='%(asctime)s : %(levelname)s : %(funcName)s : %(message)s',
        level=logging.INFO,
        filename= os.path.join(g_resultPath, "Scheduler.txt")
    )
    logger = logging.getLogger('PythonScheduler')

    logger.info("Python Scheduler version is %s " % str(g_SchedulerVersion))
    logger.info("Local python versio is {}".format(sys.version))
    
except:
    raise EOFError("Failed in common : {}".format(str(format_exc())))
        

