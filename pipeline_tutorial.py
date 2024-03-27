from pymongo import MongoClient

client = MongoClient('mongodb://likelion:1234@hanslab.org:27117/')
db = client['tutorial_db_phs']
collection = db['users1']

# 기존 데이터가 있다면 삭제 (새로운 실습을 위해)
collection.delete_many({})

# 샘플 데이터 삽입
sample_users = [
    {"name": "Alice", "age": 25, "status": "active"},
    {"name": "Bob", "age": 30, "status": "inactive"},
    {"name": "Charlie", "age": 35, "status": "active"},
    {"name": "David", "age": 40, "status": "active"},
    {"name": "Eve", "age": 25, "status": "active"},
    {"name": "Frank", "age": 30, "status": "active"}
]

collection.insert_many(sample_users)

pipeline = [
    {"$match": {"status": "active"}},
    {"$group": {"_id": "$age", "count": {"$sum": 1}}}
]

results = collection.aggregate(pipeline)

for result in results:
    print(result)