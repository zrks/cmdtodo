from sqlalchemy import create_engine, TIMESTAMP
from sqlalchemy.orm import sessionmaker

from sql import Task, Base


engine = create_engine('sqlite:///tasks.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


def add_task(name, description):
    new_task = Task(task_name=name, task_description=description)
    session.add(new_task)
    session.commit()

def list_tasks():
    return session.query(Task).all()

def delete_task(task_name):
    task_to_delete = session.query(Task).filter_by(task_name=task_name)
    task_to_delete.delete()
    session.commit()
