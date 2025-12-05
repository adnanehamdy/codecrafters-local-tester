#!/usr/bin/env python3
import os

def main():
    print("=> welcome to the cli")


def detect_project_and_language():
    current_directory = os.getcwd()
    project_name = os.path.basename(current_directory)
    ccProject, language = project_name.rsplit("-", 1)
    if not ccProject:
        raise ValueError("Project name is empty")
    if not language:
        raise ValueError("Language is empty")
    return ccProject, language



if __name__ == "__main__":
    try:
        project, language = detect_project_and_language()
        print(project, language)
    except ValueError as e:
        print(e)
        exit(1)