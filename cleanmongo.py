from pymongo import MongoClient

client = MongoClient('mongodb+srv://DBAdmin:7c1K34Xs6Jpqjj1E@mennad.s0wbc.mongodb.net/?retryWrites=true&w=majority&appName=Mennad')
 
db = client['Mennad']
for collection_name in db.list_collection_names():
    db[collection_name].drop()
    print(f"Collection '{collection_name}' supprimée.")

print("Toutes les collections ont été supprimées.")