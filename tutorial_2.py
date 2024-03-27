from pymongo import MongoClient

client = MongoClient('mongodb://likelion:1234@hanslab.org:27117/')

# 데이터베이스 선택 (없으면 새로 생성됨)
db = client['tutorial_db']

# 컬렉션 선택 (없으면 새로 생성됨)
collection = db['tutorial_collection']

# 특정 조건에 맞는 문서 조회
query = {"city": "Seoul"}
documents = collection.find(query)
for doc in documents:
    print(doc)

# 문서 업데이트
collection.update_one(
    {"name": "John Doe"},  # 조건
    {"$set": {"age": 31}}  # 변경할 내용
)

# 문서 삭제
collection.delete_one({"name": "Park"})

for doc in collection.find():
    print(doc)
