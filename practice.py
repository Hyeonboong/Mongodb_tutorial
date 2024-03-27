from pymongo import MongoClient
client = MongoClient('mongodb://likelion:1234@hanslab.org:27117/')
db = client['mydatabase_phs']
users = db['users']

users.create_index([('email', 1)], unique=True)


try :
    users.insert_many([
        {"name":"John Doe", "email" : "john@example.com"},
        {"name":"Jane Doe", "email" : "Jane@example.com"},
        {"name": "Alice", "email": "alice@example.com"}
        ])
    

except Exception as e:
    print("An error occurred:", e)


try:
    result = users.update_many(
        {"name": {"$regex": "^J"}},  # 이름이 J로 시작하는 모든 문서
        {"$set": {"status": "verified"}}
    )
    print(f"{result.matched_count} documents matched, {result.modified_count} documents updated.")
except Exception as e:
    print("An error occurred:", e)


for document in users.find():
        print(document)