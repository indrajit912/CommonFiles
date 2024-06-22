#!/usr/bin/env python3
# Author: Indrajit Ghosh
# Created On: Jun 22, 2024
# 
import os
import sys
import subprocess

# ANSI escape sequences for colors
GREEN_BOLD = "\033[1;32m"
RESET = "\033[0m"

def colored_print(message):
    """Print a message in bold green color."""
    print(GREEN_BOLD + message + RESET)

def run_command(command):
    """Run a shell command and print its output."""
    try:
        result = subprocess.run(command, shell=True, check=True, text=True, capture_output=True)
        print(result.stdout)
        if result.stderr:
            print(result.stderr, file=sys.stderr)
    except subprocess.CalledProcessError as e:
        print(f"Error running command '{command}': {e}")
        print(e.output)
        return False
    return True

def main():
    if len(sys.argv) != 2:
        print("Usage: {} <OVERLEAF_GIT_URL>".format(sys.argv[0]))
        sys.exit(1)

    overleaf_git_url = sys.argv[1]
    
    # Change to the current working directory
    cwd = os.getcwd()
    colored_print(f"Changing to the current working directory: {cwd}")

    os.chdir(cwd)

    # Step 1: Checkout the master branch
    colored_print("Checking out the master branch...")
    if not run_command("git checkout master"):
        sys.exit(1)

    # Step 2: Add the Overleaf remote repository
    colored_print("Adding the Overleaf remote repository...")
    if not run_command(f"git remote add overleaf {overleaf_git_url}"):
        sys.exit(1)

    # Step 3: Pull the master branch from the Overleaf remote repository, allowing unrelated histories
    colored_print("Pulling the master branch from Overleaf, allowing unrelated histories...")
    if not run_command("git pull overleaf master --allow-unrelated-histories"):
        # Handle failure as needed, e.g., continue with a warning
        colored_print("Warning: Pull command failed. Proceeding with script...")

    # Step 4: Stage all changes for commit
    colored_print("Staging all changes...")
    if not run_command("git add ."):
        sys.exit(1)

    # Step 5: Commit the changes with a message
    colored_print("Committing the changes...")
    if not run_command('git commit -m "allowed unrelated histories"'):
        sys.exit(1)

    # Inform the user about Step 6: Revert the latest commit
    colored_print("Step 6: Reverting the latest commit...")
    colored_print("git revert --mainline 1 HEAD")
    colored_print("Skipping actual execution...\n\n")

    # Inform the user about Step 7: Push the changes to Overleaf
    colored_print("Step 7: Pushing the changes to Overleaf...")
    colored_print("git push overleaf master")
    colored_print("Skipping actual execution...\n")


if __name__ == "__main__":
    main()
