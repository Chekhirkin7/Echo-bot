from bson import ObjectId
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

import os
from dotenv import load_dotenv

load_dotenv()

URI = os.getenv("MG_URI")

client = MongoClient(URI, server_api=ServerApi("1"))
db = client["Echo-Bot"]
