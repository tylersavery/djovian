import os

from celery import Celery

from project import __name__

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
app = Celery(__name__)
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):

    sender.add_periodic_task(10 * 60, example_task.s(), name="example_task")


@app.task
def example_task():
    from django.core import management

    management.call_command("example_command")
