from pymongo import MongoClient

# 회원
# - 회원 가입(Create)
# - 회원 목록(Read)
# - 회원 수정(Update)
# - 회원 삭제(Delete)

# 상품
# - 상품 등록(Create)
# - 상품 목록(Read)
# - 상품 수정(Update)
# - 상품 삭제(Delete)

# 게시판
# - 게시글 등록(Create)
# - 게시글 목록(Read)
# - 게시글 수정(Update)
# - 게시글 삭제(Delete)

# --> CRUD 작업  DAO(Data Access Object) 만듦
# 게시글 -> BoardDAO.py
# 회원 -> MemberDAO.py


# 진짜 코드!
# 1. Connection 작업(공통:Common)

def db_conn() :
     client = MongoClient("127.0.0.1", 27017)  # MongoDB 찾아감
     db = client['movie']                      # Database 선택
     collection = db.get_collection(('review'))  # Collection 선택
     return collection

# 2. Review 저장(Creat)
def create_review(data) :
     collection = db_conn()  # MongoDB Connection
     collection.insert_one(data)  # 1건의 데이터 저장

# 3.Review 조회(Read)
def Read_review() :  # MongoDB Connection
     pass
