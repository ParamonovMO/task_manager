import pytest
from task_manager import Task


@pytest.fixture
def task():
    task = Task('Прибраться', 'Убрать мусор из комнаты')
    return task

def pytest_make_parametrize_id(val): 
    return repr(val)