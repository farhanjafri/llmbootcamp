import numpy as np
import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
import db_ops
import time

import json
import sys
import traceback
import logging


class ConfigQueryProcessor():
    """

        Config Query processor module reads the configration values from DB
    """
    def __init__(self):
        try:
            # Get the logger
            self.logger = logger.getLogger(logger_name=__name__,file_name='./query_processor.log')
            self.logger.setLevel(logging.DEBUG)

            # Load the configuration
            f = open('./config.json')
            self.config = json.load(f)
            f.close()

            # Create a database connection
            db_user = self.config["db_user"]
            db_password = self.config["db_password"]
            db_name = self.config["db_name"]
            db_host = self.config["db_host"]
            db_connection_str = 'postgresql://%s:%s@%s/%s' % (db_user,db_password,db_host,db_name)
            self.db_engine = db.create_engine(db_connection_str)
            #engine = db.create_engine('postgresql://user:password@hostname/database_name')

        except:
            print("************* Unable to load configuration, exiting ***********:")
            print(traceback.format_exc())
            sys.exit()
        
    def get_configuration_data(self,query):
        results = []
       # select  configuration.key, configuration.value  from configuration;
        query = self.config["db_config_query"]
        self.logger.debug(query)
        fetchQuery = self.db_engine.execute(query)
          
        for t in fetchQuery.fetchall():
            self.logger.debug(str(t))
            res = {}
            res['key'] = t[0]
            res['val'] = t[1]
            results.append(res)

        return results
          
processor = ConfigQueryProcessor()
processor.process()
          
          