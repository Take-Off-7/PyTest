import click
from contextlib import contextmanager
import tasks.api as api
import tasks
from tasks import Task

# @contextmanager
# def _tasks_db():
#     """Start and stop the tasks DB around a CLI command."""
#     config = tasks.config.get_config()
#     tasks.start_tasks_db(config.db_path, config.db_type)
#     try:
#         yield
#     finally:
#         tasks.stop_tasks_db()

from tasks import config

@contextmanager
def _tasks_db():
    tasks.start_tasks_db("/tmp/tasks_db.json", "tiny")  # fixed location
    try:
        yield
    finally:
        tasks.stop_tasks_db()


@click.group()
def tasks_cli():
    """Tasks application CLI."""


@tasks_cli.command(help="Add a task")
@click.argument('summary')
@click.option('--owner', default=None, help="Task owner")
def add(summary, owner):
    with _tasks_db():
        task = Task(summary, owner)
        task_id = api.add(task)
        click.echo(task_id)


@tasks_cli.command(help="List tasks")
@click.option('-o', '--owner', default=None, help="Task owner")
def list(owner):
    """List tasks in a formatted table. If owner given, filter by owner."""
    formatstr = "  {:<5}{:<7}{:<6} {}"
    with _tasks_db():
        click.echo(formatstr.format('ID', 'owner', 'done', 'summary'))
        click.echo(formatstr.format('--', '-----', '----', '-------'))

        for t in api.list_tasks(owner):
            done = 'True' if t.done else 'False'
            owner_display = '' if t.owner is None else t.owner
            click.echo(formatstr.format(t.id, owner_display, done, t.summary))


@tasks_cli.command(help="Get a task by id")
@click.argument('task_id', type=int)
def get(task_id):
    with _tasks_db():
        click.echo(api.get(task_id))


@tasks_cli.command(help="Delete a task by id")
@click.argument('task_id', type=int)
def delete(task_id):
    with _tasks_db():
        api.delete(task_id)
        click.echo(f"Deleted task {task_id}")


@tasks_cli.command(help="Delete all tasks")
def delete_all():
    with _tasks_db():
        api.delete_all()
        click.echo("All tasks deleted.")


@tasks_cli.command(help="Update a task")
@click.argument('task_id', type=int)
@click.argument('summary')
@click.option('--owner', default=None)
@click.option('--done', is_flag=True)
def update(task_id, summary, owner, done):
        with _tasks_db():
            task = Task(summary, owner, done)
            api.update(task_id, task)
            click.echo(f"Updated task {task_id}")


if __name__ == "__main__":
    tasks_cli()
