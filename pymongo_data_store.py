from pymongo import MongoClient, errors
import random 
import datetime

client = MongoClient('mongodb://localhost:27017/')
db = client['tweets-database']
random_num = random.randint(10,10000)
tweets_col_name = "tweets_collection"+str(random_num)

def store_data(data):
    inserted_id_count = 0
    try:
        collection = db[f"{tweets_col_name}"]
        tweets = collection.insert_many(data, ordered =False)
        
        for id in tweets.inserted_ids:
            inserted_id_count += 1
    except  errors.ConnectionFailure:
        print("Could not connect to server")
    
    except :
        print("Something went wrong")


    return "Success "+str(inserted_id_count)+" number records" if inserted_id_count > 0 else "Failed"