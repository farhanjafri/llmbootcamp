
from typing import Union
from fastapi import FastAPI
from fastapi import HTTPException
from pydantic import BaseModel
#from queryresponse import QueryResponse
#from queryresponse import SearchQuery
import json
import uuid
import sys
import traceback
import logger
import db_ops
from fastapi.middleware.cors import CORSMiddleware


# Initialize semantic search
# Create logger
logger = logger.getLogger(__name__,'./main.log')
try:
    # Load the configuration
    f = open('./config.json')
    config = json.load(f)
    f.close()
    
    db_name =config["db_name"]
    db_user= config["db_user"]
    db_password = config["db_password"]
    db_host = config["db_host"]

    # Create a redis client
 #   redis_conn = redis.Redis(host=config["redis_host"], port=6379, db=0,decode_responses=True)

    
    # Create app
    app = FastAPI()

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  #Allows all origins
        allow_credentials=True,
        allow_methods=["*"],  # Allows all methods
        allow_headers=["*"],  # Allows all headers
    )

    logger.debug('Application server initialized successfully.')
  

except:
    logger.error("************* Unable to iniatize service. ***********:" )
    logger.error(traceback.format_exc())
    sys.exit()


#----------------------- Define Endpoints here --------------------

# Define the home endpoint
@app.get("/")
def home():
    return "Config Service. Please use the /config and /status endpoints for submitting and getting results"

@app.get("/config")
def config():
    try:
        return db_ops.get_configuration()
    except:
        logger.error(traceback.format_exc())
        raise HTTPException(status_code=500, detail="Unexpected error..")
    CORSMiddle