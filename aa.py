from pymongo import MongoClient

# MongoDB 인스턴스에 연결
client = MongoClient('mongodb://likelion:1234@hanslab.org:27117/')

# 데이터베이스 선택 (없으면 새로 생성됨)
db = client['tutorial_db']

# 컬렉션 선택 (없으면 새로 생성됨)
collection = db['tutorial_collection']


document = {"name": "Park", "age": 25, "city": "Busan"}
collection.insert_one(document)


for doc in collection.find():
    print(doc)

# 특정 조건에 맞는 문서 조회
query = {"city": "Seoul"}
documents = collection.find(query)
for doc in documents:
    print(doc)

# 콜렉션 조회
db.list_collection_names()

