from pymongo import MongoClient

class DBConnector:
    def __init__(self, uri="mongodb://localhost:27017", database="voicegenie"):
        self.client = MongoClient(uri)
        self.db = self.client[database]

    def get_collection(self, collection_name):
        return self.db[collection_name]

    def fetch_data(self, collection_name, query):
        collection = self.get_collection(collection_name)
        return list(collection.find(query))

    def insert_dummy_data(self):
       
        self.get_collection("users").delete_many({})
        self.get_collection("CallSessionHistories").delete_many({})
        self.get_collection("subscriptions").delete_many({})

    
        self.get_collection("users").insert_many([
            {"_id": 1, "signup_date": "2025-01-27", "is_signed_up": True},
            {"_id": 2, "signup_date": "2025-01-26", "is_signed_up": False},
            {"_id": 3, "signup_date": "2025-01-27", "is_signed_up": True},
            {"_id": 4, "signup_date": "2025-01-27", "is_signed_up": True}
        ])

        self.get_collection("CallSessionHistories").insert_many([
            {"_id": 1, "campaignId": "demo", "duration": 35, "error": None, "status": "connected"},
            {"_id": 2, "campaignId": "demo", "duration": 20, "error": None, "status": "connected"},
            {"_id": 3, "campaignId": "other", "duration": 50, "error": "network", "status": "failed"},
            {"_id": 4, "campaignId": "demo", "duration": 60, "error": None, "status": "connected"}
        ])

        self.get_collection("subscriptions").insert_many([
            {"_id": 1, "type": "Trial Monthly", "status": "active", "start_date": "2025-01-01", "end_date": "2025-01-31"},
            {"_id": 2, "type": "Starter Yearly", "status": "active", "start_date": "2024-01-01", "end_date": "2025-01-01"},
            {"_id": 3, "type": "Growth Monthly", "status": "canceled", "start_date": "2025-01-01", "end_date": "2025-01-31"},
            {"_id": 4, "type": "Elite Yearly", "status": "active", "start_date": "2024-02-01", "end_date": "2025-02-01"}
        ])