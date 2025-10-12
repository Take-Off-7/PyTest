import unittest
import shutil
import tempfile
import tasks
from tasks import Task


def setUpModule():
    global temp_dir
    temp_dir = tempfile.mkdtemp()
    tasks.start_tasks_db(str(temp_dir), 'tiny')


def tearDownModule():
    tasks.stop_tasks_db()
    shutil.rmtree(temp_dir)


class TestNonEmpty(unittest.TestCase):

    def setUp(self):
        tasks.delete_all()
        self.ids = []
        self.ids.append(tasks.add(Task('One', 'Brian', True)))
        self.ids.append(tasks.add(Task('Two', 'Still Brian', False)))
        self.ids.append(tasks.add(Task('Three', 'Not Brian', False)))


    def test_delete_decrease_count(self):
        self.assertEqual(tasks.count(), 3)
        tasks.delete(self.ids[0])
        self.assertEqual(tasks.count(), 2)
