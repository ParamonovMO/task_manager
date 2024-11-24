from task_manager import Task
import pytest


class TestTask:

    def test_title(self, task):
        assert task.title == 'Прибраться'
        assert task.description == 'Убрать мусор из комнаты'

    def test_not_complete(self, task):
        assert task.status == False

    def test_complete(self, task):
        task.complete()
        assert task.status == True

    def test_title_change(self, task):
        task.title = 'Убраться'
        assert task.title == 'Убраться'
        assert task.description == 'Убрать мусор из комнаты'
