import pytest
import tasks
from tasks import Task

@pytest.fixture
def setup_tasks(tasks_db_session):
    tasks.delete_all()
    ids = []
    ids.append(tasks.add(Task('One', 'Brian', True)))
    ids.append(tasks.add(Task('Two', 'Still Brian', False)))
    ids.append(tasks.add(Task('Three', 'Not Brian', False)))
    return ids

def test_delete_decrease_count(setup_tasks):
    ids = setup_tasks
    assert tasks.count() == 3
    tasks.delete(ids[0])
    assert tasks.count() == 2
