# comp120_assignment3

COMP120_versioncontrol

Student: Yusuf Al Nader  
Student ID: 301530178  
Section: 402

## Project overview

This is a basic task list program made for COMP120 Assignment 3. It lets a user add tasks, view the tasks, and save them in a text file. I used GitHub issues and a feature branch to organize the work.

## How to run

1. Download or clone this repository.
2. Make sure Python 3 is installed.
3. Open a terminal in the project folder.
4. Run `python task_list.py` (or `python3 task_list.py`).
5. Type **1** to add a task, **2** to see saved tasks, or **3** to exit.

Tasks are saved in `tasks.txt` in the same folder. A blank task is not added.

## Testing

Run `python -m unittest test_task_list.py` from the project folder to check the basic add-task and view-task functions.

## GitHub project work

The first version is tracked through three issues: feature development (#1), documentation (#2), and testing (#3). Development work is done on the `feature/add-task` branch before being merged into `main`.
