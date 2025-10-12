import tasks


def test_delete_decreases_count(db_with_3_tasks):
    ids = [t.id for t in tasks.list_tasks()]
    assert tasks.count() == 3
    tasks.delete(ids[0])
    assert tasks.count() == 2







