from project.worker import app


@app.task
def example_task(pk: int):
    pass
