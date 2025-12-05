
import os

def get_current_directory():
    return os.getcwd()

def detect_project_name():
    current_directory = get_current_directory()
    project_name = os.path.basename(current_directory)
    return project_name