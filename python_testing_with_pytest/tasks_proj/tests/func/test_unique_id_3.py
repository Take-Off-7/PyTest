import pytest
import tasks
from tasks import Task


@pytest.mark.skipif(tasks.__version__<'0.2.0', 
reason='not supported until version 0.2.0')
def test_unique_id_1():
    id_1 = tasks.unique_id()
    id_2 = tasks.unique_id()
    assert id_1 == id_2




