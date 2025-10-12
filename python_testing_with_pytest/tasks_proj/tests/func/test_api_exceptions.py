import pytest
import tasks
from tasks import Task


class TestUpdate():

    def test_bad_id(self):
        with pytest.raises(TypeError):
            tasks.update(task_id={'dict instead': 1},
            task=tasks.Task())

    def test_bad_task(self):
        with pytest.raises(TypeError):
            tasks.update(task_id=1, task='not a task')


@pytest.mark.usefixtures('tasks_db')
class TestAdd():
    def test_missing_summary(self):
        with pytest.raises(ValueError):
            tasks.add(Task(owner='bob'))

    def test_done_not_bool(self):
        with pytest.raises(ValueError):
            tasks.add(Task(summary='summary', done='True'))

    def test_add_and_get(self):
        with pytest.raises(ValueError):
            task_id = tasks.add(Task(summary='eat'))
            tasks.get(task_id)


def test_add_raises():
    with pytest.raises(TypeError):
        tasks.add(task='not a Task object')

def test_start_tasks_db_raises():
    with pytest.raises(ValueError) as excinfo:
        tasks.start_tasks_db('some/great/path', 'mysql')
        exception_msg = excinfo.value.args[0]
        assert exception_msg == "db_type must be a 'tiny' or 'mongo'"

@pytest.mark.smoke
def test_list_raises():
    with pytest.raises(TypeError):
        tasks.list_tasks(owner=123)

@pytest.mark.get
@pytest.mark.smoke
def test_get_raises():
    with pytest.raises(TypeError):
        tasks.get(task_id='123')
