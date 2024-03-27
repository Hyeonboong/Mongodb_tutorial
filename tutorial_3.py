from pymongo import MongoClient

client = MongoClient('mongodb://likelion:1234@hanslab.org:27117/')

# 데이터베이스 선택 (없으면 새로 생성됨)
db = client['tutorial_db_phs']

# 컬렉션 선택 (없으면 새로 생성됨)
collection = db['tutorial_collection']

# 데이터베이스 조회
print(client.list_database_names())
# 테이블 조회
print(db.list_collection_names())