# python
# 파일: `infrastructure/database.py`
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session, declarative_base
from contextlib import contextmanager

# 예시 기본값(개발용). 실제 값은 환경변수 `DATABASE_URL`로 설정하세요.
# MySQL 예: mysql\+pymysql://user:password@host:3306/dbname?charset=utf8mb4
DATABASE_URL = os.getenv("DATABASE_URL", "mysql+pymysql://user:password@localhost:3306/app_db?charset=utf8mb4")

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {},
    pool_pre_ping=True,
)

# 기본 세션 팩토리
SessionFactory = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 요청/스레드별 안전하게 쓰려면 scoped_session 사용
SessionLocal = scoped_session(SessionFactory)

Base = declarative_base()

@contextmanager
def get_db():
    """
    사용 후 반드시 세션을 remove() 해서 연결 풀에 반환
    """
    db = SessionLocal()
    try:
        yield db
        db.commit()
    except:
        db.rollback()
        raise
    finally:
        SessionLocal.remove()
