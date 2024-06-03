from sqlalchemy import Column, Integer, String, BINARY, TEXT, DATETIME, PrimaryKeyConstraint
from sqlalchemy.sql import func
from .util.database import Base

class CodeSubmission(Base):
    __tablename__ = "code_submissions"
    
    # user_ip = Column(BINARY(4), nullable=False) not using user ip to avoid privacy issues
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    code = Column(TEXT, nullable=False)
    output = Column(TEXT, nullable=True)
    timestamp = Column(DATETIME, nullable=False, default=func.now())

    # __table_args__ = (
    #     PrimaryKeyConstraint('userIP', 'timestamp'),
    # )