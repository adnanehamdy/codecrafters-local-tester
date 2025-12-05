#!/usr/bin/env python3
import git

def main():
    print("=> welcome to the cli")
    cloneRepository("https://github.com/practical-tutorials/project-based-learning.git", "/tmp/testing-python-script")



def cloneRepository(repo_url, destination):
    print(f"Cloning repository from {repo_url} to {destination}")
    try:
        git.Repo.clone_from(repo_url, destination)
        print("Repository cloned successfully.")
    except Exception as e:
        print(f"An error occurred while cloning the repository: {e}")


if __name__ == "__main__":
    main()

    
