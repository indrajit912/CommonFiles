"""
Author: Indrajit Ghosh
Created On: Sep 27, 2023

This script loads environment variables from a .env file using the dotenv library.
It retrieves the value of a specific environment variable, YOUR_VAR_SAVED_IN_DOT_ENV,
and assigns it to the variable YOUR_VAR_SAVED_IN_DOT_ENV.

Make sure to customize the environment variable name ("YOUR_VAR_SAVED_IN_DOT_ENV")
based on your actual use case.
"""

import os
from os.path import join, dirname
from dotenv import load_dotenv

# Define the path to the .env file
dotenv_path = join(dirname(__file__), '.env')

# Load environment variables from the .env file
load_dotenv(dotenv_path)

# Retrieve the value of the environment variable and store it in a variable
YOUR_VAR_SAVED_IN_DOT_ENV = os.environ.get("YOUR_VAR_SAVED_IN_DOT_ENV")

# Note: Replace "YOUR_VAR_SAVED_IN_DOT_ENV" with the actual environment variable name.
