"""Basic checks for the task list program."""
import tempfile
import unittest
from pathlib import Path

from task_list import add_task, read_tasks


class TaskListTests(unittest.TestCase):
    def test_add_and_read_task(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "tasks.txt"
            self.assertTrue(add_task("Finish homework", path))
            self.assertEqual(read_tasks(path), ["Finish homework"])

    def test_blank_task_is_not_saved(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "tasks.txt"
            self.assertFalse(add_task("   ", path))
            self.assertEqual(read_tasks(path), [])

    def test_multiple_tasks(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "tasks.txt"
            add_task("Study", path)
            add_task("Submit assignment", path)
            self.assertEqual(read_tasks(path), ["Study", "Submit assignment"])


if __name__ == "__main__":
    unittest.main()
