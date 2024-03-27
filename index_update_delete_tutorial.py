from pymongo import MongoClient

client = MongoClient('mongodb://likelion:1234@hanslab.org:27117/')
db = client['mydatabase']
users = db['users']

# 'email' 필드에 대한 인덱스 생성
users.create_index([('email', 1)], unique=True)


# update
try:
    result = users.update_many(
        {"name": {"$regex": "^J"}},  # 이름이 J로 시작하는 모든 문서
        {"$set": {"status": "verified"}}  # statuse 필드가 없으면, 생성하고 값을 넣는다.
    )
    print(f"{result.matched_count} documents matched, {result.modified_count} documents updated.")
except Exception as e:
    print("An error occurred:", e)



"""

# delete_many : 특정 조건에 해당하는 여러 문서를 한 번에 삭제하기 위함
try:
    result = users.delete_many({"status": "verified"})
    print(f"{result.deleted_count} documents deleted.")
except Exception as e:
    print("An error occurred:", e)

"""

"""
# 예외처리

from pymongo.errors import DuplicateKeyError

try:
    users.insert_one({"email": "john@example.com"})  # 이미 존재하는 이메일
except DuplicateKeyError as e:
    print("Duplicate key error:", e)
except Exception as e:
    print("An error occurred:", e)
"""

