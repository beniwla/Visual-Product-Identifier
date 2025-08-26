from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv('MONGO_URI')

try:
    client = MongoClient(MONGO_URI)
    # Test the connection
    client.admin.command('ping')
    print("✅ MongoDB Atlas connection successful!")
    
    db = client["visual_product_db"]

    products_col = db["products"]
    embedding_cnn_faiss_metadata_col = db["embedding_cnn_faiss_metadata"]
    embedding_clip_faiss_metadata_col = db["embedding_clip_faiss_metadata"]

except Exception as e:
    print(f"Connection failed: {e}")


