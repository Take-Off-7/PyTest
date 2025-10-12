from collections import namedtuple


__version__ = "0.1.0"


Task = namedtuple('Task', ['summary', 'owner', 'done', 'id'])
Task.__new__.__defaults__ = (None, None, False, None)


from .api import (
    add,
    get,
    list_tasks,
    count,
    update,
    delete,
    delete_all,
    unique_id,
    start_tasks_db,
    stop_tasks_db,
)

from .api import Task  # if Task is also defined there


