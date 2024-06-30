from pymongo import MongoClient

class AnimalShelter:
    def __init__(self, username, password, host='localhost', port=27017, db='AAC', collection='animals'):
        self.client = MongoClient(f'mongodb://{username}:{password}@{host}:{port}')
        self.database = self.client[db]
        self.collection = self.database[collection]
        print("Connection Successful")

    def create(self, data):
        if data:
            result = self.collection.insert_one(data)
            return True if result.inserted_id else False
        else:
            raise ValueError("Empty data cannot be inserted")

    def read(self, query):
        cursor = self.collection.find(query)
        return list(cursor) if cursor else []

    def update(self, query, new_values):
        result = self.collection.update_many(query, {'$set': new_values})
        return result.modified_count

    def delete(self, query):
        result = self.collection.delete_many(query)
        return result.deleted_count









