# """tasks/api.py -- API for managing tasks."""

# from tasks import Task

# # Simple in-memory "database"
# _tasks_db = {}
# _next_id = 1


# def add(task):
#     global _next_id
#     if not isinstance(task, Task):
#         raise TypeError("task must be a Task instance")

#     # --- NEW VALIDATIONS ---
#     if task.summary is None or task.summary == "":
#         raise ValueError("task.summary must not be empty")

#     if not isinstance(task.done, bool):
#         raise ValueError("task.done must be a boolean")
#     # ------------------------

#     task_id = _next_id
#     _next_id += 1
#     task = task._replace(id=task_id)
#     _tasks_db[task_id] = task
#     return task_id


# def get(task_id):  # type: (int) -> Task
#     """Return a task by id."""
#     if not isinstance(task_id, int):
#         raise TypeError("task_id must be int")
#     return _tasks_db.get(task_id)


# def list_tasks(owner=None):  # type: (str|None) -> list[Task]
#     """Return list of all tasks, optionally filtered by owner."""
#     if owner is not None and not isinstance(owner, str):
#         raise TypeError("owner must be a string or None")

#     if owner is None:
#         return list(_tasks_db.values())
#     else:
#         return [t for t in _tasks_db.values() if t.owner == owner]


# def count():  # type: () -> int
#     """Return the number of tasks."""
#     return len(_tasks_db)


# def update(task_id, task):  # type: (int, Task) -> None
#     """Update task in db."""
#     if not isinstance(task, Task):
#         raise TypeError("task must be a Task instance")
#     if task_id not in _tasks_db:
#         raise ValueError(f"no task with id {task_id}")
#     _tasks_db[task_id] = task._replace(id=task_id)


# def delete(task_id):  # type: (int) -> None
#     """Delete a task by id."""
#     if task_id in _tasks_db:
#         del _tasks_db[task_id]


# def delete_all():  # type: () -> None
#     """Remove all tasks."""
#     _tasks_db.clear()


# def unique_id():  # type: () -> int
#     """Return an unused id."""
#     global _next_id
#     uid = _next_id
#     _next_id += 1
#     return uid


# def start_tasks_db(db_path, db_type):  # type: (str, str) -> None
#     """Start the tasks database."""
#     if db_type not in ("tiny", "mongo"):
#         raise ValueError("db_type must be a 'tiny' or 'mongo'")
#     # For now, our "db" is always just the in-memory dict
#     delete_all()  # reset DB


# def stop_tasks_db():  # type: () -> None
#     """Stop the tasks database."""
#     delete_all()




################### Version writes to /tmp/tasks_db.json ###################

"""
tasks/api.py -- JSON-backed implementation for managing tasks.
"""

import json
from pathlib import Path
from tasks import Task

# File where tasks are stored
_db_file = Path("/tmp/tasks_db.json")

# In-memory cache
_tasks_db = {}
_next_id = 1

def _load_db():
    """Load the database from disk into memory."""
    global _tasks_db, _next_id
    if _db_file.exists():
        try:
            data = json.loads(_db_file.read_text())
            _tasks_db = {int(k): Task(**v) for k, v in data["tasks"].items()}
            _next_id = data["next_id"]
        except Exception:
            _tasks_db = {}
            _next_id = 1
    else:
        _tasks_db = {}
        _next_id = 1

def _save_db():
    """Persist memory database to disk."""
    data = {
        "tasks": {k: t._asdict() for k, t in _tasks_db.items()},
        "next_id": _next_id,
    }
    _db_file.write_text(json.dumps(data, indent=2))

# ---- CRUD OPERATIONS ----

def add(task):
    """Add a new task and return its ID."""
    global _next_id
    task_id = _next_id
    _next_id += 1
    _tasks_db[task_id] = task._replace(id=task_id)
    _save_db()
    return task_id

def get(task_id):
    """Return a task by ID."""
    return _tasks_db.get(task_id)

def list_tasks(owner=None):
    """Return list of tasks, optionally filtered by owner."""
    if owner is None:
        return list(_tasks_db.values())
    return [t for t in _tasks_db.values() if t.owner == owner]

def count():
    """Return number of tasks."""
    return len(_tasks_db)

def update(task_id, task):
    """Update a task."""
    if task_id not in _tasks_db:
        raise ValueError(f"No task with ID {task_id}")
    _tasks_db[task_id] = task._replace(id=task_id)
    _save_db()

def delete(task_id):
    """Delete a task by ID."""
    if task_id in _tasks_db:
        del _tasks_db[task_id]
        _save_db()

def delete_all():
    """Remove all tasks."""
    global _tasks_db, _next_id
    _tasks_db = {}
    _next_id = 1
    _save_db()

# ---- UTILITY / LEGACY COMPATIBILITY ----

def unique_id():
    """Return a new unique ID (without creating a task)."""
    global _next_id
    uid = _next_id
    _next_id += 1
    _save_db()
    return uid

# ---- DB INITIALIZATION ----

def start_tasks_db(db_path=None, db_type=None):
    """Load database from disk (db_path ignored for JSON implementation)."""
    _load_db()

def stop_tasks_db():
    """Ensure database is saved."""
    _save_db()
