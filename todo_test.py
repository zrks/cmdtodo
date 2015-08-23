from sqlalchemy import create_engine

import unittest
from sqlalchemy.orm import sessionmaker

from sql import Task, Base
#from db_handler import add_task, list_tasks, delete_task


class Todo_test(unittest.TestCase):

    engine = create_engine('sqlite:///:memory:')
    Session = sessionmaker(bind=engine)
    session = Session()

    def setUp(self):
        Base.metadata.create_all(self.engine)
        task_name = 'Test_case'
        task_description = 'Test desc.'
        task_to_add = Task(task_name=task_name, task_description=task_description)
        self.session.add(task_to_add)
        self.session.commit()

    def test_task_name(self):
        expected = 'Test_case'
        result = self.session.query(Task).filter_by(task_name=expected).first()
        self.assertEqual(result.task_name, expected)

    def test_task_description(self):
        expected = 'Test desc.'
        result = self.session.query(Task).filter_by(task_description=expected).first()
        self.assertEqual(result.task_description, expected)

    def tearDown(self):
        Base.metadata.drop_all(self.engine)


if __name__ == '__main__':
    unittest.main()
