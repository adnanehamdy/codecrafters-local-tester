#!/usr/bin/env python3
from utls import *

INVALID_PROJECT_DIR_ERROR = (
    "Directory name must contain a '-' separating project and language, "
    "e.g. 'codecrafters-sqlite-python'"
)

def detect_project_and_language():
    project_name = detect_project_name().strip()

    if "-" not in project_name:
        raise ValueError(INVALID_PROJECT_DIR_ERROR)

    cc_project, language = project_name.rsplit("-", 1)
    cc_project = cc_project.strip()
    language = language.strip()

    if not cc_project:
        raise ValueError("Project name is empty. " + INVALID_PROJECT_DIR_ERROR)
    if not language:
        raise ValueError("Language is empty. " + INVALID_PROJECT_DIR_ERROR)

    return cc_project, language


def main():
    print("=> welcome to the cli")
    try:
        cc_project, language = detect_project_and_language()
        print(cc_project, language)
    except ValueError as e:
        print(e)
        exit(1)


if __name__ == "__main__":
    main()
