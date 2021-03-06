import datetime

from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine


Base = declarative_base()


class Task(Base):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True)
    task_name = Column(String(50), nullable=False)
    task_description = Column(String(250), nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow())


engine = create_engine('sqlite:///tasks.db')

Base.metadata.create_all(engine)
