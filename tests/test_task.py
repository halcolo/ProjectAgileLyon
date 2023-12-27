import unittest
from package.task import Task
from api_routes import app


class TestTask(unittest.TestCase):
    def test_task_creation(self):
        task = Task("Task 1", "Description 1")
        self.assertEqual(task.task_id, "Task 1")

    def test_create_task(self):
        
        with app.app_context():
            task = Task("Task 2", "Cretation and delete of task")
            # player_check=False because we don't have a session player for tests
            task.create_task(session_check=False) 
            self.assertIsNotNone(task.get_id())
            # Delete task from database
            task.delete_task()

    def test_task_to_dict(self):
        with app.app_context():
            task = Task("Task 3", "Checking task dictionary")
            task.create_task(session_check=False)
            task_dict = task.to_dict()
            self.assertEqual(task_dict['id'], task.id)
            self.assertEqual(task_dict['task_id'], task.task_id)
            self.assertEqual(task_dict['stimations'], task.stimations)
            self.assertEqual(task_dict['final_score'], task.final_score)
            self.assertEqual(task_dict['manager'], task.manager)
            self.assertEqual(task_dict['creation_date'], task.creation_date)
            task.delete_task()

    def test_check_data_exist(self):
        with app.app_context():
            task = Task("Task 4", "Description 6")
            task.create_task(session_check=False)
            # self.assertFalse(task.check_data_exist())
            self.assertTrue(task.check_data_exist())
            task.delete_task()

    def test_get_task_from_db(self):
        with app.app_context():
            task = Task("Task 5", "Description 5")
            task.create_task(session_check=False)
            task_id = task.id
            task.get_task_from_db(task_id, session_check=False)
            self.assertEqual(task.get_id(), task_id)
            task.delete_task()

    def test_from_dict(self):
        task_dict = {
            'task_id': "Task 6",
            'mode': "0",
        }
        task = Task.from_dict(task_dict)
        self.assertEqual(task.task_id, "Task 6")
        self.assertEqual(task.mode, "0")