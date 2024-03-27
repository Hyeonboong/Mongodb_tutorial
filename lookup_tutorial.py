from pymongo import MongoClient

client = MongoClient('mongodb://likelion:1234@hanslab.org:27117/')
db = client['tutorial_db_phs']

# users 컬렉션 생성 및 샘플 데이터 삽입
users_collection = db['users3']
users_collection.delete_many({})  # 기존 데이터 초기화
users_sample = [
    {"_id": 1, "name": "Alice", "userId": "user1"},
    {"_id": 2, "name": "Bob", "userId": "user2"},
    {"_id": 3, "name": "Charlie", "userId": "user3"}
]
users_collection.insert_many(users_sample)

# orders 컬렉션 생성 및 샘플 데이터 삽입
orders_collection = db['orders']
orders_collection.delete_many({})  # 기존 데이터 초기화
orders_sample = [
    {"order_id": 1, "product": "Book", "user_id": "user1"},
    {"order_id": 2, "product": "Laptop", "user_id": "user1"},
    {"order_id": 3, "product": "Pen", "user_id": "user2"}
]
orders_collection.insert_many(orders_sample)
pipeline = [
    {"$lookup": {
        "from": "orders",  # 조인할 컬렉션 이름
        "localField": "userId",  # 현재 문서의 필드
        "foreignField": "user_id",  # 조인할 컬렉션의 필드
        "as": "order_info"  # 추가할 필드 이름
    }},

    {"$match": {"order_info": {"$ne": []}}},  # 주문 정보가 있는 사용자만 선택
]

results = users_collection.aggregate(pipeline)

for result in results:
    print(result)
