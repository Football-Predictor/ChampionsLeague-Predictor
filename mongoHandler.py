from pymongo import MongoClient
import pandas as pd
from pandas import json_normalize

# This will be removed for final version, this is our connection string to mongoDB
CONNECTIONSTRING = r"mongodb+srv://anduarielsivansteven:aass123!@ballondor.csw3klm.mongodb.net/?retryWrites=true&w=majority"

class mongoHandler:
    """A class to handle all mongoDB interactions"""
    def __init__(self, connectionString=CONNECTIONSTRING, collectionName="BallondOrPredictor",dbName="ChampionsLeaguePredictor"):
        self.client = MongoClient(connectionString)
        self.db = self.client[dbName]
        self.collection = self.db[collectionName]

    def addCSVToMongoDB(self, csvPath):
        """Adds csv data to a mongoDB database"""
        df = pd.read_csv(csvPath)
        data = df.to_dict(orient='records')
        self.collection.insert_many(data)

    def clearMongoDB(self):
        """Clears a mongoDB database"""
        self.collection.delete_many({})
    
    def pullMongoDB(self, filepath):
        """Pulls all data from a mongoDB database"""
        data = self.collection.find({})
        df = json_normalize(list(data))
        df.drop(columns=['_id'], inplace=True)
        df.to_csv(filepath, index=False, encoding="utf-8")