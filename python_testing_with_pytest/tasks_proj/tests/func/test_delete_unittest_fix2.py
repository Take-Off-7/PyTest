import pytest
import unittest
import tasks
from tasks import Task

@pytest.fixture
def tasks_db_non_empty(tasks_db_session, request):
    tasks.delete_all()
    ids = []
    ids.append(tasks.add(Task('One', 'Brian', True)))
    ids.append(tasks.add(Task('Two', 'Still Brian', False)))
    ids.append(tasks.add(Task('Three', 'Not Brian', False)))
    request.cls.ids = ids


@pytest.mark.usefixtures('tasks_db_non_empty')
class TestNonEmpty(unittest.TestCase):

    def test_delete_decrease_count(self):
        self.assertEqual(tasks.count(), 3)
        tasks.delete(self.ids[0])
        self.assertEqual(tasks.count(), 2)
