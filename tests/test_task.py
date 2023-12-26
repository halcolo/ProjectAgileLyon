import unittest
from package.task import Task

class TestTask(unittest.TestCase):
    def test_task_creation(self):
        task = Task("Task 1", "Description 1")
        self.assertEqual(task.task_id, "Task 1")
        # self.assertEqual(task.description, "Description 1")

    def test_create_task(self):
        task = Task("Task 2", "Cretation and delete of task")
        task.create_task(player_check=False) # player_check=False because we don't have a session player for tests
        task_dict = task.to_dict()
        assert task_dict["id"] is not None
        # Delete task from database
        task.delete_task()

    # def test_add_player(self):
    #     task = Task("Task 4", "Description 4")
    #     task.add_player("John Doe", "john@example.com")
    #     self.assertEqual(len(task.players), 1)
    #     # Add more assertions to verify the player is added correctly

    # def test_create_planning(self):
    #     task = Task("Task 5", "Description 5")
    #     task.create_planning("Planning 1", 10, ["Task 1", "Task 2"], "Game Mode 1")
    #     self.assertEqual(task.planning_name, "Planning 1")
    #     self.assertEqual(task.card_quantity, 10)
    #     self.assertEqual(task.tasks, ["Task 1", "Task 2"])
    #     self.assertEqual(task.game_mode, "Game Mode 1")
    #     # Add more assertions to verify the planning is created correctly

    # def test_to_dict(self):
    #     task = Task("Task 6", "Description 6")
    #     task_dict = task.to_dict()
    #     self.assertEqual(task_dict['id'], task.id)
    #     self.assertEqual(task_dict['name'], task.name)
    #     self.assertEqual(task_dict['stimations'], task.stimations)
    #     self.assertEqual(task_dict['squad'], task.squad)
    #     self.assertEqual(task_dict['final_score'], task.final_score)
    #     self.assertEqual(task_dict['manager'], task.manager)
    #     self.assertEqual(task_dict['creation_date'], task.creation_date)
    #     self.assertEqual(task_dict['status'], task.status)
    #     self.assertEqual(task_dict['task_mode'], task.task_mode)
    #     # Add more assertions to verify the dictionary representation is correct

    # def test_check_data_exist(self):
    #     task = Task("Task 7", "Description 7")
    #     self.assertFalse(task.check_data_exist())
    #     task.task_id = "Task 7"
    #     self.assertTrue(task.check_data_exist())

    # def test_get_task_from_db(self):
    #     task = Task("Task 8", "Description 8")
    #     task.get_task_from_db("task_id_123")
    #     # Add assertions to verify that the task data is retrieved correctly from the database

    # def test_from_dict(self):
    #     task_dict = {
    #         'id': "Task 9",
    #         'name': "Task 9",
    #         'description': "Description 9"
    #     }
    #     task = Task.from_dict(task_dict)
    #     self.assertEqual(task.task_id, "Task 9")
    #     self.assertEqual(task.description, "Description 9")