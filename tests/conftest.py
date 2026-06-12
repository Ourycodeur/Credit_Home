import sys
import os
import pytest 
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Fixons le chemin

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from db.models import Base

DATABASE_URL = "postgresql://postgres:root@localhost:5432/deploy_project"

engine = create_engine(DATABASE_URL)

Test = sessionmaker(
    autoflush=False,
    autocommit=False,
    bind=engine,
)

@pytest.fixture()
def db_session():

    Base.metadata.create_all(bind=engine)

    db = Test()

    try:
        yield db
    finally:
        db.close()