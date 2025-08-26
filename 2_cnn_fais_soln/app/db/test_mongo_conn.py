# import sys
# import os

# # Add parent folder to Python path
# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# # above lines are to tackle the error of - no module named app

from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv('MONGO_URI')


try:
    client = MongoClient(MONGO_URI)
    db = client.get_database('visual_product_db')
    
    # Test connection
    client.admin.command('ping')
    print("MongoDB Atlas connection successful!")
    
    # Check collections exist
    collections = db.list_collection_names()
    print(f"Collections found: {collections}")
    
    # Count documents in each collection
    for collection_name in collections:
        count = db[collection_name].count_documents({})
        print(f"{collection_name}: {count} documents")
        
except Exception as e:
    print(f"Connection failed: {e}")
