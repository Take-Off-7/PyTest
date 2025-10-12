import sys
import os
import json


pytest_plugins = ["pytester"]


# add the src/ directory (or your actual package directory) to sys.path
sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src"))
)

import pytest
import tasks
from tasks import Task


# @pytest.fixture()
# def tasks_db(tmpdir):
#     tasks.start_tasks_db(str(tmpdir), 'tiny')
#     yield
#     tasks.stop_tasks_db()


# implements tiny database
@pytest.fixture(scope='session')
def tasks_db_session(tmpdir_factory):
    temp_dir = tmpdir_factory.mktemp('temp')
    tasks.start_tasks_db(str(temp_dir), 'tiny')
    yield
    tasks.stop_tasks_db()


## implements both tiny and mongo database
## @pytest.fixture(scope='session', params=['tiny',])
# @pytest.fixture(scope='session', params=['tiny', 'mongo'], ids=['TinyDB', 'MongoDB'])
# def tasks_db_session(tmpdir_factory, request):
#     """Connect to db before tests, disconnect after."""
#     temp_dir = tmpdir_factory.mktemp('temp')
#     tasks.start_tasks_db(str(temp_dir), request.param)
#     yield  # this is where the testing happens
#     tasks.stop_tasks_db()


@pytest.fixture()
def tasks_db(tasks_db_session):
    tasks.delete_all()


@pytest.fixture(scope='session')
def tasks_just_a_few():
    return (
        Task('Write some code', 'Brian', True),
        Task("Code review Brian's code", 'Katie', False),
        Task('Fix what Brian did', 'Michelle', False)
    )


@pytest.fixture(scope='session')
def tasks_multi_per_owner():
    return (
        Task('Make a cookie', 'Raphael'),
        Task('Use an emoji', 'Raphael'),
        Task('Move to Berlin', 'Raphael'),
        Task('Create', 'Michelle'),
        Task('Inspire', 'Michelle'),
        Task('Encourage', 'Michelle'),
        Task('Do a handstand', 'Daniel'),
        Task('Write some books', 'Daniel'),
        Task('Eat ice cream', 'Daniel')
    )


@pytest.fixture()
def db_with_3_tasks(tasks_db, tasks_just_a_few):
    for t in tasks_just_a_few:
        tasks.add(t)


@pytest.fixture()
def db_with_multi_per_owner(tasks_db, tasks_multi_per_owner):
    for t in tasks_multi_per_owner:
        tasks.add(t)


@pytest.fixture(scope='module')
def author_file_json(tmpdir_factory):
    python_author_data = {
        'Ned': {'City': 'Boston'},
        'Brian': {'City': 'Portland'},
        'Luciano': {'City': 'Sau Paulo'}
    }

    file = tmpdir_factory.mktemp('data').join('author_file.json')
    print('file: {}'.format(str(file)))
    with file.open('w') as f:
        json.dump(python_author_data, f)
    return file


def pytest_addoption(parser):
    parser.addoption("--myopt", action="store_true", help="some boolean option")
    parser.addoption("--foo", action="store", default="bar", help="foo: bar or baz")
    parser.addoption("--go", action="store_false", help="true or false")


sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "func")))
import unnecessary_math

@pytest.fixture(autouse=True)
def add_um(doctest_namespace):
    doctest_namespace['um'] = unnecessary_math


import datetime
import random
import time

@pytest.fixture(autouse=True)
def check_duration(request, cache):
    key = 'duration/' + request.node.nodeid.replace(':','_')
    start_time = datetime.datetime.now()
    yield
    stop_time = datetime.datetime.now()
    this_duration = (stop_time - start_time).total_seconds()
    last_duration = cache.get(key, None)
    cache.set(key, this_duration)
    if last_duration is not None:
        # errorstring = "test duration over 2x last duration"
        # assert this_duration <= last_duration * 2, errorstring
        allowed = 0.1 + (last_duration * 2)
        errorstring = f"Test duration {this_duration:.4f}s exceeded limit {allowed:.4f}s"
        assert this_duration <= allowed, errorstring


def pytest_addoption(parser):
    group = parser.getgroup('nice')
    group.addoption("--nice", action="store_true",
    help="nice: turn failures into opportunities")



def pytest_report_header(config):
    if config.getoption('nice'):
        return "Thanks for running the tests.\n"


def pytest_report_teststatus(config, report):
    if report.when == 'call':
            if report.failed and config.getoption('nice'):
                return (report.outcome, 'O', 'OPPORTUNITY for improvement')



