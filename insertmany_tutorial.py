from pymongo import MongoClient

client = MongoClient('mongodb://likelion:1234@hanslab.org:27117/')

db = client['tutorial_db_phs']

users = db['users'] # users라는 이름의 collection을 생성한다 cf. sql의 table

# 'email' 필드에 대한 인덱스 생성
users.create_index([('email', 1)], unique=True)

try:
    users.insert_many([
        {"name": "John Doe", "email": "john@example.com"},
        {"name": "Jane Doe", "email": "jane@example.com"}
    ])
    print("Documents inserted successfully.")
except Exception as e:
    print("An error occurred:", e)


# 모든 문서 조회
for doc in users.find():
    print(doc)

