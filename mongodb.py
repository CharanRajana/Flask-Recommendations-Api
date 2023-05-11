from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()


def get_database():
   CONNECTION_STRING = os.getenv("MONGO_CONNECTION_URL")
   client = MongoClient(CONNECTION_STRING)
   return client['Movie_recommendation']
if __name__ == "__main__":   
  
  
   dbname = get_database()